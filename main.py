

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
from src.script import compress_kopiri
from PyQt5 import QtCore

import threading

from PyQt5.QtCore import QThread


class CompresProcess(QThread):
    txt_result = QtCore.pyqtSignal(str)
    le_wi = QtCore.pyqtSignal(str)
    le_wf = QtCore.pyqtSignal(str)
    le_reduce = QtCore.pyqtSignal(str)
    le_state = QtCore.pyqtSignal(str)
    progressBar = QtCore.pyqtSignal(int)

    def __init__(
            self,
            fileName,
            th_xm,
            th_sm,
            optimize,
            weight_max,
            quality,
    ):
        super().__init__()
        self._fileName = fileName
        self._th_xm = th_xm
        self._th_sm = th_sm
        self._optimize = optimize
        self._weight_max = weight_max
        self._quality = quality

    def run(self):
        compress_kopiri(
            self._fileName,
            self._th_xm,
            self._th_sm,
            self._optimize,
            self._weight_max,
            self._quality,
            self.txt_result,
            self.le_wi,
            self.le_wf,
            self.le_reduce,
            self.le_state,
            self.progressBar,
        )


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('desing.ui', self)
        self.selectFileButton.clicked.connect(self.openFileNamesDialog)
        self.bt_submit.clicked.connect(self.initCompress)
        # config default values
        self.fileName = []
        self.th_xm = True
        self.th_sm = True
        self.optimize = True
        self.weight_max = 300000
        self.quality = 60

        self.sd_weight.valueChanged.connect(self.valuechangeWeight)
        self.sd_quality.valueChanged.connect(self.valuechangeQuality)
        self.cb_th_xm.stateChanged.connect(self.checkBoxChangedActionSM)
        self.cb_th_sm.stateChanged.connect(self.checkBoxChangedActionXM)
        self.cb_optimize.stateChanged.connect(
            self.checkBoxChangedActionOptimize)

    def launch_Selenium_Thread(self):
        t = threading.Thread(target=self.compress)
        t.start()

    def valuechangeQuality(self):
        self.quality = self.sd_quality.value()
        self.lb_quality_sd.setText(str(self.quality))

    def valuechangeWeight(self):
        self.weight_max = self.sd_weight.value()
        self.lb_weight.setText(
            str("{0:.1f}".format(self.weight_max/1000))+" KB")

    def checkBoxChangedActionOptimize(self, state):
        if(QtCore.Qt.Checked == state):
            self.optimize = True
        else:
            self.optimize = False

    def checkBoxChangedActionXM(self, state):
        if (QtCore.Qt.Checked == state):
            self.th_xm = True
        else:
            self.th_xm = False

    def checkBoxChangedActionSM(self, state):
        if (QtCore.Qt.Checked == state):
            self.th_sm = True
        else:
            self.th_sm = False

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Python Files (*.py)", options=options)

        if files:
            self.fileName = files
            self.txt_result.append('\n')
            self.txt_result.append("Selected files:")
            self.txt_result.append("----------------------------------")
            self.txt_result.append('\n'.join(files))
            self.txt_result.append("----------------------------------")
            self.txt_result.append('\n')

    def initCompress(self):
        self.txt_result.append("start compression")

        self.compress = CompresProcess(
            self.fileName, self.th_xm, self.th_sm, self.optimize, self.weight_max, self.quality)
        self.compress.txt_result.connect(self.txt_result.append)
        self.compress.le_wi.connect(self.le_wi.setText)
        self.compress.le_wf.connect(self.le_wf.setText)
        self.compress.le_reduce.connect(self.le_reduce.setText)
        self.compress.le_state.connect(self.le_state.setText)
        self.compress.progressBar.connect(self.progressBar.setValue)

        self.compress.finished.connect(self.compressFinished)
        self.compress.start()

    def compressFinished(self):
        self.txt_result.append("Finished")
        del self.compress


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = VentanaPrincipal()
    main.show()
    sys.exit(app.exec_())
