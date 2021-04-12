from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDialog
import mysql.connector
import Database
import sys

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.row_table = 12
        self.setWindowTitle("โปรแกรมจักการคลังสินค้า")
        self.resize(1024, 600)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("resource/warehouse_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.icon)

        #================================================= Input/Output Data ================================================

        self.show_table = QtWidgets.QTableWidget(self)
        self.show_table.setGeometry(QtCore.QRect(10,10,450,325))
        self.show_table.setColumnCount(4)
        self.show_table.setRowCount(self.row_table)
        self.show_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.show_table.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("ชื่อสินค้า"))
        self.show_table.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("จำนวนสินค้า"))
        self.show_table.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("จำนวน"))
        self.show_table.horizontalHeader().setStretchLastSection(True)
        #self.show_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.text1 = QLabel(self)
        self.text1.setGeometry(QtCore.QRect(540,10,50,20))
        self.text1.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.text1.setText("ID สินค้า:")
        self.good_id = QtWidgets.QLineEdit(self)
        self.good_id.setGeometry(QtCore.QRect(600,10,100,20))
        self.good_id.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")

        self.text2 = QLabel(self)
        self.text2.setGeometry(QtCore.QRect(540,50,50,20))
        self.text2.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.text2.setText("ชื่อสินค้า:")
        self.good_name = QtWidgets.QLineEdit(self)
        self.good_name.setGeometry(QtCore.QRect(600,50,100,20))
        self.good_name.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")

        self.text3 = QLabel(self)
        self.text3.setGeometry(QtCore.QRect(540,90,60,20))
        self.text3.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.text3.setText("ชนิดสินค้า:")
        self.good_type = QtWidgets.QComboBox(self)
        self.good_type.setGeometry(QtCore.QRect(605,90,138,20))
        self.good_type.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.good_type.addItem("เครื่องใช้ไฟฟ้า")
        self.good_type.addItem("เครื่องดื่ม")
        self.good_type.addItem("เครื่องปรุง")
        self.good_type.addItem("อาหารแห้ง")
        self.good_type.addItem("ขนมขบเคี้ยว")
        self.good_type.addItem("อุปกรณ์การเรียน")
        self.good_type.addItem("ผลิตภัณฑ์สุขภาพ")

        self.text4 = QLabel(self)
        self.text4.setGeometry(QtCore.QRect(540,130,80,20))
        self.text4.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.text4.setText("จำนวนสินค้า:")
        self.good_amount = QtWidgets.QLineEdit(self)
        self.good_amount.setGeometry(QtCore.QRect(620,130,100,20))
        self.good_amount.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")

        self.search = QtWidgets.QLineEdit(self)
        self.search.setGeometry(QtCore.QRect(500,220,100,20))
        self.search.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.search_icon = QPushButton(self)
        self.search_icon.setGeometry(QtCore.QRect(600,220,20,20))
        self.search_icon.setStyleSheet(
            "QPushButton:open { /* when the button has its menu open */"
                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);"
            "}"

            "QPushButton::menu-indicator {"
                "image: url(menu_indicator.png);"
                "subcontrol-origin: padding;"
                "subcontrol-position: bottom right;"
            "}"

            "QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {"
                "position: relative;"
                "top: 2px; left: 2px; /* shift the arrow by 2 px */"
            "}"
        )
        self.search_icon.clicked.connect(self.search_db)

        #================================================ Buttons =========================================================

        self.show_tablebutton = QPushButton(self)
        self.show_tablebutton.setGeometry(QtCore.QRect(10,500,80,29))
        self.show_tablebutton.setStyleSheet(
            "font: 10pt \"Ms Shell Dlg 2\";"
            "background-color: rgb(0,100,255);"
            "color: white;"
            "border-style: outset;"
            "border-radius: 6px;"
        )
        self.show_tablebutton.setText("เปิดตาราง")
        self.show_tablebutton.clicked.connect(self.show_db)

        self.adddata_button = QPushButton(self)
        self.adddata_button.setGeometry(QtCore.QRect(550,170,80,29))
        self.adddata_button.setStyleSheet(
            "font: 10pt \"Ms Shell Dlg 2\";"
            "background-color: rgb(0,100,255);"
            "color: white;"
            "border-style: outset;"
            "border-radius: 6px;"
        )
        self.adddata_button.setText("เพิ่มข้อมูล")
        self.adddata_button.clicked.connect(self.add_db)

        self.deletedata_button = QPushButton(self)
        self.deletedata_button.setGeometry(QtCore.QRect(650,170,80,29))
        self.deletedata_button.setStyleSheet(
            "font: 10pt \"Ms Shell Dlg 2\";"
            "background-color: rgb(0,100,255);"
            "color: white;"
            "border-style: outset;"
            "border-radius: 6px;"
        )
        self.deletedata_button.setText("ลบข้อมูล")
        self.deletedata_button.clicked.connect(self.delete_db)

        self.clr_button = QPushButton(self)
        self.clr_button.setGeometry(QtCore.QRect(120,500,80,29))
        self.clr_button.setStyleSheet(
            "font: 10pt \"Ms Shell Dlg 2\";"
            "background-color: rgb(0,100,255);"
            "color: white;"
            "border-style: outset;"
            "border-radius: 6px;"
        )
        self.clr_button.setText("เคลียร์ข้อมูล")
        self.clr_button.clicked.connect(self.clr_data)

        self.close_main = QPushButton(self)
        self.close_main.setGeometry(QtCore.QRect(840,500,80,29))
        self.close_main.setStyleSheet(
            "font: 10pt \"Ms Shell Dlg 2\";"
            "background-color: rgb(0,100,255);"
            "color: white;"
            "border-style: outset;"
            "border-radius: 6px;"
        )
        self.close_main.setText("ปิดโปรแกรม")
        self.close_main.clicked.connect(self.close_it)

        self.update_button = QPushButton(self)
        self.update_button.setGeometry(QtCore.QRect(750,50,80,29))
        self.update_button.setStyleSheet(
            "font: 9pt \"Ms Shell Dlg 2\";"
            "background-color: rgb(0,100,255);"
            "color: white;"
            "border-style: outset;"
            "border-radius: 6px;"
        )
        self.update_button.setText("อัพเดพข้อมูล")
        self.update_button.clicked.connect(self.update_db)

    #=================================================== Functions ========================================================

    def show_db(self):
        global row_num 
        row_num = 0
        data = Database.view_data()
        for row in data:
            for j in range(4):
                if j==0 or j==3:
                    self.show_table.setItem(row_num,j, QtWidgets.QTableWidgetItem(str(row[j])))
                else:
                    self.show_table.setItem(row_num,j, QtWidgets.QTableWidgetItem(row[j]))
            row_num += 1

    def add_db(self):
        Database.add_data(int(self.good_id.text()), self.good_name.text(), self.good_type.currentText(), int(self.good_amount.text()))
        self.show_db()

    
    def delete_db(self):
        ID = self.good_id.text()
        Database.delete_data(ID)
        i = int(ID)-1
        for j in range(4):
            self.show_table.setItem(i,j, QtWidgets.QTableWidgetItem(""))

    def search_db(self):
        ID = self.search.text()
        data = Database.search_data(ID)
        self.good_id.setText(str(data[0][0]))
        self.good_name.setText(data[0][1])
        self.good_type.setCurrentText(data[0][2])
        self.good_amount.setText(str(data[0][3]))

    def update_db(self):
        Database.update_data(int(self.good_id.text()), self.good_name.text(), self.good_type.currentText(), int(self.good_amount.text()))
        self.show_db()

    def close_it(self):
        self.close()

    def clr_data(self):
        self.good_id.setText("")
        self.good_name.setText("")
        self.good_amount.setText("")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())