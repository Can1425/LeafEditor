from UI.AboutUI import Ui_MainWindow

import markdown

import sys

from PySide6.QtWidgets import *

from PySide6.QtCore import QStringListModel

from qt_material import apply_stylesheet

import os

import webbrowser

# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.GithubButton.clicked.connect(lambda: webbrowser.open("https://github.com/Can1425"))
        self.ui.GiteeButton.clicked.connect(lambda: webbrowser.open("https://gitee.com/Can1425"))
        self.ui.BilibiliButton.clicked.connect(lambda: webbrowser.open("https://space.bilibili.com/3493107983190567"))
        self.ui.BlogButton.clicked.connect(lambda: webbrowser.open("https://can1425.flowecho.org"))

if __name__ == '__main__':
        App = QApplication([])
        Root = MainWindow()
        Root.show()
        App.exec()