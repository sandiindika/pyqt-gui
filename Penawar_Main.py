import sys
import sqlite3
from Penawar import *
from PyQt5.QtWidgets import QMessageBox

class MyForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.simpan)
        self.ui.pushButton.clicked.connect(self.cek)

        #Inisialiasi nama,jenis pekerjaan, detail, Tanggal, dan Harga
        self.nama = ''
        self.Jenis_P = ''
        self.Detail_P = ''
        self.Tanggal = ''
        self.Harga = ''

        #Fungsi cek berfungsi untuk memberikan informasi jika data yang sudah dimasukkan sudah benar semua
    def cek(self):
        #Isian Dari Nama akan ditampung dalam self.nama
        self.nama = self.ui.lineEdit.text()
        if self.nama == "":
            self.ui.label_7.setText("Mohon Isi Nama Terlebih Dahulu")
        else:
            if self.nama.isalpha() or not self.nama.isalnum():
                self.ui.label_7.setText("")
            else:
                self.ui.label_7.setText("Mohon Isi Dengan Huruf")

        #Isian Dari Jenis Pekerjaan akan ditampung dalam self.Jenis_P
        self.Jenis_P = self.ui.lineEdit_2.text()
        if self.Jenis_P == "":
            self.ui.label_8.setText("Mohon Isi Jenis Pekerjaan Terlebih Dahulu")
        else:
            if self.Jenis_P.isalpha() or not self.Jenis_P.isalnum():
                self.ui.label_8.setText("")
            else:
                self.ui.label_8.setText("Mohon Isi Dengan Huruf")

        #Isian Dari Detail Pekerjaan akan ditampung dalam self.Detail_P
        self.Detail_P = self.ui.textEdit.toPlainText()
        if self.Detail_P == "":
            self.ui.label_9.setText("Mohon Isi Detail Pekerjaan Terlebih Dahulu")
        else:
            if self.Detail_P.isalpha() or not self.Detail_P.isalnum():
                self.ui.label_9.setText("")
            else:
                self.ui.label_9.setText("Mohon Isi Dengan Huruf")

        #Isian Dari Tanggal akan ditampung dalam self.Tanggal
        self.Tanggal = self.ui.dateEdit.text()
        if self.Tanggal == "01/01/2018":
            self.ui.label_10.setText("Mohon Setting Tanggal Terlebih Dahulu")
        else:
            self.ui.label_10.setText("")

        #Isian Dari Harga akan ditampung dalam self.Harga
        self.Harga = self.ui.lineEdit_3.text()
        if self.Harga == "":
            self.ui.label_11.setText("Mohon Isi Nominal Harga Terlebih Dahulu")
        else:
            if self.Harga.isdigit():
                self.ui.label_11.setText("")
            elif self.Harga.isalpha():
                self.ui.label_11.setText("Mohon Isi Dengan Nominal Angka")
            else:
                self.ui.label_11.setText("Mohon Isi Dengan Nominal Angka")

        #Memberikan Informasi Bahwa Data Yang Kita Masukkan Sudah Benar
        if (self.ui.label_7.text()== "") and (self.ui.label_8.text()== "") and (self.ui.label_9.text()== "") and (self.ui.label_10.text()== "") and (self.ui.label_11.text()==""):
            self.ui.label_12.setText("Data Sudah Benar")
        else:
            self.ui.label_12.setText("Data Masih Ada Yang Kosong")

    def simpan(self):
        #Pemberitahuan Bahwa Data Sudah Ditambahkan
        if self.ui.label_12.text()=="Data Sudah Benar":
            #self.ui.label_12.setText("Data Sudah Ditambahkan Ke Database")
            QMessageBox.about(self, "INFO", "Data Sudah Tersimpan Dalam Database")
            self.ui.label_12.setText("")
        #Untuk Menyimpan Kedalam Database    
        self.connection = sqlite3.connect('Freelance.sqlite')
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("""CREATE TABLE Freelance (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, Nama_Penawar TEXT, Jenis_Pekerjaan TEXT, Detil_Pekerjaan TEXT, Tanggal_Penawaran TEXT, Harga INTEGER, Status_Penawaran TEXT, Nama_Pengambil TEXT, Tanggal_Pengambilan TEXT)""")
        except:
            pass
        self.cursor.execute("INSERT INTO Freelance (Nama_Penawar, Jenis_Pekerjaan, Detil_Pekerjaan, Tanggal_Penawaran, Harga, Status_Penawaran) VALUES ('%s', '%s', '%s', '%s', %d, 'READY')" % (str(self.nama), str(self.Jenis_P), str(self.Detail_P), str(self.Tanggal), int(self.Harga)))
        self.connection.commit()
        self.connection.close()

        #Untuk Menset setiap isian kedalam bentuk awal
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.textEdit.setPlainText("")
        self.ui.lineEdit_3.setText("")
        self.ui.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
