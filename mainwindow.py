import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import (QMainWindow, QWidget, QTreeView, QFileSystemModel,
    QGridLayout, QApplication, QLabel, QComboBox, QPushButton, QSizePolicy,
    QGridLayout, QHBoxLayout, QFileDialog)


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
                self.treeView.setColumnWidth(0, 250)
                self.treeView.setRootIndex(root)

                Layout = QGridLayout()

                filterLabel = QLabel("Name contains:")
                Layout.addWidget(filterLabel, 0, 0)
                self.filterComboBox = QComboBox(self)
                self.filterComboBox.setEditable(True)
                self.filterComboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                Layout.addWidget(self.filterComboBox, 0, 1, 1, 2)

                directoryLabel = QLabel("In directory:")
                Layout.addWidget(directoryLabel, 1, 0)
                self.directoryComboBox = QComboBox(self)
                self.directoryComboBox.setEditable(True)
                self.directoryComboBox.addItem(QDir.currentPath())
                self.directoryComboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
                Layout.addWidget(self.directoryComboBox, 1, 1)
                self.browseButton = QPushButton('Browse', self)
                self.browseButton.clicked.connect(self.browse)
                Layout.addWidget(self.browseButton, 1, 2)

                Layout.addWidget(self.treeView, 2, 0, 1, 3)

                buttonsLayout = QHBoxLayout()
                buttonsLayout.addStretch()
                self.findButton = QPushButton('Find', self)
                self.findButton.clicked.connect(self.find)
                buttonsLayout.addWidget(self.findButton)
                Layout.addLayout(buttonsLayout, 3, 0, 1, 3)

                widget.setLayout(Layout)

        def browse(self):
            directory = QFileDialog.getExistingDirectory(self, "Find Files",
                QDir.currentPath())

            if directory:
                if self.directoryComboBox.findText(directory) == -1:
                    self.directoryComboBox.addItem(directory)

                self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))

                root = self.fileSystemModel.setRootPath(directory)
                self.treeView.setModel(self.fileSystemModel)
                self.treeView.setRootIndex(root)

        def find(self):
            self.fileSystemModel.setNameFilters(["*" + self.filterComboBox.currentText() + "*"])


if __name__ == '__main__':

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
