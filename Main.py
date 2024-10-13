from UI.AppUI import Ui_MainWindow

import markdown

import sys

from PySide6.QtWidgets import *

from PySide6.QtCore import QStringListModel, QCoreApplication

from qt_material import apply_stylesheet

import os

# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.TextEdit.textChanged.connect(self.EditorEditChange)
        self.ui.NameEdit.textChanged.connect(self.TextBrowserTitleChange)
        
        self.file = os.listdir('./UserFile')
        self.fileModel = QStringListModel(self.file)
        self.ui.listView.setModel(self.fileModel)

        self.ui.listView.clicked.connect(self.ListClicked)
        self.ui.SaveButton.clicked.connect(self.SaveButtonClicked)
        self.ui.NewButton.clicked.connect(self.NewButtonClicked)
        self.ui.OpenButton.clicked.connect(self.OpenButtonClicked)
        self.ui.MarkDownCheck.stateChanged.connect(self.EditorEditChange)
        self.ui.AboutButton.clicked.connect(self.AboutButtonClicked)
        # self.ui.Cancel.triggered.connect(self.CancelButtonClicked)
        # self.ui.RecoverButton.clicked.connect(self.RecoverButtonClicked)

    def TextBrowserTitleChange(self):
        getTitle = self.ui.NameEdit.text()
        self.ui.TextBrowserTitle.setText("预览：{}".format(getTitle))

    def EditorEditChange(self):
        getText = self.ui.TextEdit.toPlainText()
        if self.ui.MarkDownCheck.isChecked():
            self.ui.TextBrowser.setText(markdown.markdown(getText))
        else:
            self.ui.TextBrowser.setText(getText)
    
    def CancelButtonClicked(self):
        self.ui.TextEdit.undo()

    def RecoverButtonClicked(self):
        self.ui.TextEdit.redo()

    def ListClicked(self, model_index):
        clickedFile = self.file[model_index.row()]
        self.ui.NameEdit.setText(clickedFile)
        with open('./UserFile/{}'.format(clickedFile), 'r', encoding='UTF-8') as f:
            self.ui.TextEdit.setText(f.read())

    def SaveButtonClicked(self):
        with open('./UserFile/{}'.format(self.ui.NameEdit.text()), 'w', encoding='UTF-8') as f:
            f.write(self.ui.TextEdit.toPlainText())
        self.file = os.listdir('./UserFile')
        self.fileModel = QStringListModel(self.file)
        self.ui.listView.setModel(self.fileModel)
    
    def NewButtonClicked(self):
        self.ui.TextEdit.setText("")
        self.ui.NameEdit.setText("New_Docs")

    def OpenButtonClicked(self):
        fileName = QFileDialog.getOpenFileName(None, '请选择打开的文档', '', 'file(*.md *.txt *)')
        with open(fileName[0], 'r', encoding='UTF-8') as f:
            self.ui.TextEdit.setText(f.read())
    
    def AboutButtonClicked(self):
        import About
        self.AboutWindow = About.MainWindow()
        self.AboutWindow.show()

if __name__ == '__main__':
        App = QApplication([])
        Root = MainWindow()
        Root.show()
        App.exec()