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
        MainWindow.resize(1237, 872)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setStyleSheet(u"background-color: rgba(12, 141, 39, 191);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;")

        self.verticalLayout.addWidget(self.start_btn)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setStyleSheet(u"background-color: rgb(164, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.save_btn)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.domen_line_edit = QLineEdit(self.groupBox_2)
        self.domen_line_edit.setObjectName(u"domen_line_edit")

        self.horizontalLayout_2.addWidget(self.domen_line_edit)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
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


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.message_box_text_browser = QTextBrowser(self.centralwidget)
        self.message_box_text_browser.setObjectName(u"message_box_text_browser")
        self.message_box_text_browser.setMinimumSize(QSize(0, 80))
        self.message_box_text_browser.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_2.addWidget(self.message_box_text_browser)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab_single = QWidget()
        self.tab_single.setObjectName(u"tab_single")
        self.verticalLayout_3 = QVBoxLayout(self.tab_single)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.tab_single)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.xpaths_single_elements_text_edit = QTextEdit(self.tab_single)
        self.xpaths_single_elements_text_edit.setObjectName(u"xpaths_single_elements_text_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.xpaths_single_elements_text_edit.sizePolicy().hasHeightForWidth())
        self.xpaths_single_elements_text_edit.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.xpaths_single_elements_text_edit)

        self.label_7 = QLabel(self.tab_single)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.single_urls_text_edit = QTextEdit(self.tab_single)
        self.single_urls_text_edit.setObjectName(u"single_urls_text_edit")

        self.verticalLayout_3.addWidget(self.single_urls_text_edit)

        self.tabWidget.addTab(self.tab_single, "")
        self.tab_objects = QWidget()
        self.tab_objects.setObjectName(u"tab_objects")
        self.verticalLayout_4 = QVBoxLayout(self.tab_objects)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, -1, -1, -1)
        self.label = QLabel(self.tab_objects)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.start_url_line_edit = QLineEdit(self.tab_objects)
        self.start_url_line_edit.setObjectName(u"start_url_line_edit")

        self.gridLayout_2.addWidget(self.start_url_line_edit, 0, 1, 1, 1)

        self.label_5 = QLabel(self.tab_objects)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.xpath_singles_pages_line_edit = QLineEdit(self.tab_objects)
        self.xpath_singles_pages_line_edit.setObjectName(u"xpath_singles_pages_line_edit")

        self.gridLayout_2.addWidget(self.xpath_singles_pages_line_edit, 0, 3, 1, 1)

        self.label_4 = QLabel(self.tab_objects)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.xpath_objects_line_edit = QLineEdit(self.tab_objects)
        self.xpath_objects_line_edit.setObjectName(u"xpath_objects_line_edit")

        self.gridLayout_2.addWidget(self.xpath_objects_line_edit, 1, 1, 1, 1)

        self.label_6 = QLabel(self.tab_objects)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.xpath_next_page_line_edit = QLineEdit(self.tab_objects)
        self.xpath_next_page_line_edit.setObjectName(u"xpath_next_page_line_edit")

        self.gridLayout_2.addWidget(self.xpath_next_page_line_edit, 1, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, -1, -1, -1)
        self.label_2 = QLabel(self.tab_objects)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.max_page_spin_box = QSpinBox(self.tab_objects)
        self.max_page_spin_box.setObjectName(u"max_page_spin_box")
        self.max_page_spin_box.setMaximum(999999999)

        self.horizontalLayout_4.addWidget(self.max_page_spin_box)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.label_8 = QLabel(self.tab_objects)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.xpaths_objects_elements_text_edit = QTextEdit(self.tab_objects)
        self.xpaths_objects_elements_text_edit.setObjectName(u"xpaths_objects_elements_text_edit")

        self.verticalLayout_4.addWidget(self.xpaths_objects_elements_text_edit)

        self.tabWidget.addTab(self.tab_objects, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"xpath \u043f\u0443\u0442\u0438 \u043a \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c (\u043e\u0434\u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430)", None))
#if QT_CONFIG(tooltip)
        self.xpaths_single_elements_text_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u043d\u043e\u0432\u0430\u044f \u043f\u0430\u0440\u0430 \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.xpaths_single_elements_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u044e\u0447 : \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"URL \u0410\u0434\u0440\u0435\u0441\u0430", None))
#if QT_CONFIG(tooltip)
        self.single_urls_text_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u043d\u043e\u0432\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.single_urls_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"http://example.com/", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_single), QCoreApplication.translate("MainWindow", u"\u041e\u0434\u0438\u043d\u043e\u0447\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
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
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"  xpath \u043f\u0443\u0442\u0438 \u043a \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c [\u0432 \u043e\u0431\u044a\u0435\u043a\u0442\u0430\u0445] ", None))
#if QT_CONFIG(tooltip)
        self.xpaths_objects_elements_text_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u043d\u043e\u0432\u0430\u044f \u043f\u0430\u0440\u0430 \u0441 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.xpaths_objects_elements_text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043a\u043b\u044e\u0447 : \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_objects), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432", None))
    # retranslateUi

