# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parser.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1182, 886)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(10, 190, 1161, 661))
        self.tab_single = QWidget()
        self.tab_single.setObjectName(u"tab_single")
        self.groupBox = QGroupBox(self.tab_single)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 1141, 341))
        self.xpaths_single_elements_text_edit = QTextEdit(self.groupBox)
        self.xpaths_single_elements_text_edit.setObjectName(u"xpaths_single_elements_text_edit")
        self.xpaths_single_elements_text_edit.setGeometry(QRect(0, 20, 1141, 321))
        self.groupBox_5 = QGroupBox(self.tab_single)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 370, 1131, 291))
        self.single_urls_text_edit = QTextEdit(self.groupBox_5)
        self.single_urls_text_edit.setObjectName(u"single_urls_text_edit")
        self.single_urls_text_edit.setGeometry(QRect(0, 20, 1131, 241))
        self.tabWidget.addTab(self.tab_single, "")
        self.tab_objects = QWidget()
        self.tab_objects.setObjectName(u"tab_objects")
        self.groupBox_4 = QGroupBox(self.tab_objects)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 160, 1161, 501))
        self.xpaths_objects_elements_text_edit = QTextEdit(self.groupBox_4)
        self.xpaths_objects_elements_text_edit.setObjectName(u"xpaths_objects_elements_text_edit")
        self.xpaths_objects_elements_text_edit.setGeometry(QRect(0, 20, 1161, 451))
        self.layoutWidget = QWidget(self.tab_objects)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1131, 91))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.start_url_line_edit = QLineEdit(self.layoutWidget)
        self.start_url_line_edit.setObjectName(u"start_url_line_edit")

        self.gridLayout_2.addWidget(self.start_url_line_edit, 0, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.xpath_singles_pages_line_edit = QLineEdit(self.layoutWidget)
        self.xpath_singles_pages_line_edit.setObjectName(u"xpath_singles_pages_line_edit")

        self.gridLayout_2.addWidget(self.xpath_singles_pages_line_edit, 0, 3, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.xpath_objects_line_edit = QLineEdit(self.layoutWidget)
        self.xpath_objects_line_edit.setObjectName(u"xpath_objects_line_edit")

        self.gridLayout_2.addWidget(self.xpath_objects_line_edit, 1, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.xpath_next_page_line_edit = QLineEdit(self.layoutWidget)
        self.xpath_next_page_line_edit.setObjectName(u"xpath_next_page_line_edit")

        self.gridLayout_2.addWidget(self.xpath_next_page_line_edit, 1, 3, 1, 1)

        self.layoutWidget1 = QWidget(self.tab_objects)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 110, 251, 28))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.max_page_spin_box = QSpinBox(self.layoutWidget1)
        self.max_page_spin_box.setObjectName(u"max_page_spin_box")
        self.max_page_spin_box.setMaximum(999999999)

        self.horizontalLayout_4.addWidget(self.max_page_spin_box)

        self.tabWidget.addTab(self.tab_objects, "")
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 11, 1161, 77))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_btn = QPushButton(self.layoutWidget2)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setStyleSheet(u"background-color: rgba(12, 141, 39, 191);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;")

        self.verticalLayout.addWidget(self.start_btn)

        self.save_btn = QPushButton(self.layoutWidget2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setStyleSheet(u"background-color: rgb(164, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.save_btn)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.groupBox_2 = QGroupBox(self.layoutWidget2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.domen_line_edit = QLineEdit(self.groupBox_2)
        self.domen_line_edit.setObjectName(u"domen_line_edit")

        self.horizontalLayout_2.addWidget(self.domen_line_edit)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.layoutWidget2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_single = QRadioButton(self.groupBox_3)
        self.radio_single.setObjectName(u"radio_single")
        self.radio_single.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_single)

        self.radio_objects = QRadioButton(self.groupBox_3)
        self.radio_objects.setObjectName(u"radio_objects")

        self.horizontalLayout.addWidget(self.radio_objects)

        self.radio_objects_and_single = QRadioButton(self.groupBox_3)
        self.radio_objects_and_single.setObjectName(u"radio_objects_and_single")

        self.horizontalLayout.addWidget(self.radio_objects_and_single)


        self.horizontalLayout_3.addWidget(self.groupBox_3)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 100, 1161, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.message_box_text_browser = QTextBrowser(self.verticalLayoutWidget)
        self.message_box_text_browser.setObjectName(u"message_box_text_browser")

        self.verticalLayout_2.addWidget(self.message_box_text_browser)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u044e\u0447\u0438 \u0431\u0443\u0434\u0443\u0442 \u0438\u043c\u0435\u043d\u0430\u043c\u0438 \u043f\u043e\u043b\u0435\u0439 CSV", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"xpath \u043f\u0443\u0442\u0438 \u043a \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c (\u043e\u0434\u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430)", None))
#if QT_CONFIG(tooltip)
        self.xpaths_single_elements_text_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u043d\u043e\u0432\u0430\u044f \u043f\u0430\u0440\u0430 \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.xpaths_single_elements_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u044e\u0447 : \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441\u0430 URL", None))
#if QT_CONFIG(tooltip)
        self.single_urls_text_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u043d\u043e\u0432\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.single_urls_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"http://example.com/", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_single), QCoreApplication.translate("MainWindow", u"\u041e\u0434\u0438\u043d\u043e\u0447\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
#if QT_CONFIG(tooltip)
        self.groupBox_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u044e\u0447\u0438 \u0431\u0443\u0434\u0443\u0442 \u0438\u043c\u0435\u043d\u0430\u043c\u0438 \u043f\u043e\u043b\u0435\u0439 CSV", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"xpath \u043f\u0443\u0442\u0438 \u043a \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c [\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u0445] ", None))
#if QT_CONFIG(tooltip)
        self.xpaths_objects_elements_text_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u043d\u043e\u0432\u0430\u044f \u043f\u0430\u0440\u0430 \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.xpaths_objects_elements_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u044e\u0447 : \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421 \u044d\u0442\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043d\u0430\u0447\u043d\u0451\u0442\u0441\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u044b\u0439 URL \u0430\u0434\u0440\u0435\u0441", None))
#if QT_CONFIG(tooltip)
        self.start_url_line_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421 \u044d\u0442\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043d\u0430\u0447\u043d\u0451\u0442\u0441\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0434\u0443\u0442 \u0441\u043e\u0431\u0438\u0440\u0430\u0442\u044c\u0441\u044f \u0441\u0441\u044b\u043b\u043a\u0438 \u0434\u043b\u044f \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430 \u043e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446. \n"
"\u0415\u0441\u043b\u0438 \u0443\u043a\u0430\u0437\u0430\u043d \u043f\u0443\u0442\u044c \u043a \u043e\u0431\u044a\u0435\u043a\u0442\u0443, \u043f\u043e\u0438\u0441\u043a \u0431\u0443\u0434\u0435\u0442 \u0432\u0435\u0441\u0442\u0438\u0441\u044c \u0432\u043d\u0443\u0442\u0440\u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u0430.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"xpath \u043d\u0430 \u043e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b", None))
#if QT_CONFIG(tooltip)
        self.xpath_singles_pages_line_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0434\u0443\u0442 \u0441\u043e\u0431\u0438\u0440\u0430\u0442\u044c\u0441\u044f \u0441\u0441\u044b\u043b\u043a\u0438 \u0434\u043b\u044f \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430 \u043e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0445 \u0441\u0442\u0440\u0430\u043d\u0438\u0446", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a DIV \u0431\u043b\u043e\u043a\u0430\u043c \u043e\u0434\u043d\u043e\u0433\u043e \u0442\u043e\u0432\u0430\u0440\u0430 \u0432 \u043b\u0435\u043d\u0442\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"xpath \u043a \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u043c", None))
#if QT_CONFIG(tooltip)
        self.xpath_objects_line_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a DIV \u0431\u043b\u043e\u043a\u0430\u043c \u043e\u0434\u043d\u043e\u0433\u043e \u0442\u043e\u0432\u0430\u0440\u0430 \u0432 \u043b\u0435\u043d\u0442\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0441\u0441\u044b\u043b\u043a\u0435 \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0443\u044e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"xpath \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0443\u044e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443", None))
