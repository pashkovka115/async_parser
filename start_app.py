import os

from PySide2.QtWidgets import QApplication, QMainWindow

from parsera import Utils
from parsera import Application
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

        self.app_thread = Application(self, self.settings)
        # app.run()
        self.app_thread.app_message.connect(self.add_message)



    def on_start(self):
        self.ui.message_box_text_browser.clear()
        self.ui.save_btn.click()
        self.ui.save_btn.setEnabled(False)
        self.ui.start_btn.setEnabled(False)

        self.app_thread.start()

        self.ui.save_btn.setEnabled(True)
        self.ui.start_btn.setEnabled(True)


    def add_message(self, value):
        self.ui.message_box_text_browser.append(value)



app = QApplication()
window = MyWindow()
window.show()
sys.exit(app.exec_())
