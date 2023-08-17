

from re import X
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 338)
        MainWindow.setMinimumSize(QtCore.QSize(563, 338))
        MainWindow.setMaximumSize(QtCore.QSize(563, 338))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 571, 161))
        self.label.setObjectName("label")

        self.goto_subs_button = QtWidgets.QPushButton(self.centralwidget , clicked = lambda: self.goto_subs_func() )
        self.goto_subs_button.setGeometry(QtCore.QRect(200, 170, 131, 41))
        self.goto_subs_button.setObjectName("goto_subs_button")

        self.goto_room_button = QtWidgets.QPushButton(self.centralwidget , clicked = lambda: self.goto_room_func())
        self.goto_room_button.setGeometry(QtCore.QRect(200, 240, 131, 41))
        self.goto_room_button.setObjectName("goto_room_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#bd0e0e;\">Done by : Adeeb , Abdullah , Amjad &amp; Hazem</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#bd0e0e;\">computer ENG 3rd year project </span></p></body></html>"))
        self.goto_subs_button.setText(_translate("MainWindow", "Subs calc"))
        self.goto_room_button.setText(_translate("MainWindow", "Room calc"))

    def goto_subs_func(self) :

        filename = 'second.py'
        filename1 = 'second.exe'

        #os.system(filename)
        os.system('python '+filename)
        #os.system('python '+filename1)

        

    def goto_room_func(self) :

        filename = 'first.py'
        filename1 = 'first.exe'

        #os.system(filename)
        os.system('python '+filename)
        #os.system('python '+filename1)
    

    def open_win(self) :
        self.window = MainWindow = QtWidgets.QMainWindow()
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
