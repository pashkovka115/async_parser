from schemes.Base import Base
import logging.config
from parser.logger import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


class SingleItem(Base):

    def get_content(self):
        try:
            self.text_response = self._http_query.run()
            if bool(self.text_response):
                for page in self.text_response:
                    yield self.parser.parse_html(page['text'])
            else:
                return None

        except Exception as e:
            logger.exception(e)



    def add_urls(self, urls:list):
        self._http_query.add_urls(urls)


