import logging.config
import urllib.parse
from .logger import logger_config
from .utils import Utils

logging.config.dictConfig(logger_config)
logger = logging.getLogger('asynchronous_logger')


class Parser(Utils):
    def __init__(self, domain: str, elements_xpath: dict = None,
                 blocks_xpath: str = None, xpath_to_singles_links=None, xpath_next_url=None):

        if not isinstance(domain, str):
            logger.critical(f'domain - должен быть строкой (domain={domain})')

        if not blocks_xpath is None and not isinstance(blocks_xpath, str):
            logger.critical(
                f'blocks_xpath - должен быть строкой - xpath_to_more_blocks (blocks_xpath={blocks_xpath})')

        if not elements_xpath is None and not isinstance(elements_xpath, dict):
            logger.critical(
                f'elements_xpath - должен быть словарём {{"ключ_для_сохранения":"xpath_to_element"}} (elements_xpath={elements_xpath})')

        if not xpath_to_singles_links is None and not isinstance(xpath_to_singles_links, str):
            logger.critical(
                f'xpath_collect_links - должен быть строкой - xpath для добавления в задачи (xpath_collect_links={xpath_to_singles_links})')

        if not xpath_next_url is None and not isinstance(xpath_next_url, str):
            logger.critical(
                f'xpath_next_url - должен быть строкой - xpath для добавления в задачи (xpath_next_url={xpath_next_url})')

        self.__domain = domain
        self.__page_list_elements_xpath = elements_xpath
        self.__blocks_xpath = blocks_xpath
        self.__xpath_to_singles_links = xpath_to_singles_links
        self.__xpath_next_url = xpath_next_url
        self.__url_to_next_page = None
        self.__to_singles_links = []

        #     todo: временно
        # self.parse_html(self.file_get_contents('test_list_page.html'))


    # todo: потом сюда подать текст от http response
    def parse_html(self, html):
        singles_links = []
        blocks = {}
        next_page = None

        # если блоки определены
        if bool(self.__blocks_xpath):
            blocks = self.__parse_blocks(html)  # keys: elements, url_to_single
        # иначе если блоки НЕ определены
        elif bool(self.__page_list_elements_xpath):
            blocks = self.__get_xpaths_elements(html, self.__page_list_elements_xpath)

        # ссылки на одиночные страницы (если заданы)
        if bool(self.__xpath_to_singles_links):
            singles_links = self.__get_xpath_elements(html, self.__xpath_to_singles_links)
            for i, val in enumerate(singles_links):
                singles_links[i] = urllib.parse.urljoin(self.__domain, val)

        if bool(self.__xpath_next_url):
            url = self.xpath_one(html, self.__xpath_next_url)
            if bool(url):
                self.__url_to_next_page = urllib.parse.urljoin(self.__domain, url)
            else:
                self.__url_to_next_page = None

        self.__to_singles_links = singles_links

        # print({'elements': blocks, 'singles_links': singles_links, 'next_page': self.__url_to_next_page})
        return {'elements': blocks, 'singles_links': singles_links, 'next_page': self.__url_to_next_page}


    #     todo: временно (только для отладки, потом удалить этот метод)
    # def save(self):
    #     # todo: потом сюда подать текст от http response
    #     blocks = self.parse_html(self.file_get_contents('test_list_page.html'))
    #     # Блоки определены (элементы групируются по блочно)
    #     if isinstance(blocks, list):
    #         for block in blocks:
    #             print(block)
    #
    #     # Блоки НЕ определены (элементы групируются по типам)
    #     elif isinstance(blocks, dict):
    #         for key, val in blocks.items():
    #             print(key, ':', val)


    def __parse_blocks(self, html):
        blocks = self.__get_xpath_elements(html, self.__blocks_xpath)
        blocks_elem = []
        if bool(self.__page_list_elements_xpath):
            for block in blocks:
                blocks_elem.append(
                    self.__get_xpaths_elements(block, self.__page_list_elements_xpath)
                )
        return blocks_elem


    def __get_xpath_elements(self, html: str, xpath: str):
        return self.xpath(html, xpath)


    def __get_xpaths_elements(self, html: str, xpaths: dict):
        D = dict()
        for key, xpath in xpaths.items():
            t = self.xpath(html, xpath)
            if bool(t) and len(t) == 1:
                t = t[0]
            D[key] = t
        return D


    def file_get_contents(self, file: str, clear_spaces: bool = False) -> str:
        with open(file, mode='r') as f:
            if clear_spaces:
                return f.read().replace('\n', '')
            return f.read()

    # def __get_blocks(self, html):
    #     return self.xpath(html, self.__blocks_xpath)

    # def __get_collect_links(self, html):
    #     links = self.xpath(html, self.__xpath_to_singles_links)
    #     for i, link in enumerate(links):
    #         links[i] = urllib.parse.urljoin(self.__domain, link)
    #
    #     if bool(links) and len(links) == 1:
    #         return links[0]
    #     return links

# def clear(self):
#     self.__collect_links = []
#
# def get_collect_links(self):
#     return self.__collect_links


# def get_url_to_next_page(self):
#     return self.__url_to_next_page


# def __get_elements(self, html):
#     item = {}
#     for key, xpath in self.__save_block_elements_xpath.items():
#         try:
#             t = self.xpath(html, xpath)
#             if len(t) == 1:
#                 t = t[0]
#             item[key] = t
#         except Exception as e:
#             logger.exception(e)
#     return item
