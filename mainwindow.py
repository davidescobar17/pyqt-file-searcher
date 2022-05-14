import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import (QMainWindow, QWidget, QTreeView, QFileSystemModel,
    QGridLayout, QApplication, QLabel, QComboBox, QPushButton, QSizePolicy,
    QGridLayout, QHBoxLayout)
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

                filterLabel = QLabel("Name contains:")
                Layout.addWidget(filterLabel, 0, 0)
                self.filterComboBox = QComboBox(self)
                self.filterComboBox.setEditable(True)
                self.filterComboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                Layout.addWidget(self.filterComboBox, 0, 1)

                Layout.addWidget(self.treeView, 1, 0, 1, 2)

                buttonsLayout = QHBoxLayout()
                buttonsLayout.addStretch()
                self.findButton = QPushButton('Find', self)
                self.findButton.clicked.connect(self.find)
                buttonsLayout.addWidget(self.findButton)
                Layout.addLayout(buttonsLayout, 2, 0, 1, 2)

                widget.setLayout(Layout)

        def find(self):
            self.fileSystemModel.setNameFilters(["*" + self.filterComboBox.currentText() + "*"])


if __name__ == '__main__':

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
