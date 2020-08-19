import logging.config
import os
import sys
from ctypes import *

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


    def getRootDir(self, *args):
        if getattr(sys, 'frozen', False):
            application_path = self.toLongName(os.path.abspath(os.path.dirname(sys.executable)))
        else:
            application_path = os.path.dirname(__file__)
        if args:
            application_path = os.path.join(application_path, os.path.join(*args))
        application_path = application_path.replace('\\', '/')
        return application_path


    def toLongName(self, path):
        if sys.platform.startswith('linux'):
            return path
        '''
        from dos 8.3 format
        '''
        buf = create_unicode_buffer(500)
        windll.kernel32.GetLongPathNameW(path, buf, 500)
        return buf.value

    def get_base_path(self):
        return os.path.dirname(self.getRootDir())
