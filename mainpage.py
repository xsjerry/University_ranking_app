from ui.mainpage import Ui_MainPage
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

class MainPage(QWidget, Ui_MainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.background.setIcon(QIcon("ui/background.png"))
        self.teacher_button.setIcon(QIcon("ui/finger.png"))
        self.chemRank_button.setIcon(QIcon("ui/finger.png"))
        self.worldRank_button.setIcon(QIcon("ui/finger.png"))
        self.cnRank_button.setIcon(QIcon("ui/finger.png"))