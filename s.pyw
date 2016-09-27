# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/sms.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit
from SMS import SMS	
import ui.sms_bomb_rc
import sys

from smtplib import SMTP
from threading import Thread
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
		return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
		
except AttributeError:
    def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)


		
			
class Main:
	
	def __init__(self):
		app = QtGui.QApplication(sys.argv)
		
		self.view = View()
	
		# GUI
		self.view.pushButton.connect(self.view.pushButton, QtCore.SIGNAL("clicked()"), self.fork)
		
		
		
			
		self.view.show()
		
		sys.exit(app.exec_())
		

	def fork(self):
		thread = Thread(target = SMS, args = (self.view,)).start()
		
		
		
		
class View(QtGui.QFrame):
		

	def __init__(self):
		super(View, self).__init__()
		
		
		
		self.setObjectName(_fromUtf8("Frame"))
		self.setWindowModality(QtCore.Qt.ApplicationModal)
		self.resize(500, 290)
		self.setMinimumSize(QtCore.QSize(500, 290))
		self.setMaximumSize(QtCore.QSize(500, 290))
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/head/bomb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(icon)
		self.setToolTip(_fromUtf8(""))
		self.setStatusTip(_fromUtf8(""))
		self.setWhatsThis(_fromUtf8(""))
		self.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
		self.setFrameShape(QtGui.QFrame.StyledPanel)
		self.setFrameShadow(QtGui.QFrame.Raised)
		self.setLineWidth(0)
		
		self.header = QtWebKit.QWebView(self)
		self.header.setGeometry(QtCore.QRect(-9, 0, 515, 120))
		self.header.setMouseTracking(False)
		self.header.setToolTip(_fromUtf8(""))
		self.header.setStatusTip(_fromUtf8(""))
		self.header.setWhatsThis(_fromUtf8(""))
		self.header.setUrl(QtCore.QUrl(_fromUtf8("qrc:/head/head.html")))
		self.header.setZoomFactor(1.0)
		self.header.setObjectName(_fromUtf8("header"))
		
		self.Target = QtGui.QGroupBox(self)
		self.Target.setGeometry(QtCore.QRect(1, 120, 190, 160))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Times New Roman"))
		font.setPointSize(16)
		font.setBold(True)
		font.setUnderline(False)
		font.setWeight(75)
		self.Target.setFont(font)
		self.Target.setToolTip(_fromUtf8(""))
		self.Target.setStatusTip(_fromUtf8(""))
		self.Target.setWhatsThis(_fromUtf8(""))
		self.Target.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255); color: rgb(255, 0, 0);"))
		self.Target.setFlat(False)
		self.Target.setObjectName(_fromUtf8("Target"))
		
		self.phone_entry = QtGui.QLineEdit(self.Target)
		self.phone_entry.setGeometry(QtCore.QRect(103, 25, 83, 20))
		self.phone_entry.setAcceptDrops(False)
		self.phone_entry.setToolTip(_fromUtf8(""))
		self.phone_entry.setStatusTip(_fromUtf8(""))
		self.phone_entry.setWhatsThis(_fromUtf8(""))
		self.phone_entry.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
		self.phone_entry.setText(_fromUtf8(""))
		self.phone_entry.setFrame(False)
		self.phone_entry.setObjectName(_fromUtf8("phone_entry"))
		self.Phone_Number = QtGui.QLabel(self.Target)
		self.Phone_Number.setGeometry(QtCore.QRect(6, 27, 95, 16))
		self.Phone_Number.setObjectName(_fromUtf8("Phone_Number"))
		
		self.line = QtGui.QFrame(self.Target)
		self.line.setWindowModality(QtCore.Qt.WindowModal)
		self.line.setGeometry(QtCore.QRect(2, 46, 185, 11))
		self.line.setToolTip(_fromUtf8(""))
		self.line.setStatusTip(_fromUtf8(""))
		self.line.setWhatsThis(_fromUtf8(""))
		self.line.setFrameShadow(QtGui.QFrame.Raised)
		self.line.setLineWidth(2)
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setObjectName(_fromUtf8("line"))
		
		self.provider_label = QtGui.QLabel(self.Target)
		self.provider_label.setGeometry(QtCore.QRect(5, 61, 61, 16))
		self.provider_label.setObjectName(_fromUtf8("provider_label"))
		
		self.providers = QtGui.QComboBox(self.Target)
		self.providers.setGeometry(QtCore.QRect(103, 60, 83, 22))
		self.providers.setObjectName(_fromUtf8("providers"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(0, _fromUtf8("-"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(1, _fromUtf8("Alltel"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(2, _fromUtf8("AT&T"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(3, _fromUtf8("MetroPCS"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(4, _fromUtf8("Orange"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(5, _fromUtf8("Rogers"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(6, _fromUtf8("Sprint"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(7, _fromUtf8("T-Mobile"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(8, _fromUtf8("Telus"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(9, _fromUtf8("Verizon"))
		self.providers.addItem(_fromUtf8(""))
		self.providers.setItemText(10, _fromUtf8("Virgin Mobile"))
		
		self.line_2 = QtGui.QFrame(self.Target)
		self.line_2.setWindowModality(QtCore.Qt.WindowModal)
		self.line_2.setGeometry(QtCore.QRect(2, 83, 185, 11))
		self.line_2.setToolTip(_fromUtf8(""))
		self.line_2.setStatusTip(_fromUtf8(""))
		self.line_2.setWhatsThis(_fromUtf8(""))
		self.line_2.setFrameShadow(QtGui.QFrame.Raised)
		self.line_2.setLineWidth(2)
		self.line_2.setFrameShape(QtGui.QFrame.HLine)
		self.line_2.setObjectName(_fromUtf8("line_2"))
		
		self.message_to_send = QtGui.QLabel(self.Target)
		self.message_to_send.setGeometry(QtCore.QRect(2, 90, 186, 20))
		self.message_to_send.setToolTip(_fromUtf8(""))
		self.message_to_send.setWhatsThis(_fromUtf8(""))
		self.message_to_send.setTextFormat(QtCore.Qt.RichText)
		self.message_to_send.setObjectName(_fromUtf8("message_to_send"))
		
		self.txt = QtGui.QPlainTextEdit(self.Target)
		self.txt.setGeometry(QtCore.QRect(10, 115, 170, 40))
		self.txt.setToolTip(_fromUtf8(""))
		self.txt.setStatusTip(_fromUtf8(""))
		self.txt.setWhatsThis(_fromUtf8(""))
		self.txt.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 127); color: rgb(170, 255, 0);"))
		self.txt.setFrameShape(QtGui.QFrame.StyledPanel)
		self.txt.setFrameShadow(QtGui.QFrame.Raised)
		self.txt.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.txt.setObjectName(_fromUtf8("txt"))
		
		self.gmail = QtGui.QGroupBox(self)
		self.gmail.setGeometry(QtCore.QRect(308, 120, 190, 160))
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Times New Roman"))
		font.setPointSize(16)
		font.setBold(True)
		font.setUnderline(False)
		font.setWeight(75)
		self.gmail.setFont(font)
		self.gmail.setToolTip(_fromUtf8(""))
		self.gmail.setStatusTip(_fromUtf8(""))
		self.gmail.setWhatsThis(_fromUtf8(""))
		self.gmail.setStyleSheet(_fromUtf8("background-color: rgb(85, 0, 0); color: rgb(85, 170, 0);"))
		self.gmail.setFlat(False)
		self.gmail.setObjectName(_fromUtf8("gmail"))
		
		self.email_entry = QtGui.QLineEdit(self.gmail)
		self.email_entry.setGeometry(QtCore.QRect(4, 55, 182, 20))
		self.email_entry.setAcceptDrops(False)
		self.email_entry.setToolTip(_fromUtf8(""))
		self.email_entry.setStatusTip(_fromUtf8(""))
		self.email_entry.setWhatsThis(_fromUtf8(""))
		self.email_entry.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);"))
		self.email_entry.setText(_fromUtf8(""))
		self.email_entry.setFrame(False)
		self.email_entry.setObjectName(_fromUtf8("email_entry"))
		
		self.email = QtGui.QLabel(self.gmail)
		self.email.setGeometry(QtCore.QRect(4, 25, 179, 20))
		self.email.setToolTip(_fromUtf8(""))
		self.email.setWhatsThis(_fromUtf8(""))
		self.email.setTextFormat(QtCore.Qt.RichText)
		self.email.setObjectName(_fromUtf8("email"))
		
		self.line_3 = QtGui.QFrame(self.gmail)
		self.line_3.setWindowModality(QtCore.Qt.ApplicationModal)
		self.line_3.setGeometry(QtCore.QRect(2, 83, 185, 11))
		self.line_3.setToolTip(_fromUtf8(""))
		self.line_3.setStatusTip(_fromUtf8(""))
		self.line_3.setWhatsThis(_fromUtf8(""))
		self.line_3.setStyleSheet(_fromUtf8("color: rgb(2, 255, 82);"))
		self.line_3.setFrameShadow(QtGui.QFrame.Raised)
		self.line_3.setLineWidth(2)
		self.line_3.setMidLineWidth(2)
		self.line_3.setFrameShape(QtGui.QFrame.HLine)
		self.line_3.setObjectName(_fromUtf8("line_3"))
		
		self.password_entry = QtGui.QLineEdit(self.gmail)
		self.password_entry.setGeometry(QtCore.QRect(4, 120, 182, 20))
		self.password_entry.setAcceptDrops(False)
		self.password_entry.setToolTip(_fromUtf8(""))
		self.password_entry.setStatusTip(_fromUtf8(""))
		self.password_entry.setWhatsThis(_fromUtf8(""))
		self.password_entry.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);"))
		self.password_entry.setText(_fromUtf8(""))
		self.password_entry.setFrame(False)
		self.password_entry.setEchoMode(QtGui.QLineEdit.Password)
		self.password_entry.setObjectName(_fromUtf8("password_entry"))
		
		self.password = QtGui.QLabel(self.gmail)
		self.password.setGeometry(QtCore.QRect(2, 90, 186, 20))
		self.password.setToolTip(_fromUtf8(""))
		self.password.setWhatsThis(_fromUtf8(""))
		self.password.setTextFormat(QtCore.Qt.RichText)
		self.password.setObjectName(_fromUtf8("password"))
		
		self.email_entry.raise_()
		self.email.raise_()
		self.password_entry.raise_()
		self.password.raise_()
		self.line_3.raise_()
		
		self.pushButton = QtGui.QPushButton(self)
		self.pushButton.setGeometry(QtCore.QRect(200, 180, 100, 29))
		
		font = QtGui.QFont()
		font.setFamily(_fromUtf8("Times New Roman"))
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setWeight(9)
		
		self.pushButton.setFont(font)
		self.pushButton.setToolTip(_fromUtf8(""))
		self.pushButton.setStatusTip(_fromUtf8(""))
		self.pushButton.setWhatsThis(_fromUtf8(""))
		self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 0, 255); border-color: rgb(0, 255, 0); color: rgb(255, 255, 0); font: 75 14pt \"Times New Roman\";"))
		self.pushButton.setAutoExclusive(False)
		self.pushButton.setFlat(False)
		self.pushButton.setObjectName(_fromUtf8("pushButton"))
		
		self.set_delay = QtGui.QLabel(self)
		self.set_delay.setGeometry(QtCore.QRect(200, 120, 100, 30))
		self.set_delay.setObjectName(_fromUtf8("set_delay"))
		
		self.delay = QtGui.QSpinBox(self)
		self.delay.setGeometry(QtCore.QRect(200, 150, 50, 20))
		self.delay.setStyleSheet(_fromUtf8("color: rgb(255, 255, 0);"))
		self.delay.setSingleStep(1)
		self.delay.setObjectName(_fromUtf8("delay"))
		
		self.seconds = QtGui.QLabel(self)
		self.seconds.setGeometry(QtCore.QRect(255, 155, 40, 20))
		self.seconds.setObjectName(_fromUtf8("seconds"))
		
		self.Sent_Box = QtGui.QGroupBox(self)
		self.Sent_Box.setGeometry(QtCore.QRect(200, 220, 100, 60))
		self.Sent_Box.setToolTip(_fromUtf8(""))
		self.Sent_Box.setStatusTip(_fromUtf8(""))
		self.Sent_Box.setWhatsThis(_fromUtf8(""))
		self.Sent_Box.setStyleSheet(_fromUtf8("font-size:12pt; background-color: rgb(0, 0, 0); font-weight:600; color: rgb(255, 0, 0);"))
		self.Sent_Box.setFlat(False)
		self.Sent_Box.setCheckable(False)
		self.Sent_Box.setObjectName(_fromUtf8("Sent_Box"))
		
		self.Sent = QtGui.QLCDNumber(self.Sent_Box)
		self.Sent.setGeometry(QtCore.QRect(16, 20, 80, 37))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.Sent.setFont(font)
		self.Sent.setToolTip(_fromUtf8(""))
		self.Sent.setStatusTip(_fromUtf8(""))
		self.Sent.setWhatsThis(_fromUtf8(""))
		self.Sent.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.Sent.setStyleSheet(_fromUtf8("color: rgb(170, 0, 0);"))
		self.Sent.setFrameShape(QtGui.QFrame.NoFrame)
		self.Sent.setFrameShadow(QtGui.QFrame.Sunken)
		self.Sent.setLineWidth(0)
		self.Sent.setNumDigits(4)
		self.Sent.setDigitCount(4)
		self.Sent.setSegmentStyle(QtGui.QLCDNumber.Flat)
		self.Sent.setProperty("value", 0.0)
		self.Sent.setProperty("intValue", 0)
		self.Sent.setObjectName(_fromUtf8("Sent"))

		self.header.raise_()
		self.Target.raise_()
		self.gmail.raise_()
		self.set_delay.raise_()
		self.delay.raise_()
		self.seconds.raise_()
		self.pushButton.raise_()
		self.Sent_Box.raise_()

		QtCore.QMetaObject.connectSlotsByName(self)

		self.setWindowTitle(_translate("Frame", "SMS Bomb - NolenFelten.com", None))
		self.Target.setTitle(_translate("Frame", "Target:", None))
		self.phone_entry.setPlaceholderText(_translate("Frame", "7071234567", None))
		self.Phone_Number.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#aa0000;\">Phone Number:</span></p></body></html>", None))
		self.provider_label.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#aa0000;\">Provider:</span></p></body></html>", None))
		self.message_to_send.setText(_translate("Frame", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#aa0000;\"><center>Message To Send:</center></span></p></body></html>", None))
		self.txt.setPlainText(_translate("Frame", "SMS Bomb!", None))
		self.gmail.setTitle(_translate("Frame", "Gmail:", None))
		self.email_entry.setPlaceholderText(_translate("Frame", "Email@gmail.com", None))
		self.email.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#55aa00;\">Email Address:</span></p></body></html>", None))
		self.password_entry.setPlaceholderText(_translate("Frame", "Password", None))
		self.password.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#55aa00;\">Password:</span></p></body></html>", None))
		self.pushButton.setText(_translate("Frame", "START", None))
		self.set_delay.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#55557f;\">Set Delay:</span></p></body></html>", None))
		self.seconds.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#55557f;\">Seconds</span></p></body></html>", None))
		self.Sent_Box.setTitle(_translate("Frame", "Sent:", None))
		
		


Main()