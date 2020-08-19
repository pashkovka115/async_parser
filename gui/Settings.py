# from os import path
# from PySide2 import QtCore

# class Settings(Ui_MainWindow, QMainWindow):

class Settings:

    # todo: после отладки удалить конструктор
    # def __init__(self):
    #     super().__init__()
    #     self.settings = QtCore.QSettings(path.dirname(__file__) + '/parser.ini', QtCore.QSettings.IniFormat)


    def save_settings(self):
        self.settings.beginGroup('Window')
        self.settings.setValue('geometry', self.geometry())
        self.settings.endGroup()

        self.settings.beginGroup('Parser')
        self.settings.setValue('domain', self.domen_line_edit.text())
        self.settings.setValue('scaner_mode_single', self.radio_single.isChecked())
        self.settings.setValue('scaner_mode_objects', self.radio_objects.isChecked())
        self.settings.setValue('scaner_mode_objects_and_single', self.radio_objects_and_single.isChecked())
        self.settings.setValue('tab_active', self.tabWidget.currentIndex())
        self.settings.endGroup()

        self.settings.beginGroup('Single_tab')
        self.settings.setValue('xpaths_single_elements_text_edit', self.xpaths_single_elements_text_edit.toPlainText())
        self.settings.setValue('single_urls_text_edit', self.single_urls_text_edit.toPlainText())
        self.settings.endGroup()

        self.settings.beginGroup('Objects_tab')
        self.settings.setValue('start_url_line_edit', self.start_url_line_edit.text())
        self.settings.setValue('xpath_objects_line_edit', self.xpath_objects_line_edit.text())
        self.settings.setValue('xpath_singles_pages_line_edit', self.xpath_singles_pages_line_edit.text())
        self.settings.setValue('xpath_next_page_line_edit', self.xpath_next_page_line_edit.text())
        self.settings.setValue('xpaths_objects_elements_text_edit', self.xpaths_objects_elements_text_edit.toPlainText())
        self.settings.setValue('max_page_spin_box', self.max_page_spin_box.value())
        self.settings.endGroup()
    # ##########################################

    def set_settings(self):
        if self.settings.contains('Window/geometry'):
            self.setGeometry(self.settings.value('Window/geometry'))
        else:
            self.resize(1182, 874)

        self.settings.beginGroup('Parser')
        self.domen_line_edit.setText(self.settings.value('domain', 'http://quotes.toscrape.com'))
        self.radio_single.setChecked(self.ret_bool(self.settings.value('scaner_mode_single', True)))
        self.radio_objects.setChecked(self.ret_bool(self.settings.value('scaner_mode_objects', False)))
        self.radio_objects_and_single.setChecked(
            self.ret_bool(self.settings.value('scaner_mode_objects_and_single', False))
        )
        self.tabWidget.setCurrentIndex(int(self.settings.value('tab_active', 0)))
        self.settings.endGroup()

        self.settings.beginGroup('Single_tab')
        self.xpaths_single_elements_text_edit.setText(self.settings.value('xpaths_single_elements_text_edit', ''))
        self.single_urls_text_edit.setText(self.settings.value('single_urls_text_edit', ''))
        self.settings.endGroup()

        self.settings.beginGroup('Objects_tab')
        self.start_url_line_edit.setText(self.settings.value('start_url_line_edit', ''))
        self.xpath_objects_line_edit.setText(self.settings.value('xpath_objects_line_edit', ''))
        self.xpath_singles_pages_line_edit.setText(self.settings.value('xpath_singles_pages_line_edit', ''))
        self.xpath_next_page_line_edit.setText(self.settings.value('xpath_next_page_line_edit', ''))
        self.xpaths_objects_elements_text_edit.setText(self.settings.value('xpaths_objects_elements_text_edit', ''))
        self.max_page_spin_box.setValue(int(self.settings.value('max_page_spin_box', 0)))
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

