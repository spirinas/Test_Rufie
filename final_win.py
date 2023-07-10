from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QVBoxLayout,
       QPushButton, QLabel
)
from PyQt5.QtCore import Qt

from instr import *
from second_win import *



class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()          # устанавливает, как будет выглядеть окно
        self.initUI()              # создаём и настраиваем граф элементы     
        self.show()                # старт 
    
    def set_appear(self):
        self.setWindowTitle(txt_title3)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

    def initUI(self):
        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.index, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.workheart, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)
    
    def results(self):
        self.index = (
            4 * (int(self.exp.result_test1)
            + int(self.exp.result_test2) 
            + int(self.exp.result_test3)) - 200) / 10

