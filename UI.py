from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDialog
import mysql.connector
import Database
import sys

row_num = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #super().__init__()
        MainWindow.setObjectName("MainWindow")
        self.row_table = 100
        MainWindow.setWindowTitle("โปรแกรมการจัดการคลังสินค้า")
        MainWindow.resize(1700, 750)
        MainWindow.setStyleSheet("background-image: url(resource/background_img.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("resource/warehouse_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)

        #================================================= Input/Output Data ================================================
        self.title = QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(330, 20, 780, 61))
        self.title.setStyleSheet("font-size: 65px; color: rgb(255,255,255);")
        self.title.setText("โปรแกรมการจัดการคลังสินค้า")

        self.show_table1 = QtWidgets.QTableWidget(self.centralwidget)
        self.show_table1.setGeometry(QtCore.QRect(20,120,541,461))
        self.show_table1.setColumnCount(4)
        self.show_table1.setRowCount(self.row_table)
        self.show_table1.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.show_table1.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("ชื่อสินค้า"))
        self.show_table1.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("ชนิดสินค้า"))
        self.show_table1.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("จำนวน"))
        self.show_table1.horizontalHeader().setStretchLastSection(True)
        self.show_table1.setStyleSheet(
            "font: 10pt;"
            "background-image: url(resource/bhwzt6.gif);"
        )

        self.show_table2 = QtWidgets.QTableWidget(self.centralwidget)
        self.show_table2.setGeometry(QtCore.QRect(940,120,355,461))
        self.show_table2.setColumnCount(3)
        self.show_table2.setRowCount(self.row_table)
        self.show_table2.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.show_table2.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("วันที่นำเข้า"))
        self.show_table2.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("จำนวนสินค้า"))
        self.show_table2.horizontalHeader().setStretchLastSection(True)
        self.show_table2.setStyleSheet(
            "font: 10pt;"
            "background-image: url(resource/bhwzt6.gif);"
        )

        self.show_table3 = QtWidgets.QTableWidget(self.centralwidget)
        self.show_table3.setGeometry(QtCore.QRect(1300,120,355,461))
        self.show_table3.setColumnCount(3)
        self.show_table3.setRowCount(self.row_table)
        self.show_table3.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("ID"))
        self.show_table3.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("วันที่นำออก"))
        self.show_table3.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("จำนวนสินค้า"))
        self.show_table3.horizontalHeader().setStretchLastSection(True)
        self.show_table3.lower()
        self.show_table3.setStyleSheet(
            "font: 10pt;"
            "background-image: url(resource/bhwzt6.gif);"
        )

        self.text1 = QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(610,180,80,20))
        self.text1.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.text1.setText("ID สินค้า:")
        self.good_id = QtWidgets.QLineEdit(self.centralwidget)
        self.good_id.setGeometry(QtCore.QRect(705,180,191,31))
        self.good_id.setStyleSheet(
            "QLineEdit {"
                "font: 10pt;"
                "background: rgb(159,226,191);" 
                "font-family: Ms Shell Dlg 2;"
                "color: black;"
            "}"
        )

        self.text2 = QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(610,260,70,20))
        self.text2.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.text2.setText("ชื่อสินค้า:")
        self.good_name = QtWidgets.QLineEdit(self.centralwidget)
        self.good_name.setGeometry(QtCore.QRect(705,260,191,31))
        self.good_name.setStyleSheet(
            "QLineEdit {"
                "font: 10pt;"
                "background: rgb(159,226,191);" 
                "font-family: Ms Shell Dlg 2;"
                "color: black;"
            "}"
        )

        self.text3 = QLabel(self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(610,340,100,20))
        self.text3.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.text3.setText("ชนิดสินค้า:")
        self.good_type = QtWidgets.QComboBox(self.centralwidget)
        self.good_type.setGeometry(QtCore.QRect(705,340,191,31))
        self.good_type.setStyleSheet(
            "QComboBox {" 
                "color: black;"
                "background-color: rgb(159,226,191);"
                "font: 10pt \"Ms Shell Dlg 2\";"
            "}"
            "QComboBox::drop-down {"
                "background-image: url(resource/drop-down-arrow.png);"
            "}"
        )
        self.good_type.addItem("")
        self.good_type.addItem("เครื่องใช้ไฟฟ้า")
        self.good_type.addItem("เครื่องดื่ม")
        self.good_type.addItem("เครื่องปรุง")
        self.good_type.addItem("อาหารแห้ง")
        self.good_type.addItem("ขนมขบเคี้ยว")
        self.good_type.addItem("อุปกรณ์การเรียน")
        self.good_type.addItem("ผลิตภัณฑ์สุขภาพ")
        self.good_type.setCurrentText("")

        self.text4 = QLabel(self.centralwidget)
        self.text4.setGeometry(QtCore.QRect(610,420,100,20))
        self.text4.setStyleSheet("font: 10pt \"Ms Shell Dlg 2\";")
        self.text4.setText("จำนวนสินค้า:")
        self.good_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.good_amount.setGeometry(QtCore.QRect(705,420,191,31))
        self.good_amount.setStyleSheet(
            "QLineEdit {"
                "font: 10pt;"
                "background: rgb(159,226,191);" 
                "font-family: Ms Shell Dlg 2;"
                "color: black;"
            "}"
        )

        self.text5 = QLabel(self.centralwidget)
        self.text5.setGeometry(QtCore.QRect(600,110,100,20))
        self.text5.setStyleSheet(
            "font: 10pt;"
            "font-family: Ms Shell Dlg 2;"
        )
        self.text5.setText("ค้นหาสินค้า:")
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(690,110,191,31))
        self.search.setStyleSheet(
            "font: 10pt \"Ms Shell Dlg 2\";"
            "background: rgb(159,226,191);"
            "color: black;"
        )
        self.search_icon = QPushButton(self.centralwidget)
        self.search_icon.setGeometry(QtCore.QRect(880,110,30,31))
        self.search_icon.setStyleSheet(
            "background-image: url(resource/search_icon.png);"
        )
        self.search_icon.clicked.connect(self.search_db)

        self.text6 = QLabel(self.centralwidget)
        self.text6.setGeometry(QtCore.QRect(610,500,100,20))
        self.text6.setStyleSheet(
            "font: 10pt;"
            "font-family: Ms Shell Dlg 2;"
        )
        self.text6.setText("วันที่สินค้าเข้า:")
        self.date_in = QtWidgets.QLineEdit(self.centralwidget)
        self.date_in.setGeometry(QtCore.QRect(700,500,191,31))
        self.date_in.setStyleSheet(
            "QLineEdit {"
                "font: 10pt;"
                "background: rgb(159,226,191);" 
                "font-family: Ms Shell Dlg 2;"
                "color: black;"
            "}"
        )

        self.text7 = QLabel(self.centralwidget)
        self.text7.setGeometry(QtCore.QRect(610,580,100,20))
        self.text7.setStyleSheet(
            "font: 10pt;"
            "font-family: Ms Shell Dlg 2;"
        )
        self.text7.setText("วันที่สินค้าออก:")
        self.date_out = QtWidgets.QLineEdit(self.centralwidget)
        self.date_out.setGeometry(QtCore.QRect(700,580,191,31))
        self.date_out.setStyleSheet(
            "QLineEdit {"
                "font: 10pt;"
                "background: rgb(159,226,191);" 
                "font-family: Ms Shell Dlg 2;"
                "color: black;"
            "}"
        )
        
        self.text8 = QLabel(self.centralwidget)
        self.text8.setGeometry(QtCore.QRect(280,630,150,25))
        self.text8.setStyleSheet(
            "font: 10pt;"
            "font-family: Ms Shell Dlg 2;"
        )
        self.text8.setText("เลือกประเภทการเพิ่มข้อมูล:")
        self.select_adddata = QtWidgets.QComboBox(self.centralwidget)
        self.select_adddata.setGeometry(QtCore.QRect(430,630,140,25))
        self.select_adddata.setStyleSheet(
            "QComboBox {" 
                "color: black;"
                "background-color: rgb(159,226,191);"
                "font: 10pt \"Ms Shell Dlg 2\";"
            "}"
            "QComboBox::drop-down {"
                "background-image: url(resource/drop-down-arrow.png);"
            "}"
        )
        self.select_adddata.addItem("")
        self.select_adddata.setCurrentText("")
        self.select_adddata.addItem("เพิ่มสินค้าใหม่")
        self.select_adddata.addItem("เพิ่มจำนวนสินค้าในคลัง")
        self.select_adddata.addItem("นำสินค้าออก")

        #================================================ Buttons =========================================================

        self.show_table1button = QPushButton(self.centralwidget)
        self.show_table1button.setGeometry(QtCore.QRect(10,660,80,29))
        self.show_table1button.setStyleSheet(
            "QPushButton {"
                "font: 10pt \"Ms Shell Dlg 2\";"
                "background: rgb(255,165,0);"
                "color: black;"
                "border-style: outset;"
                "border-radius: 6px;"
            "}"
            "QPushButton:pressed {"
                "background: rgb(204,204,0);"
                "border-style: inset;"
            "}"
        )
        self.show_table1button.setText("เปิดตาราง")
        self.show_table1button.clicked.connect(self.show_db)

        self.adddata_button = QPushButton(self.centralwidget)
        self.adddata_button.setGeometry(QtCore.QRect(600,640,80,29))
        self.adddata_button.setStyleSheet(
            "QPushButton {"
                "font: 10pt \"Ms Shell Dlg 2\";"
                "background: rgb(255,165,0);"
                "color: black;"
                "border-style: outset;"
                "border-radius: 6px;"
            "}"
            "QPushButton:pressed {"
                "background: rgb(204,204,0);"
                "border-style: inset;"
            "}"
        )
        self.adddata_button.setText("เพิ่มข้อมูล")
        self.adddata_button.clicked.connect(self.add_db)

        self.deletedata_button = QPushButton(self.centralwidget)
        self.deletedata_button.setGeometry(QtCore.QRect(700,640,80,29))
        self.deletedata_button.setStyleSheet(
            "QPushButton {"
                "font: 10pt \"Ms Shell Dlg 2\";"
                "background: rgb(255,165,0);"
                "color: black;"
                "border-style: outset;"
                "border-radius: 6px;"
            "}"
            "QPushButton:pressed {"
                "background: rgb(204,204,0);"
                "border-style: inset;"
            "}"
        )
        self.deletedata_button.setText("ลบข้อมูล")
        self.deletedata_button.clicked.connect(self.delete_db)

        self.clr_button = QPushButton(self.centralwidget)
        self.clr_button.setGeometry(QtCore.QRect(120,660,80,29))
        self.clr_button.setStyleSheet(
            "QPushButton {"
                "font: 10pt \"Ms Shell Dlg 2\";"
                "background: rgb(255,165,0);"
                "color: black;"
                "border-style: outset;"
                "border-radius: 6px;"
            "}"
            "QPushButton:pressed {"
                "background: rgb(204,204,0);"
                "border-style: inset;"
            "}"
        )
        self.clr_button.setText("เคลียร์ข้อมูล")
        self.clr_button.clicked.connect(self.clr_data)

        self.close_main = QPushButton(self.centralwidget)
        self.close_main.setGeometry(QtCore.QRect(1240,640,80,29))
        self.close_main.setStyleSheet(
            "QPushButton {"
                "font: 10pt \"Ms Shell Dlg 2\";"
                "background: rgb(255,165,0);"
                "color: black;"
                "border-style: outset;"
                "border-radius: 6px;"
            "}"
            "QPushButton:pressed {"
                "background: rgb(204,204,0);"
                "border-style: inset;"
            "}"
        )
        self.close_main.setText("ปิดโปรแกรม")
        self.close_main.clicked.connect(self.close_it)

        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(800,640,80,29))
        self.update_button.setStyleSheet(
            "QPushButton {"
                "font: 10pt \"Ms Shell Dlg 2\";"
                "background: rgb(255,165,0);"
                "color: black;"
                "border-style: outset;"
                "border-radius: 6px;"
            "}"
            "QPushButton:pressed {"
                "background: rgb(204,204,0);"
                "border-style: inset;"
            "}"
        )
        self.update_button.setText("อัพเดพข้อมูล")
        self.update_button.clicked.connect(self.update_db)

        MainWindow.setCentralWidget(self.centralwidget)

    #=================================================== Functions ========================================================

    def show_db(self):
        global row_num
        goods = Database.view_data()
        goodin = Database.view_goodin()
        goodout = Database.view_goodout()
        for row in goods:
            for j in range(4):
                if j==0 or j==3:
                    self.show_table1.setItem(row_num,j, QtWidgets.QTableWidgetItem(str(row[j])))
                else:
                    self.show_table1.setItem(row_num,j, QtWidgets.QTableWidgetItem(row[j]))
            row_num += 1
        row_num = 0
        for row in goodin:
            for j in range(3):
                if j==0 or j==2:
                    self.show_table2.setItem(row_num,j, QtWidgets.QTableWidgetItem(str(row[j])))
                else:
                    self.show_table2.setItem(row_num,j, QtWidgets.QTableWidgetItem(row[j]))
            row_num += 1
        row_num = 0
        for row in goodout:
            for j in range(3):
                if j==0 or j==2:
                    self.show_table3.setItem(row_num,j, QtWidgets.QTableWidgetItem(str(row[j])))
                else:
                    self.show_table3.setItem(row_num,j, QtWidgets.QTableWidgetItem(row[j]))
            row_num += 1
        row_num = 0

        

    def add_db(self):
        txt = self.select_adddata.currentIndex()
        if txt==1:
            Database.add_data(self.good_id.text(), self.good_name.text(), self.good_type.currentText(), self.good_amount.text())
            self.show_db()
        elif txt==2:
            Database.good_in(self.good_id.text(), self.date_in.text(), self.good_amount.text())
            self.show_db()
        elif txt==3:
            Database.good_out(self.good_id.text(), self.date_out.text(), self.good_amount.text())
            self.show_db()


    
    def delete_db(self):
        ID = self.good_id.text()
        Database.delete_data(ID)
        i = int(ID)-1
        for j in range(4):
            self.show_table1.setItem(i,j, QtWidgets.QTableWidgetItem(""))

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
        MainWindow.close()

    def clr_data(self):
        self.good_id.setText("")
        self.good_name.setText("")
        self.good_amount.setText("")
        self.good_type.setCurrentText("")
        self.search.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())