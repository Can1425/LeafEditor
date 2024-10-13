# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AppUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QDockWidget,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QSizePolicy, QSpacerItem, QStatusBar,
    QTextBrowser, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1130, 698)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.NewButton = QToolButton(self.centralwidget)
        self.NewButton.setObjectName(u"NewButton")

        self.horizontalLayout.addWidget(self.NewButton)

        self.OpenButton = QToolButton(self.centralwidget)
        self.OpenButton.setObjectName(u"OpenButton")

        self.horizontalLayout.addWidget(self.OpenButton)

        self.SaveButton = QToolButton(self.centralwidget)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout.addWidget(self.SaveButton)

        self.AboutButton = QToolButton(self.centralwidget)
        self.AboutButton.setObjectName(u"AboutButton")

        self.horizontalLayout.addWidget(self.AboutButton)

        self.MarkDownCheck = QCheckBox(self.centralwidget)
        self.MarkDownCheck.setObjectName(u"MarkDownCheck")
        self.MarkDownCheck.setChecked(True)

        self.horizontalLayout.addWidget(self.MarkDownCheck)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.NameTitle = QLabel(self.centralwidget)
        self.NameTitle.setObjectName(u"NameTitle")

        self.horizontalLayout_3.addWidget(self.NameTitle)

        self.NameEdit = QLineEdit(self.centralwidget)
        self.NameEdit.setObjectName(u"NameEdit")

        self.horizontalLayout_3.addWidget(self.NameEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.TextEdit = QTextEdit(self.centralwidget)
        self.TextEdit.setObjectName(u"TextEdit")

        self.horizontalLayout_4.addWidget(self.TextEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.FileList = QDockWidget(MainWindow)
        self.FileList.setObjectName(u"FileList")
        self.FileList.setLayoutDirection(Qt.LeftToRight)
        self.FileList.setFloating(False)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.FileListTitle = QCommandLinkButton(self.dockWidgetContents_4)
        self.FileListTitle.setObjectName(u"FileListTitle")

        self.verticalLayout_3.addWidget(self.FileListTitle)

        self.listView = QListView(self.dockWidgetContents_4)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_3.addWidget(self.listView)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.FileList.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.FileList)
        self.dockWidget_4 = QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName(u"dockWidget_4")
        self.dockWidgetContents_6 = QWidget()
        self.dockWidgetContents_6.setObjectName(u"dockWidgetContents_6")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.TextBrowserTitle = QCommandLinkButton(self.dockWidgetContents_6)
        self.TextBrowserTitle.setObjectName(u"TextBrowserTitle")

        self.verticalLayout_5.addWidget(self.TextBrowserTitle)

        self.TextBrowser = QTextBrowser(self.dockWidgetContents_6)
        self.TextBrowser.setObjectName(u"TextBrowser")

        self.verticalLayout_5.addWidget(self.TextBrowser)

        self.dockWidget_4.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LeafEditor", None))
        self.NewButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u6587\u6863", None))
        self.OpenButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u6863", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5f53\u524d", None))
        self.AboutButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.MarkDownCheck.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790 MarkDownn", None))
        self.NameTitle.setText(QCoreApplication.translate("MainWindow", u"\u6587\u6863\u540d", None))
        self.NameEdit.setText("")
        self.NameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Doc Name", None))
#if QT_CONFIG(statustip)
        self.TextEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.TextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write Something...", None))
        self.FileList.setWindowTitle(QCoreApplication.translate("MainWindow", u"./UserFile \u4e2d\u7684 ...", None))
        self.FileListTitle.setText(QCoreApplication.translate("MainWindow", u"./UserFile \u4e2d\u7684 ...", None))
        self.dockWidget_4.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9884\u89c8\u5668", None))
        self.TextBrowserTitle.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
    # retranslateUi

