import logging.config

from lxml import html, etree
from lxml.html import HtmlElement
from parser.logger import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('asynchronous_logger')


class Utils:
    def xpath(self, html_code, xpath):
        try:
            L = []
            t = html.fromstring(html_code)
            for i in t.xpath(xpath):
                if isinstance(i, HtmlElement):
                    L.append(etree.tostring(i).decode("utf-8").strip())
                else:
                    L.append(str(i).strip())

            return L
        except Exception as e:
            logger.exception(e)


    def xpath_one(self, html_code, xpath):
        r = self.xpath(html_code, xpath)
        if r and len(r) > 0:
            return r[0]
        return None
