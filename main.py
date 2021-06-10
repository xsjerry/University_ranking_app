import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QStackedLayout)

import about
import chem_rank
import cn_rank
import mainpage
import teacher
import world_rank
from ui.main_window import Ui_mainWindow


class MainWindow(QWidget, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        #图标设置
        self.setWindowIcon(QIcon("ui/icon.png"))
        self.main_button.setIcon(QIcon("ui/main.png"))
        self.cnRank_button.setIcon(QIcon("ui/china.png"))
        self.worldRank_button.setIcon(QIcon("ui/world.png"))
        self.chemRank_button.setIcon(QIcon("ui/chem.png"))
        self.teacher_button.setIcon(QIcon("ui/teacher.png"))
        self.about_button.setIcon(QIcon("ui/about.png"))
        self.logo.setIcon(QIcon("ui/logo.png"))

        #去除button边框
        Qss = '''
                QPushButton{border:none #F3F3F5; color:black;;}
                '''
        self.setStyleSheet(Qss)



        self.display = QStackedLayout(self.frame)

        self.main_page = mainpage.MainPage()
        self.cn_rank = cn_rank.Cn_rankWindow()
        self.world_rank = world_rank.world_rankWindow()
        self.chem_rank = chem_rank.Chem_rankWindow()
        self.teacher = teacher.Teacher_Window()
        self.about = about.About_Window()

        self.display.addWidget(self.main_page)
        self.display.addWidget(self.cn_rank)
        self.display.addWidget(self.world_rank)
        self.display.addWidget(self.chem_rank)
        self.display.addWidget(self.teacher)
        self.display.addWidget(self.about)


        self.controller()

    def controller(self):
        self.main_button.clicked.connect(self.switch)
        self.cnRank_button.clicked.connect(self.switch)
        self.worldRank_button.clicked.connect(self.switch)
        self.chemRank_button.clicked.connect(self.switch)
        self.teacher_button.clicked.connect(self.switch)
        self.about_button.clicked.connect(self.switch)

    def switch(self):
        sender = self.sender().objectName()

        index = {
            "main_button":0,
            "cnRank_button":1,
            "worldRank_button":2,
            "chemRank_button":3,
            "teacher_button":4,
            "about_button":5,
        }
        self.display.setCurrentIndex(index[sender])

if __name__ == "__main__":

    app = QApplication(sys.argv)
    example = MainWindow()
    Qss = '''
            QPushButton{border:1px solid #F3F3F5; color:black}
            '''
    example.setStyleSheet(Qss)
    example.show()
    sys.exit(app.exec_())