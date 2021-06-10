from ui.teacher import Ui_Teacher
from PyQt5.QtWidgets import (QWidget, QAbstractItemView, QTableWidgetItem)
import sqlite3

class Teacher_Window(QWidget, Ui_Teacher):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)


        db_file = "data/teacher.db"  #数据库文件
        conn = sqlite3.connect(db_file)  #获取与数据库的连接

        #编写sql语句
        sql = 'select * from Teacher'
        cur = conn.cursor()
        cur.execute(sql)

        items = cur.fetchall()
        for i in range(len(items)):
            item = items[i]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(row,j,item)

        #关闭数据库
        conn.close()





