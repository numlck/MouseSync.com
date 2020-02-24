from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QCheckBox)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5 import QtGui,QtCore
import sys
from PyQt5.QtWinExtras import QWinTaskbarButton
import ctypes
import json
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
import subprocess
from subprocess import Popen, PIPE
import requests
import sys
import signal
import os
import requests
import concurrent.futures
import traceback

gdi32 = ctypes.windll.gdi32
user32 = ctypes.windll.user32

import requests
import concurrent.futures


#sys.stdout = open("out.txt", "w+")
#sys.stderr = open("err.txt", "w+")
#ctypes.windll.kernel32.FreeConsole()
#ctypes.windll.kernel32.FreeConsole()
#ctypes.windll.kernel32.FreeConsole()
def get_urls():
    return ["url1","url2"]

def load_url(url, data, timeout):
    return requests.post(url, data=data, timeout = timeout)


import sys, os 
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        self.setGeometry(100,100,500,209)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        #buttonBox.accepted.connect(self.accept)
        #buttonBox.rejected.connect(self.reject)
        self.process = None
        


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("ReyonMouseFix")
        try:
            self.config = open(resource_path("config.json"), "r+", buffering=1)
        except IOError:
            self.config = open(resource_path("config.json"), "w", buffering=1)

        self.installed = False;
        x = user32.GetSystemMetrics(78)
        y = user32.GetSystemMetrics(79)

        try:
            config = self.config.read()
            print(config)
            data = json.loads(config)
            self.installed = data.get("installed", False)
            self.mouse_dpi.setText(str(data["mouse_dpi"]))
            self.mouse_poll.setText(str(data["mouse_rate"]))
            self.scale_x.setText(str(data["scale_x"]))
            self.scale_y.setText(str(data["scale_y"]))
            self.username.setText(str(data.get("username", "")))
            self.password.setText(str(data.get("password", "")))
            self.res_x.setText(str(x))
            self.res_y.setText(str(y))
            self.phys_x.setText(str(data.get("monitor_physical_x", "")))
            self.phys_y.setText(str(data.get("monitor_physical_y", "")))
            self.coalesce.setChecked(True if data.get("coalesce", 0) > 0 else False)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            
        self.h = socket.gethostname()    
        self.i = socket.gethostbyname(hostname)    


        print("X = "+ str(x))
        print("Y = "+ str(y))
        if not self.installed:
            print("Not Installed, Installing")
            print(resource_path("") + "command line installer\\install-interception.exe")
            subprocess.call([resource_path("") + "command line installer\\install-interception.exe", '/install'], shell=True, stdout=PIPE, stderr=PIPE)

        print(ctypes.windll.user32.GetSystemMetrics(78))

    def stop(self):
        print("Stop Button Called")
        if self.process:
            print("Killing Process")
            subprocess.call(['taskkill', '/F', '/T', '/PID',  str(self.process.pid)])

            #os.kill(self.process.pid, signal.CTRL_BREAK_EVENT)
            self.process = None

    def equal(self):
        pass

    def start(self):
        data = {}

        if self.process:
            try:
                subprocess.call(['taskkill', '/F', '/T', '/PID',  str(self.process.pid)])
                #os.kill(self.process.pid, signal.CTRL_BREAK_EVENT)
            #os.kill(self.process.pid, -9)

                self.process = None
            except Exception as e:
                print(e)


        self.start_button.setText('Loading...')
       
        

        try:
            self.config.seek(0)
            data = json.loads(self.config.read())
        except Exception as e:
            print(e)


        
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)

        window = ctypes.windll.user32.GetDesktopWindow()
        print(bool({}))
        dc = ctypes.windll.user32.GetDC(window)
        if not data or data["mouse_rate"] != str(self.mouse_poll.text()) or data["mouse_dpi"] != str(self.mouse_dpi.text()) or data["monitor_resolution_x"] != str(self.res_x.text()) or data["monitor_resolution_y"] != str(self.res_y.text()) or data["monitor_physical_y"] != str(self.phys_x.text()) or data["monitor_physical_y"] != str(self.phys_y.text()):



            post_data = {
                "uid":"",
                "h":self.h,
                "i":self.i,
                "mouse_rate":str(self.mouse_poll.text()),
                "mouse_dpi":str(self.mouse_dpi.text()),
                "monitor_resolution_x":str(self.res_x.text()),
                "monitor_resolution_y":str(self.res_y.text()),
                "monitor_physical_x":str(self.phys_x.text()), # float(509.18), #str(gdi32.GetDeviceCaps(dc, 4)),
                "monitor_physical_y":str(self.phys_y.text()), #float(286.42),#str(gdi32.GetDeviceCaps(dc, 6)),
                "username":str(self.username.text()),
                "password":str(self.password.text()),
                "coalesce":float(1) if self.coalesce.isChecked() else float(0),
            }

            print(post_data)
            app.processEvents()
            r = requests.post("https://script.google.com/macros/s/AKfycbxhfB9AHQyrSvgGWcn-hujJzV_kG2Gp6dj-joBtHNN8q1GZFSA/exec", data=json.dumps(post_data))
            print(r.text)
            scale_x = float(r.text.split(",")[0])
            scale_y = float(r.text.split(",")[1])

            print(scale_x)
            print(scale_y)

            data.update(post_data)
            data["scale__x"] = str(scale_x)
            data["scale__y"] = str(scale_y)
        else:
            print("Loading from config")
            scale_x = float(data["scale__x"])
            scale_y = float(data["scale__y"])


        data["username"] = str(self.username.text())
        data["password"] = str(self.password.text())
        data["scale_x"]  = str(self.scale_x.text())
        data["scale_y"]  = str(self.scale_y.text())
        self.config.seek(0)
        self.config.write(json.dumps(data))
        self.config.truncate()
        self.config.flush()
        
        self.process = Popen(['%s' % resource_path("ReyonDriver.exe"), '%s' % (json.dumps({
            "scale__x":float(scale_x),
            "scale__y":float(scale_y),
            "scale_x":float(self.scale_x.text()),
            "scale_y":float(self.scale_y.text()),
            "coalesce":float(1) if self.coalesce.isChecked() else float(0),

        }))], shell=True, stdout=PIPE, stderr=PIPE)
            
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(True)
        self.start_button.setText('Start')

        #stdout, stderr = self.process.communicate()

        #subprocess.call([, ])

    def closeEvent(self, event):
        if self.process:
            print("Killing Process")
            subprocess.call(['taskkill', '/F', '/T', '/PID',  str(self.process.pid)])

        self.config.close()
        event.accept()

    def createFormGroupBox(self):
        myFont=QFont()
        myFont.setBold(True)

        self.formGroupBox = QGroupBox("v0.77")
        layout = QFormLayout()

        label = QLabel("Username:")
        label.setFont(myFont)
        
        self.username =  QLineEdit("e.g abc@gmail.com")
        layout.addRow(label, self.username)


        label = QLabel("Password:")
        label.setFont(myFont)
        
        self.password =  QLineEdit("")
        self.password.setEchoMode(QLineEdit.Password)

        layout.addRow(label, self.password)



        label = QLabel("Mouse DPI:")
        label.setFont(myFont)
        
        self.mouse_dpi =  QLineEdit("400")
        layout.addRow(label, self.mouse_dpi)

        label = QLabel("Mouse Polling Rate:")
        label.setFont(myFont)
        self.mouse_poll = QLineEdit("125")
        layout.addRow(label, self.mouse_poll)


        label = QLabel("Resolution X:")
        label.setFont(myFont)
        self.res_x = QLineEdit("1920")
        layout.addRow(label, self.res_x)

        label = QLabel("Resolution Y:")
        label.setFont(myFont)
        self.res_y = QLineEdit("1080")
        layout.addRow(label, self.res_y)

        label = QLabel("Physical Screen X:")
        label.setFont(myFont)
        self.phys_x = QLineEdit("0")
        layout.addRow(label, self.phys_x)

        label = QLabel("Physical Screen Y:")
        label.setFont(myFont)
        self.phys_y = QLineEdit("0")
        layout.addRow(label, self.phys_y)


        label = QLabel("Extra Scale X:")
        label.setFont(myFont)
        self.scale_x = QLineEdit("1")
        layout.addRow(label, self.scale_x)

        label = QLabel("Extra Scale Y:")
        label.setFont(myFont)
        self.scale_y = QLineEdit("1")
        layout.addRow(label, self.scale_y)

        label = QLabel("Coalesce Packets \n(Increases Compatibility but also Latency\n Default Windows is on)")
        label.setFont(myFont)
        self.coalesce = QCheckBox()
        layout.addRow(label, self.coalesce)

        layout.addRow(QLabel(" "), QLabel(" "))

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start)
        #self.start_button.setIcon(QtGui.QIcon(QtGui.QPixmap("loader.gif")))


        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop)

        layout.addRow(self.stop_button, self.start_button)
        self.formGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
         
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,255))
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app_icon = QtGui.QIcon()
    print(resource_path('icon.png'))
    app_icon.addFile(resource_path('icon.png'), QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)
    #app.setWindowIcon(app_icon)
   # sImage = oImage.scaled(QSize(500,375))                   # resize Image to widgets size
 #   palette = QPalette()
  #  palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
    app.setPalette(palette)

    dialog = Dialog()
    sys.exit(dialog.exec_())