#if QT_CONFIG(tooltip)
        self.xpath_next_page_line_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0441\u0441\u044b\u043b\u043a\u0435 \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0443\u044e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446 \u043c\u0430\u043a\u0441\u0438\u043c\u0443\u043c", None))
#if QT_CONFIG(tooltip)
        self.max_page_spin_box.setToolTip(QCoreApplication.translate("MainWindow", u"0 - \u043d\u0435 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043e", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_objects), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0435\u043d", None))
        self.domen_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"http://example.com", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c", None))
#if QT_CONFIG(tooltip)
        self.radio_single.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0442\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u043e\u0434\u043d\u043e\u0433\u043e \u0442\u043e\u0432\u0430\u0440\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.radio_single.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e \u043e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b", None))
#if QT_CONFIG(tooltip)
        self.radio_objects.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u043e\u0432\u0430\u0440\u043e\u0432 \u0438\u043b\u0438 \u043b\u0435\u043d\u0442\u0430 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439 \u043d\u0430 \u043e\u0434\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435", None))
#endif // QT_CONFIG(tooltip)
        self.radio_objects.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e \u0441\u043f\u0438\u0441\u043a\u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432", None))
        self.radio_objects_and_single.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043a\u0438 + \u041e\u0434\u0438\u043d\u043e\u0447\u043d\u044b\u0435", None))
    # retranslateUi

