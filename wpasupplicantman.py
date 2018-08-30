import sys
import os
from urllib.request import urlopen, URLError
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import pyqtSlot


def internet_on():
       try:
           urlopen('https://google.com', timeout=30)
           return True
       except URLError as err:
           return False
def showMessageBox(message):
	msg = QMessageBox()
	msg.setWindowTitle(' ')
	msg.setText(message)
	msg.exec_()
def askRestart(parent):
	if QMessageBox.question(parent, 'Alert', 'This needs a restart for changes to take effect, restart now?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
		os.system('reboot now')

if len(sys.argv) > 1:
     if internet_on() == True:
         sys.exit()
    

app = QApplication(sys.argv)
grid = QGridLayout()
window_width = 350
window_height = 300
w = QWidget()
w.setWindowTitle('No internet found! Add your wifi here!')
w.setGeometry(300, 300, window_width, window_height)
w.setLayout(grid)

add = QPushButton('ADD') 
ssid = QLabel('SSID:')
password = QLabel('PASSWORD:')
txt_ssid = QLineEdit()
txt_password = QLineEdit()

grid.addWidget(ssid, 0, 0)
grid.addWidget(txt_ssid, 0, 1)
grid.addWidget(password, 1, 0)
grid.addWidget(txt_password, 1, 1)
grid.addWidget(add, 2, 0, 1, 2)


@pyqtSlot()
def on_click():
	ssid_text = txt_ssid.text()
	password_text = txt_password.text()
	wpa_supplicant_conf = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'r+')
	str_to_find = 'ssid=\"'+ssid_text+'\"'
	for line in wpa_supplicant_conf:
		if str_to_find in line:
			wpa_supplicant_conf.seek(0, os.SEEK_SET)
			lines = wpa_supplicant_conf.readlines()
			wpa_supplicant_conf.close()
			
			new_file = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w')
			
			i = 0;
			
			while i < len(lines):
				new_file.write(lines[i])
				if str_to_find in lines[i]:
					new_file.write('   psk=\"'+password_text+'\"\n')
					i += 1
				i += 1
			new_file.close()
			showMessageBox("The password of " + ssid_text + " has been updated.")
			askRestart(w)
			break
	else:
		wpa_supplicant_conf.seek(0, os.SEEK_END)
		wpa_supplicant_conf.write('\n\nnetwork={\n   ssid=\"'+ssid_text+'\"\n   psk=\"'+password_text+'\"\n}')
		wpa_supplicant_conf.close()
		showMessageBox(ssid_text+" has been added successfully.")
		askRestart(w)
add.clicked.connect(on_click)



w.show()

sys.exit(app.exec_())

