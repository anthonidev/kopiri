# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Anthoni\Desktop\AuToPy\desing.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(659, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(99, 99, 99);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top = QtWidgets.QFrame(self.frame)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_top.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"font: 8pt \"Cascadia Code\";")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_top)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lb_title = QtWidgets.QLabel(self.frame_top)
        self.lb_title.setStyleSheet("color: rgb(188, 133, 252);")
        self.lb_title.setObjectName("lb_title")
        self.verticalLayout_8.addWidget(self.lb_title)
        self.label = QtWidgets.QLabel(self.frame_top)
        self.label.setStyleSheet("color: rgb(0, 170, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_top)
        self.frame_body = QtWidgets.QFrame(self.frame)
        self.frame_body.setStyleSheet("background-color: rgb(32, 32, 32);")
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_body)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_body)
        self.frame_2.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_2.setStyleSheet("QCheckBox{\n"
"    color: rgb(2, 218, 197);\n"
"    font: 10pt \"Cascadia Code\";\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(170, 85, 255);\n"
"    font: 11pt \"Cascadia Code\";\n"
"    border-bottom: 2px solid  rgb(170, 85, 255);\n"
"     \n"
"}\n"
"\n"
"QPushButton{\n"
"    color: rgb(9,9,9);\n"
"    font: 12pt \"Cascadia Code\";\n"
"     padding: 8px;\n"
"    background-color:rgb(170, 85, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_3.setStyleSheet("\n"
"\n"
"QSlider {\n"
"    border: 1px solid;\n"
"    height: 12px;\n"
"  \n"
"    }\n"
"\n"
"QFrame{\n"
"padding:5px  ;\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"border-radius: 0;\n"
"color:white;\n"
"border-bottom:1px solid white;\n"
"margin-bottom:5px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #565a5e;\n"
"    height: 10px;\n"
"    background: #eee;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(2, 218, 197);\n"
"    border: 1px solid #565a5e;\n"
"    width: 24px;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lb_create_th = QtWidgets.QLabel(self.frame_3)
        self.lb_create_th.setObjectName("lb_create_th")
        self.verticalLayout_5.addWidget(self.lb_create_th)
        self.cb_th_sm = QtWidgets.QCheckBox(self.frame_3)
        self.cb_th_sm.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.cb_th_sm.setChecked(True)
        self.cb_th_sm.setObjectName("cb_th_sm")
        self.verticalLayout_5.addWidget(self.cb_th_sm)
        self.cb_th_xm = QtWidgets.QCheckBox(self.frame_3)
        self.cb_th_xm.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.cb_th_xm.setChecked(True)
        self.cb_th_xm.setObjectName("cb_th_xm")
        self.verticalLayout_5.addWidget(self.cb_th_xm)
        self.lb_quality = QtWidgets.QLabel(self.frame_3)
        self.lb_quality.setObjectName("lb_quality")
        self.verticalLayout_5.addWidget(self.lb_quality)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setStyleSheet("QLabel{\n"
"border:none;\n"
"    color: rgb(2, 218, 197);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sd_quality = QtWidgets.QSlider(self.frame_8)
        self.sd_quality.setStyleSheet("")
        self.sd_quality.setMinimum(1)
        self.sd_quality.setMaximum(100)
        self.sd_quality.setProperty("value", 60)
        self.sd_quality.setOrientation(QtCore.Qt.Horizontal)
        self.sd_quality.setObjectName("sd_quality")
        self.horizontalLayout_5.addWidget(self.sd_quality)
        self.lb_quality_sd = QtWidgets.QLabel(self.frame_8)
        self.lb_quality_sd.setStyleSheet("QLabel{\n"
"border:none;\n"
"    color: rgb(2, 218, 197);\n"
"font: 8pt;\n"
"margin:0;\n"
"padding:0;\n"
"}\n"
"\n"
"")
        self.lb_quality_sd.setObjectName("lb_quality_sd")
        self.horizontalLayout_5.addWidget(self.lb_quality_sd)
        self.horizontalLayout_5.setStretch(0, 9)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.cb_optimize = QtWidgets.QCheckBox(self.frame_3)
        self.cb_optimize.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.cb_optimize.setChecked(True)
        self.cb_optimize.setObjectName("cb_optimize")
        self.verticalLayout_5.addWidget(self.cb_optimize)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sd_weight = QtWidgets.QSlider(self.frame_7)
        self.sd_weight.setMinimum(100000)
        self.sd_weight.setMaximum(450000)
        self.sd_weight.setProperty("value", 300000)
        self.sd_weight.setOrientation(QtCore.Qt.Horizontal)
        self.sd_weight.setObjectName("sd_weight")
        self.horizontalLayout_4.addWidget(self.sd_weight)
        self.lb_weight = QtWidgets.QLabel(self.frame_7)
        self.lb_weight.setStyleSheet("QLabel{\n"
"border:none;\n"
"    color: rgb(2, 218, 197);\n"
"font: 8pt;\n"
"margin:0;\n"
"padding:0;\n"
"}\n"
"\n"
"")
        self.lb_weight.setObjectName("lb_weight")
        self.horizontalLayout_4.addWidget(self.lb_weight)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("QFrame{\n"
"    margin:4px;\n"
"    background-color: rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:white;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.selectFileButton = QtWidgets.QPushButton(self.frame_4)
        self.selectFileButton.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.selectFileButton.setFont(font)
        self.selectFileButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Cascadia Code\";\n"
"background-color: rgb(144, 144, 144);\n"
"border: 2px solid   rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Anthoni\\Desktop\\AuToPy\\static/svg/filesadd.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectFileButton.setIcon(icon)
        self.selectFileButton.setIconSize(QtCore.QSize(25, 25))
        self.selectFileButton.setObjectName("selectFileButton")
        self.verticalLayout_6.addWidget(self.selectFileButton)
        self.bt_submit = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bt_submit.setFont(font)
        self.bt_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(144, 144, 144);\n"
"border: 2px solid   rgb(255, 255, 255);\n"
"margin:12px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Anthoni\\Desktop\\AuToPy\\static/svg/svgviewer-output.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_submit.setIcon(icon1)
        self.bt_submit.setIconSize(QtCore.QSize(16, 16))
        self.bt_submit.setObjectName("bt_submit")
        self.verticalLayout_6.addWidget(self.bt_submit)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_4.setStretch(0, 4)
        self.verticalLayout_4.setStretch(1, 2)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_9 = QtWidgets.QFrame(self.frame_body)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.txt_result = QtWidgets.QTextEdit(self.frame_9)
        self.txt_result.setMinimumSize(QtCore.QSize(340, 0))
        self.txt_result.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txt_result.setStyleSheet("\n"
"padding:5px;\n"
"border:2px solid  rgb(85, 85, 85);\n"
"border-radius: 5px;\n"
"color: rgb(1, 127, 114);")
        self.txt_result.setReadOnly(True)
        self.txt_result.setObjectName("txt_result")
        self.verticalLayout_7.addWidget(self.txt_result)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setStyleSheet("QLineEdit{\n"
"    border:0 0 0 0;\n"
"color: rgb(0, 170, 127);\n"
"font:18px;\n"
"}\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lb_state = QtWidgets.QLabel(self.frame_10)
        self.lb_state.setStyleSheet("color: rgb(188, 133, 252);\n"
"font:14px")
        self.lb_state.setObjectName("lb_state")
        self.horizontalLayout_6.addWidget(self.lb_state)
        self.le_state = QtWidgets.QLineEdit(self.frame_10)
        self.le_state.setObjectName("le_state")
        self.horizontalLayout_6.addWidget(self.le_state)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.addWidget(self.frame_body)
        self.frame_bot = QtWidgets.QFrame(self.frame)
        self.frame_bot.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"font: 8pt \"Cascadia Code\";")
        self.frame_bot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bot.setObjectName("frame_bot")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_bot)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_bot)
        self.frame_6.setStyleSheet("QPushButton{\n"
"    color: rgb(9,9,9);\n"
"    font: 8pt \"Cascadia Code\";\n"
"     padding: 8px;\n"
"\n"
"    border-radius: 5px;\n"
"    background-color: rgb(208, 102, 124);\n"
"\n"
"}\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_11 = QtWidgets.QFrame(self.frame_6)
        self.frame_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_11.setStyleSheet("QProgressBar\n"
"{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: #74c8ff;\n"
"    border-radius: 7px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    \n"
"    background-color: rgb(2, 218, 197);\n"
"}\n"
"\n"
"QFrame{\n"
"padding:5px  ;\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius: 5px;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.progressBar = QtWidgets.QProgressBar(self.frame_11)
        self.progressBar.setMinimumSize(QtCore.QSize(300, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_9.addWidget(self.progressBar)
        self.bt_clear = QtWidgets.QPushButton(self.frame_11)
        self.bt_clear.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bt_clear.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Anthoni\\Desktop\\AuToPy\\static/svg/clear.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_clear.setIcon(icon2)
        self.bt_clear.setDefault(False)
        self.bt_clear.setObjectName("bt_clear")
        self.verticalLayout_9.addWidget(self.bt_clear)
        self.verticalLayout_9.setStretch(0, 3)
        self.verticalLayout_9.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.frame_11)
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_5.setStyleSheet("QFrame{\n"
"padding:5px  ;\n"
"background-color: rgb(45, 45, 45);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font:10px;\n"
"    border:0 0 0 0\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border:0 0 0 0;\n"
"    color: rgb(0, 170, 127);\n"
"    font:15px;\n"
"background-color: rgb(45, 45, 45);\n"
"    color: rgb(208, 102, 124);\n"
"} \n"
"\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lb_wi = QtWidgets.QLabel(self.frame_5)
        self.lb_wi.setStyleSheet("")
        self.lb_wi.setObjectName("lb_wi")
        self.verticalLayout_3.addWidget(self.lb_wi)
        self.le_wi = QtWidgets.QLineEdit(self.frame_5)
        self.le_wi.setStyleSheet("")
        self.le_wi.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_wi.setObjectName("le_wi")
        self.verticalLayout_3.addWidget(self.le_wi)
        self.lb_wf = QtWidgets.QLabel(self.frame_5)
        self.lb_wf.setObjectName("lb_wf")
        self.verticalLayout_3.addWidget(self.lb_wf)
        self.le_wf = QtWidgets.QLineEdit(self.frame_5)
        self.le_wf.setStyleSheet("")
        self.le_wf.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_wf.setObjectName("le_wf")
        self.verticalLayout_3.addWidget(self.le_wf)
        self.lb_reduce = QtWidgets.QLabel(self.frame_5)
        self.lb_reduce.setObjectName("lb_reduce")
        self.verticalLayout_3.addWidget(self.lb_reduce)
        self.le_reduce = QtWidgets.QLineEdit(self.frame_5)
        self.le_reduce.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_reduce.setObjectName("le_reduce")
        self.verticalLayout_3.addWidget(self.le_reduce)
        self.horizontalLayout.addWidget(self.frame_5)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout_3.setStretch(0, 4)
        self.verticalLayout_2.addWidget(self.frame_bot)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">KOPIRI</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Convert JPG to WEPB for yout site web.</p></body></html>"))
        self.lb_create_th.setText(_translate("MainWindow", "Create Thumbnail"))
        self.cb_th_sm.setText(_translate("MainWindow", "Small"))
        self.cb_th_xm.setText(_translate("MainWindow", "Extra Small"))
        self.lb_quality.setText(_translate("MainWindow", "Quality"))
        self.lb_quality_sd.setText(_translate("MainWindow", "60"))
        self.cb_optimize.setText(_translate("MainWindow", "Optimize"))
        self.label_7.setText(_translate("MainWindow", "weight max"))
        self.lb_weight.setText(_translate("MainWindow", "300 KB"))
        self.selectFileButton.setText(_translate("MainWindow", "Select Image or Images"))
        self.bt_submit.setText(_translate("MainWindow", "Comprimir"))
        self.txt_result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&gt;&gt; CREATE FOR ANTHONI PORTOCARRERO -&gt; </span><a href=\"https://github.com/anthonidev/kopiri\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">Git Hub</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">............................................................................</p></body></html>"))
        self.lb_state.setText(_translate("MainWindow", "STATE:"))
        self.le_state.setText(_translate("MainWindow", "------"))
        self.bt_clear.setText(_translate("MainWindow", "Clear"))
        self.lb_wi.setText(_translate("MainWindow", "Weight Initial:"))
        self.le_wi.setText(_translate("MainWindow", "--"))
        self.lb_wf.setText(_translate("MainWindow", "Weight Final:"))
        self.le_wf.setText(_translate("MainWindow", "--"))
        self.lb_reduce.setText(_translate("MainWindow", "Reduce in:"))
        self.le_reduce.setText(_translate("MainWindow", "--"))
