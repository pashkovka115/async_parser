import csv
import logging.config
import os

from parser.logger import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('asynchronous_logger')

# todo: В разработке

class Writer:

    def write_csv_row(self, file_name, data:dict, order=None, mode='a'):

        with open(file_name, mode=mode) as file:
            if not bool(order):
                order = list(data.keys())
                order.sort()

            writer = csv.DictWriter(file, fieldnames=order)
            if os.path.isfile(file_name) and os.path.getsize(file_name) == 0:
               writer.writeheader()

            writer.writerow(data)
