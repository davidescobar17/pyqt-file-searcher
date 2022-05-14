# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import (QMainWindow, QWidget, QTreeView, QFileSystemModel,
    QGridLayout, QApplication)
from PyQt5.QtGui import QKeySequence


class MainWindow(QMainWindow):
        def __init__(self):
                QMainWindow.__init__(self)

                widget = QWidget()
                self.setCentralWidget(widget)

                self.setWindowTitle("File Searcher")
                self.setMinimumSize(160,160)
                self.resize(700,600)

                self.treeView = QTreeView()
                self.fileSystemModel = QFileSystemModel(self.treeView)
                self.fileSystemModel.setReadOnly(False)
                self.fileSystemModel.setNameFilterDisables(False)
                root = self.fileSystemModel.setRootPath("/")
                self.treeView.setModel(self.fileSystemModel)
                self.treeView.setRootIndex(root)

                Layout = QGridLayout()

                Layout.addWidget(self.treeView)

                widget.setLayout(Layout)


if __name__ == '__main__':

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
