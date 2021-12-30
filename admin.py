# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1261, 801)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 170, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search = QtWidgets.QLineEdit(Dialog)
        self.search.setGeometry(QtCore.QRect(870, 170, 261, 31))
        self.search.setObjectName("search")
        self.cari = QtWidgets.QPushButton(Dialog)
        self.cari.setGeometry(QtCore.QRect(1150, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cari.setFont(font)
        self.cari.setObjectName("cari")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 210, 1241, 491))
        self.tableView.setObjectName("tableView")
        self.Delete = QtWidgets.QPushButton(Dialog)
        self.Delete.setGeometry(QtCore.QRect(1030, 720, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Delete.setFont(font)
        self.Delete.setObjectName("Delete")
        self.Update = QtWidgets.QPushButton(Dialog)
        self.Update.setGeometry(QtCore.QRect(60, 720, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Update.setFont(font)
        self.Update.setObjectName("Update")
        self.Cancel = QtWidgets.QPushButton(Dialog)
        self.Cancel.setGeometry(QtCore.QRect(550, 720, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Cancel.setFont(font)
        self.Cancel.setObjectName("Cancel")
        self.Tittle = QtWidgets.QLabel(Dialog)
        self.Tittle.setGeometry(QtCore.QRect(10, 40, 1241, 81))
        font = QtGui.QFont()
        font.setFamily("Mesquite Std")
        font.setPointSize(50)
        font.setBold(False)
        font.setWeight(50)
        self.Tittle.setFont(font)
        self.Tittle.setAlignment(QtCore.Qt.AlignCenter)
        self.Tittle.setObjectName("Tittle")
        self.comboMenu = QtWidgets.QComboBox(Dialog)
        self.comboMenu.setGeometry(QtCore.QRect(160, 170, 221, 31))
        self.comboMenu.setObjectName("comboMenu")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Pencarian :"))
        self.cari.setText(_translate("Dialog", "Cari"))
        self.Delete.setText(_translate("Dialog", "Delete"))
        self.Update.setText(_translate("Dialog", "Update"))
        self.Cancel.setText(_translate("Dialog", "Cancel"))
        self.Tittle.setText(_translate("Dialog", "Admin Freelance"))

