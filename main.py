

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
from src.script import compress_kopiri


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('desing.ui', self)

        self.selectFileButton.clicked.connect(self.openFileNamesDialog)
        self.bt_submit.clicked.connect(self.compress)
        self.fileName = []

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Python Files (*.py)", options=options)

        if files:
            self.fileName = files
            self.textEdit.setText('\n'.join(files))

    def compress(self):
        print(self.fileName)
        print(self.fileName[0])
        compress_kopiri(self)
        self.textEdit.setText('\n'"compressing")


app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())
