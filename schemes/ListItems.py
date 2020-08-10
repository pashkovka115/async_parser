from schemes.Base import Base
import logging.config
from parser.logger import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


class ListItems(Base):

    def get_content(self):
        while True:
            try:
                self.text_response = self._http_query.http_get_request(self._start_url)
                content = self.parser.parse_html(self.text_response)

                yield content

                if not bool(content['next_page']):
                    break
                else:
                    self._start_url = content['next_page']
            except Exception as e:
                logger.exception(e)


