from ui.chem_rank import Ui_Chem_Rank
from PyQt5.QtWidgets import (QWidget, QAbstractItemView, QTableWidgetItem)
from data.chemRank_data import get_worldData, get_cnData

class Chem_rankWindow(QWidget, Ui_Chem_Rank):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        items = get_cnData()
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
        self.tableWidget.clearContents()

        if self.comboBox.currentText() == "中国":
            items = get_cnData()
        else:
            items = get_worldData()

        for i in range(len(items)):
            item = items[i]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(row,j,item)
