import asyncio
import logging.config
import random
import urllib.parse
from time import time
import requests
import aiohttp
import uvloop

from parser.headers import HEADERS
from parser.logger import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('asynchronous_logger')


class HTTPQuery:
    def __init__(
            self, domain: str, start_url: str = None, semaphore: int = 10,
            sleeping=(2, 5), timeout=30, proxy=None
    ):

        if not hasattr(sleeping, '__iter__') or len(sleeping) != 2 or sleeping[0] > sleeping[1]:
            logger.critical(
                f'sleeping должен быть итерируемый и состоять из начального и конечного значения. (sleeping={sleeping})')

        if not isinstance(domain, str):
            logger.critical(f'domain - должен быть строкой (domain={domain})')

        if not isinstance(timeout, int):
            logger.critical(f'timeout - должен быть числом (timeout={timeout})')

        if not isinstance(start_url, str):
            logger.critical(f'start_url - должен быть строкой (start_url={start_url})')

        if not isinstance(semaphore, int):
            logger.critical(f'semaphore - должен быть числом (semaphore={semaphore})')

        self.__sleeping = sleeping
        self.__domain = domain
        # self.__lock = asyncio.Lock() todo: добавляю thread, вместе с ним нехочет работать
        # self.__semaphore = asyncio.Semaphore(semaphore)
        self.__semaphore = semaphore
        self.__timeout = timeout
        self.__proxy = proxy  # todo: сделать проверку на соответствие типа
        self.__urls = set()
        self.start_url = start_url
        # self.__urls.add(start_url)
        self.__history_links = set()
        self.__tasks = []
        self.__start_time = time()
        self.session = None


    def clear(self):
        self.__urls = set()
        self.__tasks = []


    def add_urls(self, urls: list):
        try:
            logger.info(f'Добавлено {len(urls)} ссылок')
            i = 1
            for url in urls:
                if not url in self.__history_links:
                    self.__urls.add(urllib.parse.urljoin(self.__domain, url))
                    self.__history_links.add(urllib.parse.urljoin(self.__domain, url))
                    logger.info(f'{i}. Добавляется {url} ссылка. Всего ссылок в задаче: {len(self.__urls)}')
                i += 1
            return self
        except Exception as e:
            logger.exception(e)


    def add_url(self, url: str):
        if not url in self.__history_links:
            self.__urls.add(urllib.parse.urljoin(self.__domain, url))
            self.__history_links.add(urllib.parse.urljoin(self.__domain, url))
            logger.debug(
                f'Добавляется ссылка: {urllib.parse.urljoin(self.__domain, url)}. Ссылок в задаче: {len(self.__urls)}')


    # def add_task(self, task, *args, **kwargs):
    #     self.__tasks.append(asyncio.Task(task(*args, **kwargs)))
    #     return self

    async def _fetch(self, session, url, *args, **kwargs):
        t1 = time()
        async with session.get(url, timeout=self.__timeout, proxy=self.__proxy, *args,
                               **kwargs) as response:
            t2 = time()
            # self.response = await response
            if self.__sleeping:
                await asyncio.sleep(random.randint(*self.__sleeping))

            logger.info(
                f"Сервер ответил за {round(t2 - t1, 2)} сек. 'Статус:', {response.status}, {response.url}"
            )

            if response.status == 200:
                return {'text': await response.text(), 'url': response.url}
            else:
                logger.warning(
                    f'Статус ответа: {response.status}. Ссылка: {response.url}')
                return None


    # url = "https://www.ebay.com/signin/s"
    # data_login = {"userid": "frank345345.zuver@gmail.com", "pass": "2355235qwe123QWE!!1"}
    #
    # async def http_post_contents(client, url, data):
    #     while True:
    #         try:
    #             async with client.post(url, headers=headers, data=data) as r:
    #                 logger.info(f'Запрос: {url}')
    #                 return await r.text()
    #         except:
    #             time.sleep(1)


    async def http_get_contents(self, sem, url):
        """ асинхронный """
        try:
            async with sem:
                async with aiohttp.ClientSession(headers=random.choice(HEADERS)) as session:
                    self.session = session
                    return await self._fetch(self.session, url)
        except Exception as e:
            logger.exception(e)


    def http_get_request(self, url):
        """ синхронный """
        with requests.Session() as session:
            self.session = session
            r = self.session.get(url, headers=random.choice(HEADERS))
            if r.status_code == 200:
                logger.debug(f'Статус: {r.status_code}, {url}')
                return r.text
            else:
                logger.warning(f'Статус: {r.status_code}, {url}')


    async def __start(self):
        # tasks_from_urls = []
        sem = asyncio.Semaphore(self.__semaphore)
        for url in self.__urls:
            self.__tasks.append(asyncio.Task(self.http_get_contents(sem, url)))

        self.runer = await asyncio.gather(*self.__tasks)

        return self.runer


    def run(self):
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        self.loop = asyncio.get_event_loop()

        self.result = self.loop.run_until_complete(self.__start())
        self.clear()
        self.loop.close()
        logger.info(f"Время выполнения HTTP запросов: {time() - self.__start_time}. Результатов: {len(self.result)}")
        return self.result
