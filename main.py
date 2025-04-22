# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_test_ui2tYVIEk.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import traceback
from ast import Not
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import sys
from paramiko import SSHClient
from time import sleep
import difflib

cipher_auto = "auto"
cipher_ccmp = "Force CCMP (AES) (Recommended)"
cipher_tkip_aes = "Force TKIP and AES (compatiblity)"
cipher_tkip = "Force TKIP (only for very old devices)"
ciphers = [cipher_auto, cipher_ccmp, cipher_tkip_aes, cipher_tkip]

enc_wpa3 = "WPA3-SAE (best security)"
enc_wpa2_3 = "WPA2-PSK/WPA3-SAE Mixed Mode (strong security)"
enc_wpa2 = "WPA2-PSK (strong security)"
enc_wpa1_2 = "WPA-PSK/WPA2-PSK Mixed Mode (medium security)"
enc_wpa1 = "WPA-PSK (weak security)"
enc_owe = "OWE (open network)"
enc_open = "No Encryption (open network)"
encryption = [enc_wpa3, enc_wpa2_3, enc_wpa2, enc_wpa1_2, enc_wpa1, enc_owe, enc_open]

ip_addr = ""
usern = ""
passwd = ""
wifi2 = False
wifi5 = False
wifi6 = False

country_code = None

countries = ["HU", "DE", "FR"]


