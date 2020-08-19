import os

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow

from parser import Utils
from parser.Application import Application
from gui import Settings
from gui import Ui_MainWindow
import sys


# utils = Utils()
# BASE_PATH = os.path.dirname(utils.getRootDir())


class MyWindow(Ui_MainWindow, QMainWindow, Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.utils = Utils()
        self.settings = QtCore.QSettings(os.path.dirname(self.utils.getRootDir()) + '/parser.ini', QtCore.QSettings.IniFormat)
        QApplication.setOrganizationName('Sergey Smirnov')
        QApplication.setApplicationName('parser')
        QApplication.setApplicationVersion('lite_0.1')
        self.setWindowTitle('Парсер интернет страниц (Lite)')

        self.set_settings()
        self.save_btn.clicked.connect(self.save_settings)
        self.save_btn.click()
        self.start_btn.clicked.connect(self.on_start)

        if not os.path.isdir(os.path.dirname(self.utils.getRootDir()) + '/results'):
            os.mkdir(os.path.dirname(self.utils.getRootDir()) + '/results')


    def on_start(self):
        self.save_btn.click()
        self.save_btn.setEnabled(False)
        self.start_btn.setEnabled(False)
        app = Application(self, self.settings)
        app.procces()
        self.save_btn.setEnabled(True)
        self.start_btn.setEnabled(True)



app = QApplication()
window = MyWindow()
window.show()
sys.exit(app.exec_())
