import os

from PySide2.QtWidgets import QApplication, QMainWindow

from parser import Utils
from parser import Application
from gui import Settings
from gui import Ui_MainWindow
import sys




class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.utils = Utils()
        self.settings = Settings()

        QApplication.setOrganizationName('Sergey Smirnov')
        QApplication.setApplicationName('parser')
        QApplication.setApplicationVersion('lite_0.1')

        self.setWindowTitle('Парсер интернет страниц (Lite)')

        self.settings.set_settings(self)
        self.ui.save_btn.clicked.connect(self.settings.save_settings)
        self.ui.save_btn.click()
        self.ui.start_btn.clicked.connect(self.on_start)

        if not os.path.isdir(os.path.dirname(self.utils.getRootDir()) + '/results'):
            os.mkdir(os.path.dirname(self.utils.getRootDir()) + '/results')



    def on_start(self):
        self.ui.save_btn.click()
        self.ui.save_btn.setEnabled(False)
        self.ui.start_btn.setEnabled(False)
        app = Application(self, self.settings)
        app.procces()
        self.ui.save_btn.setEnabled(True)
        self.ui.start_btn.setEnabled(True)



app = QApplication()
window = MyWindow()
window.show()
sys.exit(app.exec_())
