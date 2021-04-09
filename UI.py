from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDialog
import mysql.connector
#import Database
import sys

row_table = 10

class Ui_MainWindow(object):
    def setup(self, MainWindow):
        self.row_table = 10
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("โปรแกรมจักการคลังสินค้า")
        MainWindow.resize(1024, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/warehouse_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.show_table = QtWidgets.QTableWidget(self.centralwidget)
        self.show_table.setGeometry(QtCore.QRect(10,10,450,325))
        self.show_table.setColumnCount(4)
        self.show_table.setRowCount(self.row_table)
        self.show_table.setItem(0,0, QtWidgets.QTableWidgetItem("ID"))
        self.show_table.setItem(0,1, QtWidgets.QTableWidgetItem("ชื่อสินค้า"))
        self.show_table.setItem(0,2, QtWidgets.QTableWidgetItem("ชนิดสินค้า"))
        self.show_table.setItem(0,3, QtWidgets.QTableWidgetItem("จำนวน"))
        self.show_table.setObjectName("show_table")
        self.show_table.horizontalHeader().setStretchLastSection(True)
        self.show_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "zazaguy5",
            password = "426815",
            database = "warehouse"
        )
        self.mycursor = mydb.cursor()
        self.mycursor.execute(
            "select *"
            "from warehouse"
        )
        mytable = self.mycursor.fetchall()
        i = 1
        for table in mytable:
            for j in range(0,4):
                self.show_table.setItem(i,j, QtWidgets.QTableWidgetItem(table[j]))
                if j ==3:
                    self.show_table.setItem(i,j, QtWidgets.QTableWidgetItem(str(table[j])))
            i += 1

        self.show_tablebutton = QtWidgets.QPushButton(self.centralwidget)
        self.show_tablebutton.setGeometry(QtCore.QRect(10,500,80,29))
        self.show_tablebutton.setStyleSheet(
            "font: 10pt \"Ms Shell Dlg 2\";"
            "background-color: rgb(0,100,255);"
            "color: white;"
            "border-style: outset;"
            "border-radius: 6px;"
        )
        self.show_tablebutton.setText("เปิดตาราง")

        self.add_databutton = QtWidgets.QPushButton(self.centralwidget)
        self.add_databutton.setGeometry(QtCore.QRect(120,500,80,29))
        self.add_databutton.setStyleSheet(
            "font: 10pt \"Ms Shell Dlg 2\";"
            "background-color: rgb(0,100,255);"
            "color: white;"
            "border-style: outset;"
            "border-radius: 6px;"
        )
        self.add_databutton.setText("เพิ่มข้อมูล")
        self.add_databutton.clicked.connect(self.add_data)

        MainWindow.setCentralWidget(self.centralwidget)

    def add_data(self):
        self.row_table1 = 11
        good_ID = input("พิมพ์ไอดีสินค้า: ")
        good_name = input("พิมพ์ชื่อสินค้าที่จะเพิ่ม: ")
        good_type = input("พิมพ์ชนิดสินค้า: ")
        good_amount = int(input("จำนวนสินค้า: "))
        self.show_table.setRowCount(self.row_table1)
        self.show_table.setItem(self.row_table1,0, QtWidgets.QTableWidgetItem(good_ID))
        self.show_table.setItem(self.row_table1,1, QtWidgets.QTableWidgetItem(good_name))
        self.show_table.setItem(self.row_table1,2, QtWidgets.QTableWidgetItem(good_type))
        self.show_table.setItem(self.row_table1,3, QtWidgets.QTableWidgetItem(good_amount))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())