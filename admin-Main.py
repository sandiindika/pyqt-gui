import sys
from admin import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtSql
class MyForm(QtWidgets.QDialog):
     def __init__(self, parent=None):
         QtWidgets.QWidget.__init__(self, parent)
         self.ui = Ui_Dialog()
         self.ui.setupUi(self)
         self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
         self.db.setDatabaseName('Freelance.sqlite')
         self.db.open()
         self.model = QtSql.QSqlTableModel(self)
         self.model.setTable("Freelance")
         self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
         self.model.select()
         self.ui.tableView.setModel(self.model)
         self.ui.tableView.setColumnHidden(0, True) #menyembunyikan coloumn hanya pada table view

         #lineEdit search 
         self.ui.search.setPlaceholderText("Masukkan Nama Penawar")

         #comboBox menu
         self.searchBy=['Nama Penawar', 'Nama Pengambil', 'Jenis Pekerjaan', 'Tanggal Penawaran', 'Tanggal Pengambilan', 'Pekerjaan Tersedia']
         self.addcontent()
         self.ui.comboMenu.currentIndexChanged.connect(self.selectionchange)
         self.indexMenu = 0

         #button
         self.ui.cari.clicked.connect(self.SearchRecord)
         self.ui.Update.clicked.connect(self.UpdateRecord)
         self.ui.Cancel.clicked.connect(self.CancelAll)
         self.ui.Delete.clicked.connect(self.DeleteRecord)
          
     def addcontent(self):
         for i in self.searchBy:
               self.ui.comboMenu.addItem(i)

     def selectionchange(self, i):
         chosen = self.ui.comboMenu.currentText()
         if chosen == 'Nama Penawar':
               self.ui.search.setEnabled(True)
               self.ui.search.setPlaceholderText("Masukkan Nama Penawar")
               self.indexMenu = i
         elif chosen == 'Nama Pengambil':
               self.ui.search.setEnabled(True)
               self.ui.search.setPlaceholderText("Masukkan Nama Pengambil")
               self.indexMenu = i
         elif chosen == 'Jenis Pekerjaan':
               self.ui.search.setEnabled(True)
               self.ui.search.setPlaceholderText("Masukkan Jenis Pekerjaan")
               self.indexMenu = i
         elif chosen == 'Tanggal Penawaran':
               self.ui.search.setEnabled(True)
               self.ui.search.setPlaceholderText("Masukkan Tanggal Penawaran (dd/mm/yyyy)")
               self.indexMenu = i
         elif chosen == 'Tanggal Pengambilan':
               self.ui.search.setEnabled(True)
               self.ui.search.setPlaceholderText("Masukkan Tanggal Pengambilan (dd/mm/yyyy)")
               self.indexMenu = i
         else:
               self.ui.search.setEnabled(False)
               self.ui.search.setPlaceholderText("Klik tombol cari! ")
               self.indexMenu = i
               
              
     def UpdateRecord(self):
         QMessageBox.about(self, "Sukses", "Data berhasil di update")
         self.model.submitAll()
         
     def CancelAll(self):
         self.model.revertAll()
         
     def DeleteRecord(self):
         self.model.removeRow(self.ui.tableView.currentIndex().row())
         self.model.submitAll()
         
     def SearchRecord(self):
         if self.indexMenu == 0:
               self.model.setFilter("Nama_Penawar like'"+self.ui.search.text()+"%'")
         elif self.indexMenu == 1:
               self.model.setFilter("Nama_Pengambil like'"+self.ui.search.text()+"%'")
         elif self.indexMenu == 2:
               self.model.setFilter("Jenis_Pekerjaan like'"+self.ui.search.text()+"%'")
         elif self.indexMenu == 3:
               self.model.setFilter("Tanggal_Penawaran like'"+self.ui.search.text()+"%'")
         elif self.indexMenu == 4:
               self.model.setFilter("Tanggal_Pengambilan like'"+self.ui.search.text()+"%'")
         else:
               self.model.setFilter("Status_Penawaran like'READY%'")
              
              
         
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     myapp = MyForm()
     myapp.show()
     sys.exit(app.exec_())
