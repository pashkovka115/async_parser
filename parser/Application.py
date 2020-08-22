import os
from random import randint
from time import sleep

# from gui import Ui_MainWindow
from PySide2 import QtCore
from PySide2.QtCore import Signal

from parser import Utils
from schemes.ListItems import ListItems
from schemes.SingleItem import SingleItem
from parser.Writer import Writer
# from start_app import MyWindow


class Application(QtCore.QThread):

    app_message = Signal(str)

    def __init__(self, window, settings):
        super().__init__()

        self.window = window
        self.settings = settings.get_settings()
        self.domain = self.settings.value('Parser/domain', None)
        self.writer = Writer()
        self.utils = Utils()


    def run(self):
        self.app_message.emit('Получаю настройки')

        self.settings.beginGroup('Parser')
        single_page = self.settings.value('scaner_mode_single')
        objects_page = self.settings.value('scaner_mode_objects')
        single_and_objects_page = self.settings.value('scaner_mode_objects_and_single')
        self.settings.endGroup()

        self.app_message.emit('Начинаю парсить...')
        if single_page:
            self.single_page()
        elif objects_page:
            self.objects_page()
        elif single_and_objects_page:
            self.single_and_objects_page()
        else:
            raise Exception('Не поддерживаемый режим сканирования')

        self.app_message.emit('Парсинг окончен.')
        print('Парсинг окончен.')


    def single_page(self):
        sp_els = str(self.settings.value('Single_tab/xpaths_single_elements_text_edit')).split('\n')
        sp_urls = str(self.settings.value('Single_tab/single_urls_text_edit')).split('\n')
        sp_urls = list(map(str.strip, sp_urls))

        single = SingleItem(
            domain=self.domain,
            elements_xpath=self.resolve_elements_xpaths(sp_els)
        )
        single.add_urls(sp_urls)

        for page in single.get_content():
            self.writer.write_csv_row(os.path.dirname(self.utils.getRootDir()) + '/results/singles_pages.csv', page['elements'])


    def objects_page(self):
        sp_els = str(self.settings.value('Objects_tab/xpaths_objects_elements_text_edit')).split('\n')

        list_parser = ListItems(
            domain=self.domain,
            start_url=self.settings.value('Objects_tab/start_url_line_edit', None),
            blocks_xpath=self.settings.value('Objects_tab/xpath_objects_line_edit', None),
            elements_xpath=self.resolve_elements_xpaths(sp_els),
            xpath_to_singles_links=self.settings.value('Objects_tab/xpath_singles_pages_line_edit', None),
            xpath_next_url=self.settings.value('Objects_tab/xpath_next_page_line_edit', None),
        )

        for page in list_parser.get_content():
            for el in page['elements']:
                self.writer.write_csv_row(os.path.dirname(self.utils.getRootDir()) + '/results/objects_page.csv', el)


    def single_and_objects_page(self):
        sp_obj_els = str(self.settings.value('Objects_tab/xpaths_objects_elements_text_edit')).split('\n')
        sp_single_els = str(self.settings.value('Single_tab/xpaths_single_elements_text_edit')).split('\n')
        count_pages = int(self.settings.value('Objects_tab/max_page_spin_box', 0))

        list_parser = ListItems(
            domain=self.domain,
            start_url=self.settings.value('Objects_tab/start_url_line_edit', None),
            blocks_xpath=self.settings.value('Objects_tab/xpath_objects_line_edit', None),
            elements_xpath=self.resolve_elements_xpaths(sp_obj_els),
            xpath_to_singles_links=self.settings.value('Objects_tab/xpath_singles_pages_line_edit', None),
            xpath_next_url=self.settings.value('Objects_tab/xpath_next_page_line_edit', None),
        )

        for page in list_parser.get_content(count_pages):
            for el in page['elements']:
                self.writer.write_csv_row(os.path.dirname(self.utils.getRootDir()) + '/results/objects_page.csv', el)

            single = SingleItem(
                domain=self.domain,
                elements_xpath=self.resolve_elements_xpaths(sp_single_els)
            )
            single.add_urls(page['singles_links'])

            for single_page in single.get_content():
                flag = False
                for k, v in single_page['elements'].items():
                    if bool(v):
                        flag = True
                if flag:
                    self.writer.write_csv_row(os.path.dirname(self.utils.getRootDir()) + '/results/singles_pages.csv', single_page['elements'])

            sleep(randint(2, 5))



    def resolve_elements_xpaths(self, items):
        els_xpath = {}
        for el in items:
            if el == '' or el is None:
                continue
            op = el.split(':')
            if len(op) == 2:
                els_xpath.update({op[0].strip(): op[1].strip()})
            else:
                raise Exception('Не корректные настройки')

        return els_xpath
