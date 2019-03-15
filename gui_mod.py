# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_add_player_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from modify import *


class Ui_MainWindow(object):
    def newPlayer(self):
        self.juomarit = lisaa_pelaaja(self.juomarit, self.playerName.text())
        print(self.juomarit[len(self.juomarit)-1].name)
        self.InitialDrinkPage.show()
        self.InitialPlayerPage.hide()
        self.comboBox.addItem(self.juomarit[len(self.juomarit)-1].name)

    def newDrink(self):
        playername = self.comboBox.currentText()
        drink = self.lineEdit.text()
        idx = 0
        for i in range(len(self.juomarit)):
            if self.juomarit[idx].name == playername:
                idx = i
        self.juomarit[idx].lisaa_juoma(drink)
        self.lineEdit.clear()
        print(self.juomarit[idx].juomalista)
    
    def pelaa_painettu(self):
        self.pelaa_wdg.show()
        for juomari in self.juomarit:
            self.comboBox.additem(juomari.name)
    
    def arvo_juoma(self):
        idx = 0
        for i in range(self.juomarit):
            if self.juomarit[i].name == self.pelaaja_menu.currentText():
                idx = i
        juomari = self.juomarit[idx]
        juomari, juoma = pelaa(juomari)
        self.juomarit[idx] = juomari
        self.print_juoma.setText(juoma)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.juomarit = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 20, 711, 481))
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
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setObjectName("mainPage")
        self.pelaa_btn = QtWidgets.QPushButton(self.mainPage)
        self.pelaa_btn.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.pelaa_btn.setObjectName("pelaa_btn")
        self.tilastot_btn = QtWidgets.QPushButton(self.mainPage)
        self.tilastot_btn.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.tilastot_btn.setObjectName("tilastot_btn")
        self.lista_btn = QtWidgets.QPushButton(self.mainPage)
        self.lista_btn.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.lista_btn.setObjectName("lista_btn")
        self.lopeta_btn = QtWidgets.QPushButton(self.mainPage)
        self.lopeta_btn.setGeometry(QtCore.QRect(10, 160, 75, 23))
        self.lopeta_btn.setObjectName("lopeta_btn")
        self.pelaa_wdg = QtWidgets.QStackedWidget(self.mainPage)
        self.pelaa_wdg.setGeometry(QtCore.QRect(170, 10, 551, 501))
        self.pelaa_wdg.setObjectName("pelaa_wdg")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pelaa_wdg.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.roll_btn = QtWidgets.QPushButton(self.page_2)
        self.roll_btn.setGeometry(QtCore.QRect(10, 180, 341, 23))
        self.roll_btn.setObjectName("roll_btn")
        self.print_juoma = QtWidgets.QLabel(self.page_2)
        self.print_juoma.setGeometry(QtCore.QRect(10, 20, 341, 91))
        self.print_juoma.setObjectName("print_juoma")
        self.pelaaja_menu = QtWidgets.QComboBox(self.page_2)
        self.pelaaja_menu.setGeometry(QtCore.QRect(10, 150, 69, 22))
        self.pelaaja_menu.setAccessibleDescription("")
        self.pelaaja_menu.setCurrentText("")
        self.pelaaja_menu.setObjectName("pelaaja_menu")
        self.valitse_pelaaja = QtWidgets.QLabel(self.page_2)
        self.valitse_pelaaja.setGeometry(QtCore.QRect(10, 130, 81, 16))
        self.valitse_pelaaja.setObjectName("valitse_pelaaja")
        self.pelaa_wdg.addWidget(self.page_2)
        self.stackedWidget.addWidget(self.mainPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.InitialPlayerPage.show()
        self.InitialDrinkPage.hide()
        self.mainPage.hide()
        self.addPlayer.clicked.connect(self.newPlayer)
        self.pushButton.clicked.connect(self.newDrink)
        self.pelaa_btn.clicked.connect(self.pelaa_painettu)


    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addPlayer.setText(_translate("MainWindow", "Lisää pelaaja"))
        self.label.setText(_translate("MainWindow", "Syötä nimesi"))
        self.pushButton.setText(_translate("MainWindow", "Lisää juoma"))
        self.label_2.setText(_translate("MainWindow", "Syötä juoma:"))
        self.label_3.setText(_translate("MainWindow", "Valitse pelaaja"))
        self.pelaa_btn.setText(_translate("MainWindow", "Pelaa"))
        self.tilastot_btn.setText(_translate("MainWindow", "Tilastot"))
        self.lista_btn.setText(_translate("MainWindow", "Juomalista"))
        self.lopeta_btn.setText(_translate("MainWindow", "Lopeta"))
        self.roll_btn.setText(_translate("MainWindow", "Arvo juoma"))
        self.print_juoma.setText(_translate("MainWindow", "TextLabel"))
        self.valitse_pelaaja.setText(_translate("MainWindow", "Valitse pelaaja"))
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

