import logging.config
from settings import logger_config


logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')
# logger.setLevel(logging.DEBUG)
#
# console_handler = logging.StreamHandler()
# logger.addHandler(console_handler)
#
# std_format = logging.Formatter(fmt='{asctime} - {levelname} - {name} - {message}', style='{')
# console_handler.setFormatter(std_format)
#
# file_handler = logging.FileHandler('debug.log', mode='a')
# logger.addHandler(file_handler)
# file_handler.setFormatter(std_format)


def main():
    logger.debug('Enter in to the main()')


if __name__ == '__main__':
    main()

