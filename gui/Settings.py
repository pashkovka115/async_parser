from os import path
from PySide2 import QtCore
from parsera.utils import Utils


class Settings:

    def __init__(self, ini_name='parser.ini'):
        super().__init__()
        self.utils = Utils()
        self.settings = QtCore.QSettings(
            path.dirname(self.utils.getRootDir()) + path.sep + ini_name,
            QtCore.QSettings.IniFormat
        )


    def save_settings(self):
        self.settings.beginGroup('Window')
        self.settings.setValue('geometry', self.window.geometry())
        self.settings.endGroup()

        self.settings.beginGroup('Parser')
        self.settings.setValue('domain', self.window.ui.domen_line_edit.text())
        self.settings.setValue('scaner_mode_single', self.window.ui.radio_single.isChecked())
        self.settings.setValue('scaner_mode_objects', self.window.ui.radio_objects.isChecked())
        self.settings.setValue('scaner_mode_objects_and_single', self.window.ui.radio_objects_and_single.isChecked())
        self.settings.setValue('tab_active', self.window.ui.tabWidget.currentIndex())
        self.settings.endGroup()

        self.settings.beginGroup('Single_tab')
        self.settings.setValue('xpaths_single_elements_text_edit',
                               self.window.ui.xpaths_single_elements_text_edit.toPlainText())
        self.settings.setValue('single_urls_text_edit', self.window.ui.single_urls_text_edit.toPlainText())
        self.settings.endGroup()

        self.settings.beginGroup('Objects_tab')
        self.settings.setValue('start_url_line_edit', self.window.ui.start_url_line_edit.text())
        self.settings.setValue('xpath_objects_line_edit', self.window.ui.xpath_objects_line_edit.text())
        self.settings.setValue('xpath_singles_pages_line_edit', self.window.ui.xpath_singles_pages_line_edit.text())
        self.settings.setValue('xpath_next_page_line_edit', self.window.ui.xpath_next_page_line_edit.text())
        self.settings.setValue(
            'xpaths_objects_elements_text_edit',
            self.window.ui.xpaths_objects_elements_text_edit.toPlainText()
        )
        self.settings.setValue('max_page_spin_box', self.window.ui.max_page_spin_box.value())
        self.settings.endGroup()


    def set_settings(self, window):
        self.window = window
        if self.settings.contains('Window/geometry'):
            self.window.setGeometry(self.settings.value('Window/geometry'))
        else:
            self.window.resize(1182, 874)

        self.settings.beginGroup('Parser')
        self.window.ui.domen_line_edit.setText(self.settings.value('domain', 'http://quotes.toscrape.com'))
        self.window.ui.radio_single.setChecked(self.ret_bool(self.settings.value('scaner_mode_single', True)))
        self.window.ui.radio_objects.setChecked(self.ret_bool(self.settings.value('scaner_mode_objects', False)))
        self.window.ui.radio_objects_and_single.setChecked(
            self.ret_bool(self.settings.value('scaner_mode_objects_and_single', False))
        )
        self.window.ui.tabWidget.setCurrentIndex(int(self.settings.value('tab_active', 0)))
        self.settings.endGroup()

        self.settings.beginGroup('Single_tab')
        self.window.ui.xpaths_single_elements_text_edit.setText(
            self.settings.value('xpaths_single_elements_text_edit', ''))
        self.window.ui.single_urls_text_edit.setText(self.settings.value('single_urls_text_edit', ''))
        self.settings.endGroup()

        self.settings.beginGroup('Objects_tab')
        self.window.ui.start_url_line_edit.setText(self.settings.value('start_url_line_edit', ''))
        self.window.ui.xpath_objects_line_edit.setText(self.settings.value('xpath_objects_line_edit', ''))
        self.window.ui.xpath_singles_pages_line_edit.setText(self.settings.value('xpath_singles_pages_line_edit', ''))
        self.window.ui.xpath_next_page_line_edit.setText(self.settings.value('xpath_next_page_line_edit', ''))
        self.window.ui.xpaths_objects_elements_text_edit.setText(
            self.settings.value('xpaths_objects_elements_text_edit', ''))
        self.window.ui.max_page_spin_box.setValue(int(self.settings.value('max_page_spin_box', 0)))
        self.settings.endGroup()


    def ret_bool(self, item):
        """ преобразует строковое значение в булево """
        if isinstance(item, bool):
            return item
        elif isinstance(item, str):
            item = item.lower()
            if item == 'true':
                return True
            elif item == 'false':
                return False

        raise Exception('Что-то пошло не так. Не могу привести к булеву значению.')


    def get_settings(self):
        return self.settings
