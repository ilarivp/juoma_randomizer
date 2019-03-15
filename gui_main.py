# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_add_player.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 30, 711, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.InitialPlayerPage = QtWidgets.QWidget()
        self.InitialPlayerPage.setObjectName("InitialPlayerPage")
        self.addPlayer = QtWidgets.QPushButton(self.InitialPlayerPage)
        self.addPlayer.setGeometry(QtCore.QRect(50, 140, 111, 31))
        self.addPlayer.setObjectName("addPlayer")
        self.label = QtWidgets.QLabel(self.InitialPlayerPage)
        self.label.setGeometry(QtCore.QRect(50, 80, 111, 16))
        self.label.setObjectName("label")
        self.playerName = QtWidgets.QLineEdit(self.InitialPlayerPage)
        self.playerName.setGeometry(QtCore.QRect(50, 110, 113, 25))
        self.playerName.setObjectName("playerName")
        self.stackedWidget.addWidget(self.InitialPlayerPage)
        self.InitialDrinkPage = QtWidgets.QWidget()
        self.InitialDrinkPage.setObjectName("InitialDrinkPage")
        self.pushButton = QtWidgets.QPushButton(self.InitialDrinkPage)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.InitialDrinkPage)
        self.label_2.setGeometry(QtCore.QRect(100, 200, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.InitialDrinkPage)
        self.lineEdit.setGeometry(QtCore.QRect(100, 230, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.tableView = QtWidgets.QTableView(self.InitialDrinkPage)
        self.tableView.setGeometry(QtCore.QRect(330, 170, 256, 192))
        self.tableView.setObjectName("tableView")
        self.comboBox = QtWidgets.QComboBox(self.InitialDrinkPage)
        self.comboBox.setGeometry(QtCore.QRect(100, 170, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.InitialDrinkPage)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 111, 21))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.InitialDrinkPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUusi_peli = QtWidgets.QAction(MainWindow)
        self.actionUusi_peli.setObjectName("actionUusi_peli")
        self.actionLopeta_peli = QtWidgets.QAction(MainWindow)
        self.actionLopeta_peli.setObjectName("actionLopeta_peli")
        self.menuFile.addAction(self.actionUusi_peli)
        self.menuFile.addAction(self.actionLopeta_peli)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addPlayer.setText(_translate("MainWindow", "Lisää pelaaja"))
        self.label.setText(_translate("MainWindow", "Syötä nimesi"))
        self.pushButton.setText(_translate("MainWindow", "Lisää juoma"))
        self.label_2.setText(_translate("MainWindow", "Syötä juoma:"))
        self.label_3.setText(_translate("MainWindow", "Valitse pelaaja"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionUusi_peli.setText(_translate("MainWindow", "Uusi peli"))
        self.actionLopeta_peli.setText(_translate("MainWindow", "Lopeta peli"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