# Connect
client = SSHClient()
client.load_system_host_keys()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1299, 544)
        self.mainwidget = QWidget(MainWindow)
        self.mainwidget.setObjectName(u"mainwidget")
        self.verticalLayoutWidget = QWidget(self.mainwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1579, 416))
        self.mainLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.router_form = QFormLayout()
        self.router_form.setObjectName(u"router_form")
        self.admin_usr_label = QLabel(self.verticalLayoutWidget)
        self.admin_usr_label.setObjectName(u"admin_usr_label")

        self.router_form.setWidget(0, QFormLayout.LabelRole, self.admin_usr_label)

        self.admin_usr_line = QLineEdit(self.verticalLayoutWidget)
        self.admin_usr_line.setObjectName(u"admin_usr_line")

        self.router_form.setWidget(0, QFormLayout.FieldRole, self.admin_usr_line)

        self.admin_pwd_label = QLabel(self.verticalLayoutWidget)
        self.admin_pwd_label.setObjectName(u"admin_pwd_label")

        self.router_form.setWidget(1, QFormLayout.LabelRole, self.admin_pwd_label)

        self.admin_pwd_line = QLineEdit(self.verticalLayoutWidget)
        self.admin_pwd_line.setObjectName(u"admin_pwd_line")
        self.admin_pwd_line.setEchoMode(QLineEdit.Password)

        self.router_form.setWidget(1, QFormLayout.FieldRole, self.admin_pwd_line)

        self.ip_addr_label = QLabel(self.verticalLayoutWidget)
        self.ip_addr_label.setObjectName(u"ip_addr_label")

        self.router_form.setWidget(3, QFormLayout.LabelRole, self.ip_addr_label)

        self.ip_addr_line = QLineEdit(self.verticalLayoutWidget)
        self.ip_addr_line.setObjectName(u"ip_addr_line")

        self.router_form.setWidget(3, QFormLayout.FieldRole, self.ip_addr_line)

        self.ssh_button = QPushButton(self.verticalLayoutWidget)
        self.ssh_button.setObjectName(u"ssh_button")

        self.ssh_button.clicked.connect(self.Establish_Connection)

        self.router_form.setWidget(4, QFormLayout.LabelRole, self.ssh_button)

        self.ssh_button_label = QLabel(self.verticalLayoutWidget)
        self.ssh_button_label.setObjectName(u"ssh_button_label")

        self.router_form.setWidget(4, QFormLayout.FieldRole, self.ssh_button_label)

        self.country_label = QLabel(self.verticalLayoutWidget)
        self.country_label.setObjectName(u"country_label")
        self.country_label.setEnabled(False)

        self.router_form.setWidget(5, QFormLayout.LabelRole, self.country_label)

        self.country_combobox = QComboBox(self.verticalLayoutWidget)
        self.country_combobox.setObjectName(u"country_combobox")
        self.country_combobox.setEnabled(False)
        for _ in countries:
            self.country_combobox.addItem("")

        self.router_form.setWidget(5, QFormLayout.FieldRole, self.country_combobox)


        self.mainLayout.addLayout(self.router_form)

        self.wifi_horizontal_layout = QHBoxLayout()
        self.wifi_horizontal_layout.setObjectName(u"wifi_horizontal_layout")
        self.wifi_2_widget = QWidget(self.verticalLayoutWidget)
        self.wifi_2_widget.setObjectName(u"wifi_2_widget")
        self.wifi_24_form = QFormLayout(self.wifi_2_widget)
        self.wifi_24_form.setObjectName(u"wifi_24_form")
        self.wifi_2z_checkbox = QCheckBox(self.wifi_2_widget)
        self.wifi_2z_checkbox.setObjectName(u"wifi_2z_checkbox")
        self.wifi_2_widget.setVisible(False)

        self.wifi_24_form.setWidget(0, QFormLayout.LabelRole, self.wifi_2z_checkbox)

        self.wifi_2_ssid_label = QLabel(self.wifi_2_widget)
        self.wifi_2_ssid_label.setObjectName(u"wifi_2_ssid_label")

        self.wifi_24_form.setWidget(1, QFormLayout.LabelRole, self.wifi_2_ssid_label)

        self.wifi_2_ssid_line = QLineEdit(self.wifi_2_widget)
        self.wifi_2_ssid_line.setObjectName(u"wifi_2_ssid_line")

        self.wifi_24_form.setWidget(1, QFormLayout.FieldRole, self.wifi_2_ssid_line)

        self.wifi_2_pwd_label = QLabel(self.wifi_2_widget)
        self.wifi_2_pwd_label.setObjectName(u"wifi_2_pwd_label")

        self.wifi_24_form.setWidget(2, QFormLayout.LabelRole, self.wifi_2_pwd_label)

        self.wifi_2_pwd_line = QLineEdit(self.wifi_2_widget)
        self.wifi_2_pwd_line.setObjectName(u"wifi_2_pwd_line")
        self.wifi_2_pwd_line.setEchoMode(QLineEdit.Password)

        self.wifi_24_form.setWidget(2, QFormLayout.FieldRole, self.wifi_2_pwd_line)

        self.wifi_24_encryption_label = QLabel(self.wifi_2_widget)
        self.wifi_24_encryption_label.setObjectName(u"wifi_24_encryption_label")

        self.wifi_24_form.setWidget(3, QFormLayout.LabelRole, self.wifi_24_encryption_label)

        self.wifi_24_encryption_combobox = QComboBox(self.wifi_2_widget)
        for _ in encryption:
            self.wifi_24_encryption_combobox.addItem("")
        self.wifi_24_encryption_combobox.setObjectName(u"wifi_24_encryption_combobox")

        self.wifi_24_form.setWidget(3, QFormLayout.FieldRole, self.wifi_24_encryption_combobox)

        self.wifi_2_cipher_label = QLabel(self.wifi_2_widget)
        self.wifi_2_cipher_label.setObjectName(u"wifi_2_cipher_label")
        self.wifi_2_cipher_label.setEnabled(False)

        self.wifi_24_form.setWidget(4, QFormLayout.LabelRole, self.wifi_2_cipher_label)

        self.wifi_2_cipher_combobox = QComboBox(self.wifi_2_widget)
        for _ in ciphers:
            self.wifi_2_cipher_combobox.addItem("")
        self.wifi_2_cipher_combobox.setObjectName(u"wifi_2_cipher_combobox")
        self.wifi_2_cipher_combobox.setEnabled(False)

        self.wifi_24_form.setWidget(4, QFormLayout.FieldRole, self.wifi_2_cipher_combobox)


        self.wifi_horizontal_layout.addWidget(self.wifi_2_widget)

        self.wifi_5_widget = QWidget(self.verticalLayoutWidget)
        self.wifi_5_widget.setObjectName(u"wifi_5_widget")
        self.wifi_5_form = QFormLayout(self.wifi_5_widget)
        self.wifi_5_form.setObjectName(u"wifi_5_form")
        self.wifi_5_checkbox = QCheckBox(self.wifi_5_widget)
        self.wifi_5_checkbox.setObjectName(u"wifi_5_checkbox")
        self.wifi_5_checkbox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.wifi_5_widget.setVisible(False)

        self.wifi_5_form.setWidget(0, QFormLayout.LabelRole, self.wifi_5_checkbox)

        self.wifi_5_ssid_label = QLabel(self.wifi_5_widget)
        self.wifi_5_ssid_label.setObjectName(u"wifi_5_ssid_label")

        self.wifi_5_form.setWidget(1, QFormLayout.LabelRole, self.wifi_5_ssid_label)

        self.wifi_5_ssid_line = QLineEdit(self.wifi_5_widget)
        self.wifi_5_ssid_line.setObjectName(u"wifi_5_ssid_line")

        self.wifi_5_form.setWidget(1, QFormLayout.FieldRole, self.wifi_5_ssid_line)

        self.wifi_5_pwd_label = QLabel(self.wifi_5_widget)
        self.wifi_5_pwd_label.setObjectName(u"wifi_5_pwd_label")

        self.wifi_5_form.setWidget(2, QFormLayout.LabelRole, self.wifi_5_pwd_label)

        self.wifi_5_pwd_line = QLineEdit(self.wifi_5_widget)
        self.wifi_5_pwd_line.setObjectName(u"wifi_5_pwd_line")
        self.wifi_5_pwd_line.setEchoMode(QLineEdit.Password)

        self.wifi_5_form.setWidget(2, QFormLayout.FieldRole, self.wifi_5_pwd_line)

        self.wifi_5_encryption_label = QLabel(self.wifi_5_widget)
        self.wifi_5_encryption_label.setObjectName(u"wifi_5_encryption_label")

        self.wifi_5_form.setWidget(3, QFormLayout.LabelRole, self.wifi_5_encryption_label)

        self.wifi_5_encryption_combobox = QComboBox(self.wifi_5_widget)
        for _ in encryption:
            self.wifi_5_encryption_combobox.addItem("")
        self.wifi_5_encryption_combobox.setObjectName(u"wifi_5_encryption_combobox")

        self.wifi_5_form.setWidget(3, QFormLayout.FieldRole, self.wifi_5_encryption_combobox)

        self.wifi_5_cipher_label = QLabel(self.wifi_5_widget)
        self.wifi_5_cipher_label.setObjectName(u"wifi_5_cipher_label")
        self.wifi_5_cipher_label.setEnabled(False)

        self.wifi_5_form.setWidget(4, QFormLayout.LabelRole, self.wifi_5_cipher_label)

        self.wifi_5_cipher_combobox = QComboBox(self.wifi_5_widget)
        for _ in ciphers:
            self.wifi_5_cipher_combobox.addItem("")
        self.wifi_5_cipher_combobox.setObjectName(u"wifi_5_cipher_combobox")
        self.wifi_5_cipher_combobox.setEnabled(False)

        self.wifi_5_form.setWidget(4, QFormLayout.FieldRole, self.wifi_5_cipher_combobox)


        self.wifi_horizontal_layout.addWidget(self.wifi_5_widget)

        self.wifi_6_widget = QWidget(self.verticalLayoutWidget)
        self.wifi_6_widget.setObjectName(u"wifi_6_widget")
        self.wifi_6_form = QFormLayout(self.wifi_6_widget)
        self.wifi_6_form.setObjectName(u"wifi_6_form")
        self.wifi_6_checkbox = QCheckBox(self.wifi_6_widget)
        self.wifi_6_checkbox.setObjectName(u"wifi_6_checkbox")
        self.wifi_6_widget.setVisible(False)

        self.wifi_6_form.setWidget(0, QFormLayout.LabelRole, self.wifi_6_checkbox)

        self.wifi_6_ssid_label = QLabel(self.wifi_6_widget)
        self.wifi_6_ssid_label.setObjectName(u"wifi_6_ssid_label")

        self.wifi_6_form.setWidget(1, QFormLayout.LabelRole, self.wifi_6_ssid_label)

        self.wifi_6_ssid_line = QLineEdit(self.wifi_6_widget)
        self.wifi_6_ssid_line.setObjectName(u"wifi_6_ssid_line")

        self.wifi_6_form.setWidget(1, QFormLayout.FieldRole, self.wifi_6_ssid_line)

        self.wifi_6_pwd_label = QLabel(self.wifi_6_widget)
        self.wifi_6_pwd_label.setObjectName(u"wifi_6_pwd_label")

        self.wifi_6_form.setWidget(2, QFormLayout.LabelRole, self.wifi_6_pwd_label)

        self.wifi_6_pwd_line = QLineEdit(self.wifi_6_widget)
        self.wifi_6_pwd_line.setObjectName(u"wifi_6_pwd_line")
        self.wifi_6_pwd_line.setEchoMode(QLineEdit.Password)

        self.wifi_6_form.setWidget(2, QFormLayout.FieldRole, self.wifi_6_pwd_line)

        self.wifi_6_encryption_label = QLabel(self.wifi_6_widget)
        self.wifi_6_encryption_label.setObjectName(u"wifi_6_encryption_label")

        self.wifi_6_form.setWidget(3, QFormLayout.LabelRole, self.wifi_6_encryption_label)

        self.wifi_6_encryption_combobox = QComboBox(self.wifi_6_widget)
        for _ in encryption:
            self.wifi_6_encryption_combobox.addItem("")
        self.wifi_6_encryption_combobox.setObjectName(u"wifi_6_encryption_combobox")

        self.wifi_6_form.setWidget(3, QFormLayout.FieldRole, self.wifi_6_encryption_combobox)

        self.wifi_6_cipher_label = QLabel(self.wifi_6_widget)
        self.wifi_6_cipher_label.setObjectName(u"wifi_6_cipher_label")
        self.wifi_6_cipher_label.setEnabled(False)

        self.wifi_6_form.setWidget(4, QFormLayout.LabelRole, self.wifi_6_cipher_label)

        self.wifi_6_cipher_combobox = QComboBox(self.wifi_6_widget)
        for _ in ciphers:
            self.wifi_6_cipher_combobox.addItem("")
        self.wifi_6_cipher_combobox.setObjectName(u"wifi_6_cipher_combobox")
        self.wifi_6_cipher_combobox.setEnabled(False)

        self.wifi_6_form.setWidget(4, QFormLayout.FieldRole, self.wifi_6_cipher_combobox)


        self.wifi_horizontal_layout.addWidget(self.wifi_6_widget)

        self.commit_changes_button = QPushButton(self.verticalLayoutWidget)
        self.commit_changes_button.setObjectName(u"commit_changes_button")
        self.commit_changes_button.clicked.connect(self.CommitChanges)

        self.wifi_horizontal_layout.addWidget(self.commit_changes_button)


        self.mainLayout.addLayout(self.wifi_horizontal_layout)

        MainWindow.setCentralWidget(self.mainwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1299, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.admin_usr_label.setText(QCoreApplication.translate("MainWindow", u"Router admin username:", None))
        self.admin_usr_line.setText(QCoreApplication.translate("MainWindow", u"root", None))
        self.admin_pwd_label.setText(QCoreApplication.translate("MainWindow", u"Router admin password:", None))
        self.admin_pwd_line.setText("")
        self.ip_addr_label.setText(QCoreApplication.translate("MainWindow", u"OpenWRT IP:", None))
        self.ip_addr_line.setText(QCoreApplication.translate("MainWindow", u"192.168.1.1", None))
        self.ssh_button.setText(QCoreApplication.translate("MainWindow", u"SSH Test", None))
        self.ssh_button_label.setText("")
        self.country_label.setText(QCoreApplication.translate("MainWindow", u"Country:", None))
        self.wifi_2z_checkbox.setText(QCoreApplication.translate("MainWindow", u"2.4GHz", None))
        self.wifi_2_ssid_label.setText(QCoreApplication.translate("MainWindow", u"Wi-Fi SSID:", None))
        self.wifi_2_ssid_line.setText("")
        self.wifi_2_pwd_label.setText(QCoreApplication.translate("MainWindow", u"Wi-Fi Password:", None))
        self.wifi_2_pwd_line.setText("")
        self.wifi_24_encryption_label.setText(QCoreApplication.translate("MainWindow", u"Encryption method:", None))

        for i, country in enumerate(countries):
            self.country_combobox.setItemText(i, QCoreApplication.translate("MainWindow", u"" + country, None))

        for i, enc in enumerate(encryption):
            self.wifi_24_encryption_combobox.setItemText(i, QCoreApplication.translate("MainWindow", u"" + enc, None))
            self.wifi_5_encryption_combobox.setItemText(i, QCoreApplication.translate("MainWindow", u"" + enc, None))
            self.wifi_6_encryption_combobox.setItemText(i, QCoreApplication.translate("MainWindow", u"" + enc, None))

        self.wifi_24_encryption_combobox.currentIndexChanged.connect(self.onChanged2GHz)
        self.wifi_5_encryption_combobox.currentIndexChanged.connect(self.onChanged5GHz)
        self.wifi_6_encryption_combobox.currentIndexChanged.connect(self.onChanged6GHz)

        self.wifi_2_cipher_label.setText(QCoreApplication.translate("MainWindow", u"Cipher: ", None))
        for i, cipher in enumerate(ciphers):
            self.wifi_2_cipher_combobox.setItemText(i, QCoreApplication.translate("MainWindow", u"" + cipher, None))
            self.wifi_5_cipher_combobox.setItemText(i, QCoreApplication.translate("MainWindow", u"" + cipher, None))
            self.wifi_6_cipher_combobox.setItemText(i, QCoreApplication.translate("MainWindow", u"" + cipher, None))

        self.wifi_5_checkbox.setText(QCoreApplication.translate("MainWindow", u"5GHz", None))
        self.wifi_5_ssid_label.setText(QCoreApplication.translate("MainWindow", u"Wi-Fi SSID:", None))
        self.wifi_5_pwd_label.setText(QCoreApplication.translate("MainWindow", u"Wi-Fi Password:", None))
        self.wifi_5_encryption_label.setText(QCoreApplication.translate("MainWindow", u"Encryption method:", None))

        self.wifi_5_cipher_label.setText(QCoreApplication.translate("MainWindow", u"Cipher:", None))

        self.wifi_6_checkbox.setText(QCoreApplication.translate("MainWindow", u"6GHz", None))
        self.wifi_6_ssid_label.setText(QCoreApplication.translate("MainWindow", u"Wi-Fi SSID:", None))
        self.wifi_6_pwd_label.setText(QCoreApplication.translate("MainWindow", u"Wi-Fi Password:", None))
        self.wifi_6_encryption_label.setText(QCoreApplication.translate("MainWindow", u"Encryption method:", None))

        self.wifi_6_cipher_label.setText(QCoreApplication.translate("MainWindow", u"Cipher:", None))

        self.commit_changes_button.setText(QCoreApplication.translate("MainWindow", u"Commit Changes", None))
    # retranslateUi

    def Establish_Connection(self):
        global passwd, ip_addr, usern

        if not self.Check_credentials:
            return 0
        # Connect
        ip_addr = self.ip_addr_line.text().strip()
        usern = self.admin_usr_line.text().strip()
        passwd = self.admin_pwd_line.text().strip()
        try:
            client.connect(hostname = ip_addr, port=22, username = usern, password = passwd)
            self.ssh_button_label.setText("Connection Established")
            self.country_combobox.setEnabled(True)
            self.country_label.setEnabled(True)

            wifi2, wifi5, wifi6 = False, False, False
            wifi2_exists, wifi2_disabled = self.Check_wifi_ghz(0)
            if wifi2_exists and not wifi2_disabled:
                self.wifi_2_widget.setVisible(True)
                self.wifi_2z_checkbox.setChecked(True)
                wifi2 = True
            elif wifi2_exists and wifi2_disabled:
                self.wifi_2_widget.setVisible(True)
                wifi2 = True

            wifi5_exists, wifi5_disabled  = self.Check_wifi_ghz(1)
            if wifi5_exists and not wifi5_disabled:
                self.wifi_5_widget.setVisible(True)
                self.wifi_5_checkbox.setChecked(True)
                wifi5 = True
            elif wifi5_exists and wifi5_disabled:
                self.wifi_5_widget.setVisible(True)
                wifi5 = True

            wifi6_exists, wifi6_disabled  = self.Check_wifi_ghz(2)
            if wifi6_exists and not wifi6_disabled:
                self.wifi_6_widget.setVisible(True)
                self.wifi_6_checkbox.setChecked(True)
                wifi6 = True
            elif wifi6_exists and wifi6_disabled:
                self.wifi_6_widget.setVisible(True)
                wifi6 = True

            if wifi2:
                self.SetCurrentWifiData(0)
            if wifi5:
                self.SetCurrentWifiData(1)
            if wifi6:
                self.SetCurrentWifiData(2)
        except Exception as e:
            self.ssh_button_label.setText("Connection Error")
            print(traceback.format_exc())


    def Check_wifi_ghz(self, num :int):
        wifi_exists = False
        wifi_disabled = False
        try:
            client.connect(hostname = ip_addr, port=22, username = usern, password = passwd)
        finally:
            stdin, stdout, stderr = client.exec_command(f"uci get wireless.radio{num}")
            rand = stdout.readline().strip()
            if rand == "wifi-device":
                wifi_exists = True

            stdin, stdout, stderr = client.exec_command(f"uci get wireless.radio{num}.disabled")
            rand = stdout.readline().strip()
            if rand == "1":
                wifi_disabled = True
            return wifi_exists, wifi_disabled

    def GetWifiData(self, radio_num:int):
        global passwd, ip_addr, usern, country_code
        current_ssid, current_passwd, current_enc, current_cipher = None, None, None, None

        client.connect(hostname = ip_addr, port=22, username = usern, password = passwd)
        stdin, stdout, stderr = client.exec_command(f"uci get wireless.default_radio{radio_num}.ssid")
        ssid = stdout.readline().strip()
        if ssid is not None:
            current_ssid = ssid

        stdin, stdout, stderr = client.exec_command(f"uci get wireless.default_radio{radio_num}.key")
        password =stdout.readline().strip()
        if stdout.readline().strip() is not None:
            current_passwd = password

        stdin, stdout, stderr = client.exec_command(f"uci get wireless.default_radio{radio_num}.encryption")
        enc = stdout.readline().strip()
        if enc is not None:
            if enc.startswith("sae-mixed"):
                current_enc = encryption.index(enc_wpa2_3)
            elif enc.startswith("sae"):
                current_enc = encryption.index(enc_wpa3)
            elif enc.startswith("psk2"):
                current_enc = encryption.index(enc_wpa2)
            elif enc.startswith("psk-mixed"):
                current_enc = encryption.index(enc_wpa1_2)
            elif enc.startswith("psk"):
                current_enc = encryption.index(enc_wpa1)
            elif enc.startswith("wep+open"):
                current_enc = encryption.index(enc_open)
            elif enc.startswith("wep"):
                current_enc = encryption.index(enc_owe)

            if "tkip+ccmp" in enc or "tkip+aes" in enc:
                current_cipher = ciphers.index(cipher_tkip_aes)
            elif "aes" in enc or "ccmp" in enc:
                current_cipher = ciphers.index(cipher_ccmp)
            elif "tkip" in enc:
                current_cipher = ciphers.index(cipher_tkip)

        if country_code is None:
            stdin, stdout, stderr = client.exec_command(f"uci get wireless.radio{radio_num}.country")
            country_code = stdout.readline().strip()
            if len(country_code) == 2:
                self.country_combobox.setCurrentIndex(countries.index(country_code))
        return current_ssid, current_passwd, current_enc, current_cipher

    def SetCurrentWifiData(self, radio_num:int):
        if radio_num == 0:
            current_ssid, current_passwd, current_enc, current_cipher  = self.GetWifiData(0)
            if current_ssid is not None:
                self.wifi_2_ssid_line.setText(current_ssid)
            if current_passwd is not None:
                self.wifi_2_pwd_line.setText(current_passwd)
            if current_enc is not None:
                self.wifi_24_encryption_combobox.setCurrentIndex(current_enc)
            if current_cipher is not None:
                self.wifi_24_encryption_combobox.setCurrentIndex(current_cipher)

        elif radio_num == 1:
            current_ssid, current_passwd, current_enc, current_cipher  = self.GetWifiData(1)
            if current_ssid is not None:
                self.wifi_5_ssid_line.setText(current_ssid)
            if current_passwd is not None:
                self.wifi_5_pwd_line.setText(current_passwd)
            if current_enc is not None:
                self.wifi_5_encryption_combobox.setCurrentIndex(current_enc)
            if current_cipher is not None:
                self.wifi_5_encryption_combobox.setCurrentIndex(current_cipher)

        elif radio_num == 2:
            current_ssid, current_passwd, current_enc, current_cipher  = self.GetWifiData(2)
            if current_ssid is not None:
                self.wifi_6_ssid_line.setText(current_ssid)
            if current_passwd is not None:
                self.wifi_6_pwd_line.setText(current_passwd)
            if current_enc is not None:
                self.wifi_6_encryption_combobox.setCurrentIndex(current_enc)
            if current_cipher is not None:
                self.wifi_6_encryption_combobox.setCurrentIndex(current_cipher)

    def CommitChanges(self):
        print(ip_addr)
        if self.wifi_2z_checkbox.isChecked():
            client.connect(hostname = ip_addr, port=22, username = usern, password = passwd)
            stdin, stdout, stderr = client.exec_command(f"uci set wireless.default_radio0.ssid={self.wifi_2_ssid_line.text()}")
            stdin, stdout, stderr = client.exec_command(f"uci set wireless.default_radio0.key={self.wifi_2_pwd_line.text()}")

            current_enc = self.GetCurrentEncryption(self.wifi_24_encryption_combobox.currentIndex, self.wifi_2_cipher_combobox.currentIndex)

            stdin, stdout, stderr = client.exec_command(f"uci set wireless.default_radio0.encryption={current_enc}")
            stdin, stdout, stderr = client.exec_command(f"uci set wireless.default_radio0.country={self.country_combobox.currentText}")
        else:
            stdin, stdout, stderr = client.exec_command(f"uci set wireless.radio0.disabled=1")
        stdin, stdout, stderr = client.exec_command("/etc/config/wireless restart")

    def GetCurrentEncryption(self, enc_index, cipher_index):
        current_enc = None

        if enc_index == encryption.index(enc_wpa3):
            current_enc = "sae"
        elif enc_index == encryption.index(enc_wpa2_3):
            current_enc = "sae-mixed"
        elif enc_index == encryption.index(enc_owe):
            current_enc = "owe"
        elif enc_index == encryption.index(enc_open):
            current_enc = "none"
        elif enc_index == encryption.index(enc_wpa1_2):
            current_enc = "psk-mixed"
        elif enc_index == encryption.index(enc_wpa2):
            current_enc = "psk2"
        elif enc_index == encryption.index(enc_wpa1):
            current_enc = "psk"

        if cipher_index == ciphers.index(cipher_tkip_aes):
            current_enc = f"{current_enc}+tkip+ccmp"
        elif cipher_index == ciphers.index(cipher_tkip):
            current_enc = f"{current_enc}+tkip"
        elif cipher_index == ciphers.index(cipher_ccmp):
            current_enc = f"{current_enc}+ccmp"
        else:
            current_enc = f"{current_enc}+ccmp"

        return current_enc

    def checkIfCipherIsNeeded(self, index):
        return (index in [encryption.index(enc_wpa2), encryption.index(enc_wpa1_2), encryption.index(enc_wpa1)])

    def onChanged2GHz(self, index):
        if self.checkIfCipherIsNeeded(index):
            self.wifi_2_cipher_combobox.setEnabled(True)
            self.wifi_2_cipher_label.setEnabled(True)
        else:
            self.wifi_2_cipher_combobox.setEnabled(False)
            self.wifi_2_cipher_label.setEnabled(False)

    def onChanged5GHz(self, index):
        if self.checkIfCipherIsNeeded(index):
            self.wifi_5_cipher_combobox.setEnabled(True)
            self.wifi_5_cipher_label.setEnabled(True)
        else:
            self.wifi_5_cipher_combobox.setEnabled(False)
            self.wifi_5_cipher_label.setEnabled(False)

    def onChanged6GHz(self, index):
        if self.checkIfCipherIsNeeded(index):
            self.wifi_6_cipher_combobox.setEnabled(True)
            self.wifi_6_cipher_label.setEnabled(True)
        else:
            self.wifi_6_cipher_combobox.setEnabled(False)
            self.wifi_6_cipher_label.setEnabled(False)

    def Check_credentials(self):
        if (not bool(self.ip_addr_line.text())) or (self.ip_addr_line is None):
            self.ssh_button_label.setText("Please Fill in the IP addresss field")
            return False

        elif (not bool (self.admin_pwd_line.text())) or (self.admin_pwd_line is None):
            self.ssh_button_label.setText("Please Fill in the Admin password field")
            return False

        elif (not bool(self.admin_usr_line.text())) or (self.admin_usr_line is None):
            self.ssh_button_label.setText("Please Fill in the Admin username field")
            return False
        return True

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec()
# sys.exit(app.exec())
sys.exit(client.close())


#        combo.currentIndexChanged.connect(self.onChanged)
#
#    def onChanged(self, index):
#        self.qlabel.setText(combo.itemText(index))
#        self.qlabel.adjustSize()
