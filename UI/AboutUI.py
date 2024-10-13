# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutUI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 331)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AboutTitle = QCommandLinkButton(self.centralwidget)
        self.AboutTitle.setObjectName(u"AboutTitle")

        self.verticalLayout.addWidget(self.AboutTitle)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.textBrowser)

        self.GithubButton = QPushButton(self.centralwidget)
        self.GithubButton.setObjectName(u"GithubButton")

        self.verticalLayout.addWidget(self.GithubButton)

        self.GiteeButton = QPushButton(self.centralwidget)
        self.GiteeButton.setObjectName(u"GiteeButton")

        self.verticalLayout.addWidget(self.GiteeButton)

        self.BlogButton = QPushButton(self.centralwidget)
        self.BlogButton.setObjectName(u"BlogButton")

        self.verticalLayout.addWidget(self.BlogButton)

        self.BilibiliButton = QPushButton(self.centralwidget)
        self.BilibiliButton.setObjectName(u"BilibiliButton")

        self.verticalLayout.addWidget(self.BilibiliButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e LeafEditor", None))
        self.AboutTitle.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4e00\u4e2a\u57fa\u4e8e Qt Designer + PySide6 \u6784\u5efa\u7684\u6587\u672c\u7f16\u8f91\u5668\uff0c\u4ec5\u6b64\u800c\u5df2</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u529f\u80fd\u5341\u5206\u7684\u6709\u9650\uff0c\u56e0\u4e3a\u6211\u624d\u5f00\u59cb\u5b66\u4e60 Python \u4ee5\u53ca PySide6\uff0c\u671b\u89c1\u8c05</p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5982\u679c\u4f60\u80fd\u4e2a\u6211\u4e00\u4e9b\u5e2e\u52a9\uff0c\u6211\u53ca\u5176\u613f\u610f\uff0c\u4f46\u8fd9\u4e1c\u897f\u80fd\u88ab\u4eba\u770b\u5230\u5417</p></body></html>", None))
        self.GithubButton.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.GiteeButton.setText(QCoreApplication.translate("MainWindow", u"Gitee", None))
        self.BlogButton.setText(QCoreApplication.translate("MainWindow", u"My Blog\uff08\u4e07\u5e74\u4e0d\u66f4\uff09", None))
        self.BilibiliButton.setText(QCoreApplication.translate("MainWindow", u"Bilibili", None))
    # retranslateUi

