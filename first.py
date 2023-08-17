


from turtle import width
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_FirstWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 445)
        MainWindow.setMinimumSize(QtCore.QSize(613, 445))
        MainWindow.setMaximumSize(QtCore.QSize(613, 445))
        
       
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.k_factor_label = QtWidgets.QLabel(self.centralwidget)
        self.k_factor_label.setGeometry(QtCore.QRect(20, 230, 91, 31))
        self.k_factor_label.setObjectName("k_factor_label")
        
        self.width_label = QtWidgets.QLabel(self.centralwidget)
        self.width_label.setGeometry(QtCore.QRect(190, 65, 81, 31))
        self.width_label.setObjectName("width_label")
        
        self.maintaince_facto_label = QtWidgets.QLabel(self.centralwidget)
        self.maintaince_facto_label.setGeometry(QtCore.QRect(290, 110, 221, 31))
        self.maintaince_facto_label.setObjectName("maintaince_facto_label")
        
        self.height = QtWidgets.QLineEdit(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(470, 70, 60, 20))
        self.height.setObjectName("height")
        
        self.room_type = QtWidgets.QComboBox(self.centralwidget)
        self.room_type.setGeometry(QtCore.QRect(190, 20, 111, 31))
        self.room_type.setBaseSize(QtCore.QSize(0, 0))
        self.room_type.setAutoFillBackground(False)
        self.room_type.setEditable(False)
        self.room_type.setObjectName("room_type")
        self.room_type.addItem("")
        self.room_type.addItem("")
        self.room_type.addItem("")
        self.room_type.addItem("")
        self.room_type.addItem("")
        self.room_type.addItem("")
        self.room_type.addItem("")
        self.room_type.addItem("")
        self.room_type.addItem("")
        
        self.width = QtWidgets.QLineEdit(self.centralwidget)
        self.width.setGeometry(QtCore.QRect(280, 70, 60, 20))
        self.width.setText("")
        self.width.setObjectName("width")
        
        self.roo_label = QtWidgets.QLabel(self.centralwidget)
        self.roo_label.setGeometry(QtCore.QRect(20, 10, 151, 41))
        self.roo_label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.roo_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.roo_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.roo_label.setTextFormat(QtCore.Qt.AutoText)
        self.roo_label.setObjectName("roo_label")
        
        self.wall_color_label = QtWidgets.QLabel(self.centralwidget)
        self.wall_color_label.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.wall_color_label.setObjectName("wall_color_label")
        
        self.power_factor_label = QtWidgets.QLabel(self.centralwidget)
        self.power_factor_label.setGeometry(QtCore.QRect(340, 150, 171, 31))
        self.power_factor_label.setObjectName("power_factor_label")
        
        self.wall_color = QtWidgets.QComboBox(self.centralwidget)
        self.wall_color.setGeometry(QtCore.QRect(150, 120, 91, 22))
        self.wall_color.setObjectName("wall_color")
        self.wall_color.addItem("")
        self.wall_color.addItem("")
        
        self.fi_label = QtWidgets.QLabel(self.centralwidget)
        self.fi_label.setGeometry(QtCore.QRect(10, 270, 91, 41))
        self.fi_label.setObjectName("fi_label")
        
        self.k_factor_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.k_factor_lcd.setGeometry(QtCore.QRect(170, 230, 91, 31))
        self.k_factor_lcd.setAutoFillBackground(True)
        self.k_factor_lcd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.k_factor_lcd.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.k_factor_lcd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.k_factor_lcd.setLineWidth(1)
        self.k_factor_lcd.setMidLineWidth(0)
        self.k_factor_lcd.setSmallDecimalPoint(False)
        self.k_factor_lcd.setDigitCount(5)
        self.k_factor_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.k_factor_lcd.setProperty("value", 0.0)
        #self.k_factor_lcd.setProperty("intValue", 0)
        self.k_factor_lcd.setObjectName("k_factor_lcd")
        
        self.no_of_lambs_label = QtWidgets.QLabel(self.centralwidget)
        self.no_of_lambs_label.setGeometry(QtCore.QRect(10, 320, 141, 31))
        self.no_of_lambs_label.setObjectName("no_of_lambs_label")
        
        self.power_factor = QtWidgets.QLineEdit(self.centralwidget)
        self.power_factor.setGeometry(QtCore.QRect(520, 160, 60, 20))
        self.power_factor.setObjectName("power_factor")
        
        self.length_label = QtWidgets.QLabel(self.centralwidget)
        self.length_label.setGeometry(QtCore.QRect(20, 65, 81, 31))
        self.length_label.setObjectName("length_label")
        
        self.maintaince_factor = QtWidgets.QLineEdit(self.centralwidget)
        self.maintaince_factor.setGeometry(QtCore.QRect(520, 120, 60, 20))
        self.maintaince_factor.setObjectName("maintaince_factor")
        
        self.room_power_label = QtWidgets.QLabel(self.centralwidget)
        self.room_power_label.setGeometry(QtCore.QRect(0, 360, 161, 31))
        self.room_power_label.setObjectName("room_power_label")
        
        self.length = QtWidgets.QLineEdit(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(110, 70, 60, 20))
        self.length.setBaseSize(QtCore.QSize(0, 0))
        self.length.setObjectName("length")
        
        self.height_label = QtWidgets.QLabel(self.centralwidget)
        self.height_label.setGeometry(QtCore.QRect(380, 65, 81, 31))
        self.height_label.setObjectName("height_label")
        
        self.roof_color = QtWidgets.QComboBox(self.centralwidget)
        self.roof_color.setGeometry(QtCore.QRect(150, 155, 91, 22))
        self.roof_color.setObjectName("roof_color")
        self.roof_color.addItem("")
        self.roof_color.addItem("")
        
        self.roof_colorlabel = QtWidgets.QLabel(self.centralwidget)
        self.roof_colorlabel.setGeometry(QtCore.QRect(10, 150, 131, 31))
        self.roof_colorlabel.setObjectName("roof_colorlabel")
        
        self.full_fi_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.full_fi_lcd.setGeometry(QtCore.QRect(170, 270, 91, 31))
        self.full_fi_lcd.setAutoFillBackground(True)
        self.full_fi_lcd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.full_fi_lcd.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.full_fi_lcd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.full_fi_lcd.setLineWidth(1)
        self.full_fi_lcd.setMidLineWidth(0)
        self.full_fi_lcd.setSmallDecimalPoint(False)
        self.full_fi_lcd.setDigitCount(5)
        self.full_fi_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.full_fi_lcd.setProperty("value", 0.0)
        #self.full_fi_lcd.setProperty("intValue", 0)
        self.full_fi_lcd.setObjectName("full_fi_lcd")
        
        self.no_of_lambs_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.no_of_lambs_lcd.setGeometry(QtCore.QRect(170, 320, 91, 31))
        self.no_of_lambs_lcd.setAutoFillBackground(True)
        self.no_of_lambs_lcd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.no_of_lambs_lcd.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.no_of_lambs_lcd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.no_of_lambs_lcd.setLineWidth(1)
        self.no_of_lambs_lcd.setMidLineWidth(0)
        self.no_of_lambs_lcd.setSmallDecimalPoint(False)
        self.no_of_lambs_lcd.setDigitCount(5)
        self.no_of_lambs_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.no_of_lambs_lcd.setProperty("value", 0.0)
        #self.no_of_lambs_lcd.setProperty("intValue", 0)
        self.no_of_lambs_lcd.setObjectName("no_of_lambs_lcd")
        
        self.room_power_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.room_power_lcd.setGeometry(QtCore.QRect(170, 360, 91, 31))
        self.room_power_lcd.setAutoFillBackground(True)
        self.room_power_lcd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.room_power_lcd.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.room_power_lcd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.room_power_lcd.setLineWidth(1)
        self.room_power_lcd.setMidLineWidth(0)
        self.room_power_lcd.setSmallDecimalPoint(False)
        self.room_power_lcd.setDigitCount(5)
        self.room_power_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.room_power_lcd.setProperty("value", 0.0)
        #self.room_power_lcd.setProperty("intValue", 0)
        self.room_power_lcd.setObjectName("room_power_lcd")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(610, -20, 20, 471))
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setWindowModality(QtCore.Qt.NonModal)
        self.line_2.setGeometry(QtCore.QRect(0, 440, 621, 20))
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.calculate_room_button = QtWidgets.QPushButton(self.centralwidget , clicked = lambda: calc_func())
        self.calculate_room_button.setGeometry(QtCore.QRect(150, 400, 101, 31))
        
        def calc_func() :
            try :
                height = float(self.height.text() )
                width = float(self.width.text() )
                length = float(self.length.text() )
                maintaince_factor = float(self.maintaince_factor.text() )
                power_factor = float(self.power_factor.text() )
                room_typo = self.room_type.currentIndex()
                lum_i = lum_intensity(room_typo) 
                l1 = 0.2
                l2 = 0.5
                roof_clr = self.roof_color.currentIndex()
                wall_clr = self.wall_color.currentIndex()
                
                rm = get_the_R_value(roof_clr)
                rp = get_the_R_value(wall_clr)
                
                room_area = length * width
                eff_height = height - (l1 + l2) 
                k_factor =( (2*length) + (8*width) ) / (10 * eff_height)
                fi = (lum_i * room_area) / ( maintaince_factor * power_factor )
                n_of_lambs = fi / (2600*0.88)
                room_power = 40 * n_of_lambs
                print(lum_i)
                self.k_factor_lcd.setProperty("value", k_factor)
                self.full_fi_lcd.setProperty("value", fi)
                self.no_of_lambs_lcd.setProperty("value", n_of_lambs)
                self.room_power_lcd.setProperty("value", room_power)
            except :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('')
                msg.setWindowTitle("Error")
                msg.exec_()




        def get_the_R_value(color) :
            if color == 0 :
                return 0.5
            if color == 1 :
                return 0.7    

        def lum_intensity (room_type) :
            if room_type == 0 or room_type == 3 or room_type == 8  :
                return 50
            elif room_type == 1 or room_type == 4 or room_type == 5 :
                return 150
            elif room_type == 2 :
                return 300    
            elif room_type == 6 or room_type == 7 :
                return 100    

        
        
        self.calculate_room_button.setObjectName("calculate_room_button")
        self.add_to_total_power_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_total_power_button.setGeometry(QtCore.QRect(430, 330, 141, 31))
        
        
        
        self.add_to_total_power_button.setObjectName("add_to_total_power_button")
        
        self.tot_power_label = QtWidgets.QLabel(self.centralwidget)
        self.tot_power_label.setGeometry(QtCore.QRect(340, 220, 151, 41))
        self.tot_power_label.setObjectName("tot_power_label")
        
        self.total_power_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.total_power_lcd.setGeometry(QtCore.QRect(510, 230, 64, 23))
        self.total_power_lcd.setAutoFillBackground(True)
        self.total_power_lcd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.total_power_lcd.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.total_power_lcd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.total_power_lcd.setLineWidth(1)
        self.total_power_lcd.setMidLineWidth(0)
        self.total_power_lcd.setSmallDecimalPoint(False)
        self.total_power_lcd.setDigitCount(5)
        self.total_power_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.total_power_lcd.setProperty("value", 0.0)
        self.total_power_lcd.setProperty("intValue", 0)
        self.total_power_lcd.setObjectName("total_power_lcd")
        
        self.no_of_subs_label = QtWidgets.QLabel(self.centralwidget)
        self.no_of_subs_label.setGeometry(QtCore.QRect(350, 270, 151, 41))
        self.no_of_subs_label.setObjectName("no_of_subs_label")
        
        self.no_of_subs_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.no_of_subs_lcd.setGeometry(QtCore.QRect(510, 280, 64, 23))
        self.no_of_subs_lcd.setAutoFillBackground(True)
        self.no_of_subs_lcd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.no_of_subs_lcd.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.no_of_subs_lcd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.no_of_subs_lcd.setLineWidth(1)
        self.no_of_subs_lcd.setMidLineWidth(0)
        self.no_of_subs_lcd.setSmallDecimalPoint(False)
        self.no_of_subs_lcd.setDigitCount(5)
        self.no_of_subs_lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.no_of_subs_lcd.setProperty("value", 0.0)
        self.no_of_subs_lcd.setProperty("intValue", 0)
        self.no_of_subs_lcd.setObjectName("no_of_subs_lcd")
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.height, self.room_type)
        MainWindow.setTabOrder(self.room_type, self.width)
        MainWindow.setTabOrder(self.width, self.wall_color)
        MainWindow.setTabOrder(self.wall_color, self.power_factor)
        MainWindow.setTabOrder(self.power_factor, self.maintaince_factor)
        MainWindow.setTabOrder(self.maintaince_factor, self.length)
        MainWindow.setTabOrder(self.length, self.roof_color)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.k_factor_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffa1a1;\">K factor</span></p></body></html>"))
        self.width_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">width</span></p></body></html>"))
        self.maintaince_facto_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">maintaince_factor</span></p></body></html>"))
        self.room_type.setItemText(0, _translate("MainWindow", "1-Living"))
        self.room_type.setItemText(1, _translate("MainWindow", "2-Living_2"))
        self.room_type.setItemText(2, _translate("MainWindow", "3-Study"))
        self.room_type.setItemText(3, _translate("MainWindow", "4-Bed"))
        self.room_type.setItemText(4, _translate("MainWindow", "5-Bed_2"))
        self.room_type.setItemText(5, _translate("MainWindow", "6-Recepion"))
        self.room_type.setItemText(6, _translate("MainWindow", "7-Kitchen"))
        self.room_type.setItemText(7, _translate("MainWindow", "8-Bath_stairs"))
        self.room_type.setItemText(8, _translate("MainWindow", "9-Garage"))
        self.roo_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">Room type</span></p></body></html>"))
        self.wall_color_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">wall_color</span></p></body></html>"))
        self.power_factor_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">power_factor</span></p></body></html>"))
        self.wall_color.setItemText(0, _translate("MainWindow", "Light"))
        self.wall_color.setItemText(1, _translate("MainWindow", "Dark"))
        self.fi_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffa1a1;\">full_fi</span></p></body></html>"))
        self.no_of_lambs_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffa1a1;\">no of lambs</span></p></body></html>"))
        self.length_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">length</span></p></body></html>"))
        self.room_power_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffa1a1;\">room power</span></p></body></html>"))
        self.height_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">height</span></p></body></html>"))
        self.roof_color.setItemText(0, _translate("MainWindow", "Light"))
        self.roof_color.setItemText(1, _translate("MainWindow", "Dark"))
        self.roof_colorlabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#85adc8;\">roof_color</span></p></body></html>"))
        self.calculate_room_button.setText(_translate("MainWindow", "calc"))
        self.add_to_total_power_button.setText(_translate("MainWindow", "add to total power"))
        self.tot_power_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#881303;\">Total power</span></p></body></html>"))
        self.no_of_subs_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#881303;\">no of subs</span></p></body></html>"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
