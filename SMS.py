from PyQt4 import QtCore, QtGui

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


class SMS(Thread):
	
	def __init__(self, view):
		Thread.__init__(self)
		self.daemon = True
		
		view.pushButton.setText(_translate("Frame", "Initializing :D", None))
		
		self.text = {
			"email": str(view.email_entry.text()),
			"password": str(view.password_entry.text()),
			"delay": int(view.delay.value()),
			"target": str(view.phone_entry.text()),
			"message": str(view.txt.toPlainText()),
			"provider": str(view.providers.currentText()),
			"pushButton": view.pushButton,
			"lcd": view.Sent
		}
		
		self.start()
	
	
	def run(self):
		
		self.text["pushButton"].setText(_translate("Frame", "Connecting", None))

		server = SMTP("smtp.gmail.com:587")

		self.text["pushButton"].setText(_translate("Frame", "Securing", None))
		
		server.starttls()

		self.text["pushButton"].setText(_translate("Frame", "Logging In", None))
		
		try:
			server.login(self.text["email"], self.text["password"])
			
			self.text["pushButton"].setText(_translate("Frame", "^_^ Success ^_^", None))			
				
			if self.text["provider"] == "Alltel":
				carrier_attack = "@alltelmessage.com"

			if self.text["provider"] == "AT&T":
				carrier_attack = "@txt.att.net"

			if self.text["provider"] == "Rogers":
				carrier_attack = "@pcs.rogers.com"

			if self.text["provider"] == "Sprint":
				carrier_attack = "@messaging.sprintpcs.com"

			if self.text["provider"] == "T-Mobile":
				carrier_attack = "@tmomail.net"

			if self.text["provider"] == "Telus":
				carrier_attack = "@msg.telus.com"

			if self.text["provider"] == "Verizon":
				carrier_attack = "@vtext.com"

			if self.text["provider"] == "Virgin Mobile":
				carrier_attack = "@vmobl.com"

			if self.text["provider"] == "Orange":
				carrier_attack = "@sms.orange.pl"

			if self.text["provider"] == "MetroPCS":
				carrier_attack = "@mymetropcs.com"
				
				
			self.text["target"] = self.text["target"] + carrier_attack
				
				
		except SMTPAuthenticationError:
			self.text["pushButton"].setText(_translate("Frame", "Log in Failed", None))
			
		
		self.text["message"] = """\
From: %s
To: %s
Subject: %s
%s
""" % ("bob@bob.com", self.text["target"], "", self.text["message"])
		
		count = 0
		while count != 1999:
						
			self.text["pushButton"].setText(_translate("Frame", "Sending...", None))
			
			server.sendmail(self.text["email"], self.text["target"], self.text["message"])
			
			self.text["pushButton"].setText(_translate("Frame", "Sent", None))
			
			count += 1
			
			self.text["lcd"].display(count)
			
			for x in range(self.text["delay"]):
				self.text["pushButton"].setText(_translate("Frame", "Sleep " + str(self.text["delay"] - x) + "s", None))
				time.sleep(1)