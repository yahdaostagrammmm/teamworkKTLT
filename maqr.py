# Form implementation generated from reading ui file 'maqr.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 502)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget#centralwidget {\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #fff7ad,\n"
"        stop:0.5 #ffa9f9,\n"
"        stop:1 #d98bbf\n"
"    );\n"
"    border-radius: 20px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 311, 301))
        self.label.setStyleSheet("background-color:transparent")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Pictures/Screenshots/Screenshot 2025-03-02 235953.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 330, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:transparent")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ButtonXacnhanTT = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonXacnhanTT.setGeometry(QtCore.QRect(60, 370, 121, 51))
        self.ButtonXacnhanTT.setStyleSheet("QPushButton {\n"
"    background-color: #ff69b4; /* Màu hồng */\n"
"    border: 2px solid rgb(255, 212, 243); \n"
"    border-radius: 15px; \n"
"    font: bold 12pt;\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 185, 255); /* Màu vàng khi hover */\n"
"    color: black;\n"
"    border: 3px dashed #ff69b4; /* Viền đứt đẹp đẹp */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 203, 224); \n"
"    color: white;\n"
"    border: 3px solid rgb(255, 169, 230);\n"
"}\n"
"")
        self.ButtonXacnhanTT.setObjectName("ButtonXacnhanTT")
        self.ButtonQuaylaiTT = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonQuaylaiTT.setGeometry(QtCore.QRect(210, 370, 121, 51))
        self.ButtonQuaylaiTT.setStyleSheet("QPushButton {\n"
"    background-color: #ff69b4; /* Màu hồng */\n"
"    border: 2px solid rgb(255, 212, 243); \n"
"    border-radius: 15px; \n"
"    font: bold 12pt;\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 185, 255); /* Màu vàng khi hover */\n"
"    color: black;\n"
"    border: 3px dashed #ff69b4; /* Viền đứt đẹp đẹp */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 203, 224); \n"
"    color: white;\n"
"    border: 3px solid rgb(255, 169, 230);\n"
"}\n"
"")
        self.ButtonQuaylaiTT.setObjectName("ButtonQuaylaiTT")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 396, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Vui lòng quét mã để thanh toán!"))
        self.ButtonXacnhanTT.setText(_translate("MainWindow", "Xác nhận"))
        self.ButtonQuaylaiTT.setText(_translate("MainWindow", "Quay lại"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
