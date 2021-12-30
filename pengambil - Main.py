import sys
from pengambil import *
from PyQt5 import QtSql
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Project(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data = []
        self.verifIP = False
        self.verifJP = False
        self.verifDP = False
        self.loaddata()
        self.ui.pushButton.clicked.connect(self.cari)
        self.ui.pushButton_5.clicked.connect(self.tambahkan)
        self.ui.pushButton_7.clicked.connect(self.send)
    
        
    def loaddata(self):
        self.connection = sqlite3.connect('Freelance.sqlite')
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * from Freelance WHERE status_penawaran = 'READY'" )
        self.rows = self.cursor.fetchall()
        for row in self.rows:
            self.data.append([row[0], row[2],row[3]])
            self.ui.listWidget.addItem("Id : %d\nJenis Pekerjaan : %s \nDetil Pekerjaan : %s\nHarga \t: Rp. %d,-\n======================" % (row[0], row[2],row[3], row[5]))
        self.connection.commit()
        self.connection.close()
        

    def cari(self):
        if self.ui.lineEdit.text() == "":
            self.ui.listWidget.clear()
            self.loaddata()
        else:
            self.ui.listWidget.clear()
            self.connection = sqlite3.connect('Freelance.sqlite')
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * from Freelance WHERE status_penawaran = 'READY' AND Jenis_Pekerjaan like'"+self.ui.lineEdit.text()+"%'")
            self.rows = self.cursor.fetchall()
            for row in self.rows:
                self.ui.listWidget.addItem("Id : %d\nJenis Pekerjaan : %s \nDetil Pekerjaan : %s\nHarga \t: Rp. %d,-\n======================" % (row[0], row[2],row[3], row[5]))
            self.connection.commit()
            self.connection.close()
        
    def tambahkan(self):
        #cek nama
        if self.ui.lineEdit_2.text() == "":
            QMessageBox.about(self, "Error", "Masukkan nama Anda!")
            self.ui.lineEdit_2.setFocus()            
      
        #cek id pekerjaan
        for i in range(len(self.data)):
            if int(self.ui.lineEdit_5.text()) == self.data[i][0]:
                self.verifIP = True
                self.ui.label_10.setText("")
                break
            elif self.ui.lineEdit_5.text() == "":
                self.ui.label_10.setText("Diisi terlebih dahulu!")
            else:
                self.ui.label_10.setText("Periksa kembali masukkan Anda!")

        #cek jenis pekerjaan
        for i in range(len(self.data)):
            if self.ui.lineEdit_3.text() == self.data[i][1]:
                self.verifJP = True
                self.ui.label_7.setText("")
                break
            elif self.ui.lineEdit_3.text() == "":
                self.ui.label_7.setText("Diisi terlebih dahulu!")
            else:
                self.ui.label_7.setText("Periksa kembali masukkan Anda!")
        
        #cek detil pekerjaan
        for j in range(len(self.data)):
            if self.ui.lineEdit_4.text() == self.data[j][2]:
                self.verifDP = True
                self.ui.label_8.setText("")
                break
            elif self.ui.lineEdit_4.text() == "":
                self.ui.label_8.setText("Diisi terlebih dahulu!")
            else:
                self.ui.label_8.setText("Periksa kembali masukkan Anda!")

        if self.verifIP and self.verifJP and self.verifDP:
            self.ui.listWidget_2.addItem(self.ui.lineEdit_5.text())
            self.ui.listWidget_2.addItem(self.ui.lineEdit_2.text())
            self.ui.listWidget_2.addItem(self.ui.dateEdit.text())
            self.ui.listWidget_2.addItem(self.ui.lineEdit_3.text())
        
    def send(self):
        if self.verifIP and self.verifJP and self.verifDP:
            self.connection = sqlite3.connect('Freelance.sqlite')
            self.cursor = self.connection.cursor()
            self.cursor.execute("UPDATE Freelance SET Status_Penawaran = 'SOLD', Nama_Pengambil = '%s', Tanggal_Pengambilan = '%s' WHERE id = '%d' AND Jenis_Pekerjaan = '%s' AND Detil_Pekerjaan = '%s'" % (self.ui.lineEdit_2.text(), self.ui.dateEdit.text(), int(self.ui.lineEdit_5.text()), self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text()))
            self.connection.commit()
            self.connection.close()
            self.ui.listWidget.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.listWidget_2.clear()
            self.ui.lineEdit_5.clear()
            self.loaddata()
            QMessageBox.about(self, "Sukses", "Data Telah Terkirim")
        else:
            QMessageBox.about(self, "Error", "Tambahkan data terlebih dahulu!")
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Project()
    myapp.show()
    sys.exit(app.exec_())
