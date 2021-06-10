from ui.about import Ui_About
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

class About_Window(QWidget, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.answer.setIcon(QIcon("ui/information.png"))
        self.label.setOpenExternalLinks(True)
