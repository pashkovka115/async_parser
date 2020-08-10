import logging.config
import os

from parser.logger import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('asynchronous_logger')

# todo: В разработке

class Writer:
    def __init__(self, domain, data, page_type, dir_name=None, context='csv', append=True):
        try:

            if not bool(dir_name):
                self.dir_name = str(os.path.dirname(__file__))
            else:
                self.dir_name = dir_name

            if not bool(context):
                context = ''
                self.context = context
            else:
                self.context = context

            self.page_type = page_type
            self.domain = domain
            self.append = append

            self.data = data
            # self.dir_name = dir_name
            self.filename = self.dir_name + '/' + page_type + '.' + context

            # logger.debug('Writer self.filename:' + self.filename)
            # logger.debug('Writer dir_name:' + self.dir_name)
            # logger.debug('Writer page_type:' + page_type)
            # logger.debug('Writer context:' + context)

        except Exception as e:
            logger.exception(e)


    def save_as(self):
        if self.context == 'csv':
            self.csv()
        elif self.context == 'txt':
            self.txt()
        elif self.context == 'json':
            self.json()
        elif self.context == 'xml':
            self.xml()


    def csv(self):
        with open(self.filename, 'a') as f:
            f.write(str(self.data) + '\n')
        # print(self.data)
        # exit()
        # fn = self.__get_file_name()
        # for k, v in self.data.items():
        #     print(k, v)
        # exit()


    def txt(self):
        print(self.data)


    def json(self):
        print(self.data)


    def xml(self):
        print(self.data)


    def __get_file_name(self):
        url = self.data['url'].replace(self.domain, '')
        if url.startswith('/'):
            url = url[1:]
        return url.replace('/', '_')
