import asyncio
import random

# import aiofiles
import sys

import aiohttp
from time import time
from lxml import html, etree
import uvloop
import urllib.parse
from .headers import HEADERS


class Asynchronous:
    def __init__(self, debug=True, semaphore=10):
        self.debug = debug
        self.view_response_html = False
        self.lock = asyncio.Lock()
        self.semaphore = asyncio.Semaphore(semaphore)
        self.runer = False
        self.urls = []
        self.timeout = 30
        self.start_time = time()
        self.tasks = []
        self.result = None
        self.domain = ''
        # ссылка на стартовую или следующую страницу, формируется автоматически. (но всё можно исправить)))
        self.start_url = False
        # xpath для группы страниц для извлечения данных
        self.xpath_get_data = {}
        # xpath ссылки на следующую страницу
        self.xpath_next_href = ''
        # объект в котором будет идти поиск
        self.block_xpath = None
        self.sleep = (2, 5)
        self.proxy = None
        self.response = None


    async def _fetch(self, session, url, *args, **kwargs):
        t1 = time()
        async with session.get(url, timeout=self.timeout, proxy=self.proxy, *args, **kwargs) as response:
            t2 = time()
            self.response = await response
            if self.sleep:
                await asyncio.sleep(random.randint(*self.sleep))
            if self.debug:
                print(round(t2 - t1, 2), 'Response:', response.status, response.url, flush=True)
            if self.view_response_html:
                print(await response.text())
            if response.status == 200:
                return await response.text()


    async def get_data(self, url: str, data_xpath: dict = None, block_xpath: str = None):
        """
        Обрабатывает Request и возвращает распарсенные данные согласно входящих параметров
        :param url: Адрес в интернете
        :param data_xpath: путь поиска в html, если установлен block_xpath поиск будет идти по блочно
        :param block_xpath: блок(и) в которых будет идти поиск с соответствующей сортировкой контента
        :return: Возвращает список html или список словарей с распарсенными данными
        """
        try:
            if data_xpath is None:
                data_xpath = {}
                data_xpath.update(self.xpath_get_data)
            if block_xpath is None:
                block_xpath = self.block_xpath

            async with self.semaphore:
                async with aiohttp.ClientSession(headers=random.choice(HEADERS)) as session:
                    html_page = await self._fetch(session, url)
                    if bool(self.xpath_next_href):
                        try:
                            self.start_url = urllib.parse.urljoin(
                                self.domain,
                                self.xpath(html_page, self.xpath_next_href)[0]
                            )
                        except:
                            self.start_url = ''
                    else:
                        self.start_url = ''
                    # если есть что искать
                    if bool(data_xpath):
                        data = []
                        # если есть общие блоки и надо искать в них
                        if bool(block_xpath):
                            blocks = self.xpath(html_page, block_xpath) or []
                            for block in blocks:
                                item = {}
                                for key in data_xpath.keys():
                                    try:
                                        tmp = self.xpath(
                                            etree.tostring(block).decode("utf-8"),
                                            data_xpath[key]
                                        )
                                        if len(tmp) == 1:
                                            item[key] = tmp[0].strip()
                                        else:
                                            item[key] = tmp
                                    except:
                                        item[key] = data_xpath[key]

                                data.append(item)
                            return data
                        # если контент нужен как общий для страницы или это страница одного объекта
                        else:
                            item = {}
                            for key in data_xpath.keys():
                                try:
                                    tmp = self.xpath(html_page, data_xpath[key])
                                    # print(html_page, data_xpath[key])  # todo
                                    if len(tmp) == 1:
                                        item[key] = tmp[0].strip()
                                    else:
                                        item[key] = tmp
                                except:
                                    item[key] = data_xpath[key]
                            data.append(item)
                            return data
                    else:
                        return html_page
        except Exception as e:
            print(type(e), e, type(self), 'Line:', sys.exc_info()[-1].tb_lineno)


    def add_task(self, task, *args, **kwargs):
        """
        Добавляет задачу
        :param task: ссылка на функцию
        :param args: аргументы для этой функции
        :return: self
        """
        self.tasks.append(asyncio.Task(task(*args, **kwargs)))
        return self


    def set_urls(self, urls: list):
        """
        Скачать только по этим ссылкам
        Формат: [(url, xpath=False), (url, xpath=False),...]
        Добавляет ссылки на интернет ресурсы, из которых в последствии формирует задачи
        """
        self.urls = urls


    def set_domain(self, domain: str):
        self.domain = domain
        return self


    def set_start_url(self, url: str):
        self.start_url = url
        return self


    async def _start(self):
        if len(self.urls) > 0:
            tasks_from_urls = []
            for url in self.urls:
                tasks_from_urls.append(asyncio.Task(self.get_data(*url)))
            self.tasks = self.tasks + tasks_from_urls
            self.runer = await asyncio.gather(*self.tasks)

        elif isinstance(self.start_url, str) and len(self.start_url) > 0:

            if bool(self.start_url):
                self.runer = await asyncio.gather(
                    self.get_data(
                        self.start_url,
                        self.xpath_get_data,
                        self.block_xpath
                    ))

        return self.runer


    def run(self):
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        self.loop = asyncio.get_event_loop()

        self.result = self.loop.run_until_complete(self._start())
        self.loop.close()
        print('Время выполнения:', time() - self.start_time)
        return self.result


    def get_result(self):
        return self.result


    def xpath(self, html_code, xpath):
        try:
            t = html.fromstring(html_code)
            return t.xpath(xpath)
        except:
            return xpath
