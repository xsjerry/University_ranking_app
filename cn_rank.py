from ui.cn_rank import Ui_Cn_Rank
from PyQt5.QtWidgets import (QWidget, QAbstractItemView, QTableWidgetItem)
from data.cnRank_data import get_data

class Cn_rankWindow(QWidget, Ui_Cn_Rank):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) #禁止编辑
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) #整行选中

        items = get_data(2021)
        for i in range(len(items)):
            item = items[i]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(row,j,item)

        self.comboBox.currentTextChanged.connect(self.change)

    def change(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clearContents() #清空原表格内容

        items = get_data(year=self.comboBox.currentText())
        for i in range(len(items)):
            item = items[i]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(items[i][j])
                self.tableWidget.setItem(row,j,item)




