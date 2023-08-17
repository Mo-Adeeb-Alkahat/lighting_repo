

from PyQt5.QtWidgets import QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 350)
        MainWindow.setMinimumSize(QtCore.QSize(565, 350))
        MainWindow.setMaximumSize(QtCore.QSize(565, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       
        self.ib_label = QtWidgets.QLabel(self.centralwidget)
        self.ib_label.setGeometry(QtCore.QRect(250, 40, 81, 31))
        self.ib_label.setObjectName("ib_label")
        
        self.sub_current_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.sub_current_lcd.setGeometry(QtCore.QRect(230, 207, 64, 23))
        self.sub_current_lcd.setAutoFillBackground(True)
        self.sub_current_lcd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sub_current_lcd.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.sub_current_lcd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sub_current_lcd.setLineWidth(1)
        self.sub_current_lcd.setMidLineWidth(0)
        self.sub_current_lcd.setSmallDecimalPoint(False)
        self.sub_current_lcd.setDigitCount(5)
        self.sub_current_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.sub_current_lcd.setProperty("value", 0.0)
        #self.sub_current_lcd.setProperty("intValue", 0)
        self.sub_current_lcd.setObjectName("sub_current_lcd")
        
        self.sub_area_label = QtWidgets.QLabel(self.centralwidget)
        self.sub_area_label.setGeometry(QtCore.QRect(70, 150, 121, 41))
        self.sub_area_label.setObjectName("sub_area_label")
        
        self.tot_sub_power_label = QtWidgets.QLabel(self.centralwidget)
        self.tot_sub_power_label.setGeometry(QtCore.QRect(20, 45, 131, 31))
        self.tot_sub_power_label.setObjectName("tot_sub_power_label")
        
        self.iz_label = QtWidgets.QLabel(self.centralwidget)
        self.iz_label.setGeometry(QtCore.QRect(410, 40, 81, 31))
        self.iz_label.setObjectName("iz_label")
        
        
        
        self.ib = QtWidgets.QLineEdit(self.centralwidget)
        self.ib.setGeometry(QtCore.QRect(330, 50, 60, 20))
        self.ib.setText("")
        self.ib.setObjectName("ib")
        
        self.iz = QtWidgets.QLineEdit(self.centralwidget)
        self.iz.setGeometry(QtCore.QRect(480, 50, 60, 20))
        self.iz.setText("")
        self.iz.setObjectName("iz")
        
        
        
        self.sub_power = QtWidgets.QLineEdit(self.centralwidget)
        self.sub_power.setGeometry(QtCore.QRect(160, 50, 60, 20))
        self.sub_power.setBaseSize(QtCore.QSize(0, 0))
        self.sub_power.setObjectName("sub_power")
        
        self.sub_current_label = QtWidgets.QLabel(self.centralwidget)
        self.sub_current_label.setGeometry(QtCore.QRect(50, 200, 161, 31))
        self.sub_current_label.setObjectName("sub_current_label")
        
        self.sub_area_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.sub_area_lcd.setGeometry(QtCore.QRect(230, 160, 64, 23))
        self.sub_area_lcd.setAutoFillBackground(True)
        self.sub_area_lcd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sub_area_lcd.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.sub_area_lcd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sub_area_lcd.setLineWidth(1)
        self.sub_area_lcd.setMidLineWidth(0)
        self.sub_area_lcd.setSmallDecimalPoint(False)
        self.sub_area_lcd.setDigitCount(5)
        self.sub_area_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.sub_area_lcd.setProperty("value", 0.0)
        #self.sub_area_lcd.setProperty("intValue", 0)
        self.sub_area_lcd.setObjectName("sub_area_lcd")
        
        self.equa_state_label = QtWidgets.QLabel(self.centralwidget)
        self.equa_state_label.setGeometry(QtCore.QRect(220, 260, 101, 41))
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        
        self.equa_state_label.setFont(font)
        self.equa_state_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.equa_state_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.equa_state_label.setLineWidth(5)
        self.equa_state_label.setObjectName("equa_state_label")
        
        self.equa_state_const_label = QtWidgets.QLabel(self.centralwidget)
        self.equa_state_const_label.setGeometry(QtCore.QRect(30, 260, 191, 41))
        self.equa_state_const_label.setObjectName("equa_state_const_label")
        
        self.calc_button = QtWidgets.QPushButton(self.centralwidget , clicked = lambda: calc_func())
        self.calc_button.setGeometry(QtCore.QRect(450, 260, 93, 28))
        self.calc_button.setObjectName("calc_button")

        self.sub_length_label = QtWidgets.QLabel(self.centralwidget)
        self.sub_length_label.setGeometry(QtCore.QRect(130, 93, 171, 31))
        self.sub_length_label.setObjectName("sub_length_label")

        self.sub_length = QtWidgets.QLineEdit(self.centralwidget)
        self.sub_length.setGeometry(QtCore.QRect(300, 100, 60, 20))
        self.sub_length.setBaseSize(QtCore.QSize(0, 0))
        self.sub_length.setObjectName("sub_length")

        def calc_func() :
            try :
                ib = float(self.ib.text() )
                iz = float(self.iz.text() )
                sub_power = float(self.sub_power.text() )
                sub_length = float(self.sub_length.text())
                sub_area = (2*sub_power*sub_length*100) / (56*220*220*1.5)
                
                if sub_power > 0 and sub_power < 1500 : 
                    
                    
                        i = sub_power / (0.8*220)

                        self.sub_current_lcd.setProperty("value", i)
                        self.sub_area_lcd.setProperty("value", sub_area)

                        if ib <= iz and i <= ib   :
                            _translate = QtCore.QCoreApplication.translate 
                            self.equa_state_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#9d0101;\">True</span></p></body></html>"))
                        if not(ib <= iz and i <= i) :
                            _translate = QtCore.QCoreApplication.translate 
        
                            self.equa_state_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#9d0101;\">False</span></p></body></html>"))
                else :
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("value error")
                        msg.setInformativeText('')
                        msg.setWindowTitle("value error")
                        msg.exec_() 

            except :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('')
                msg.setWindowTitle("Error")
                msg.exec_() 



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ib_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">Ib</span></p></body></html>"))
        self.sub_area_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffa1a1;\">sub area</span></p></body></html>"))
        self.tot_sub_power_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">sub Power</span></p></body></html>"))
        self.iz_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">Iz</span></p></body></html>"))
        self.sub_length_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">sub length</span></p></body></html>"))
        self.sub_current_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffa1a1;\">sub current</span></p></body></html>"))
        self.equa_state_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#9d0101;\">False</span></p></body></html>"))
        self.equa_state_const_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#9d0101;\">Iu1 &lt; Ib &lt; Iz</span></p></body></html>"))
        self.calc_button.setText(_translate("MainWindow", "calc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
