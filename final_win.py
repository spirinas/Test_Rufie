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
        self.result = self.get_results()
        self.index = self.get_index()
        self.text_index = QLabel(txt_index + str(self.index))
        self.workheart = QLabel(txt_workheart + self.result)
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.text_index, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.workheart, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)
    
    def get_index(self):
        self.index = (
            4 * (self.exp.result_test1
            + self.exp.result_test2
            + self.exp.result_test3) - 200) / 10
        return self.index

    def get_results(self):
        self.index = self.get_index()
        if self.exp.age < 7:
            self.index = 0
            return "Нет данных для данного возраста"

        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif 11 <= self.index <= 14.9:
                return  txt_res2
            elif 6 <= self.index <= 10.9:
                return txt_res3
            elif 0.5 <= self.index <= 5.9:
                return  txt_res4
            else:
                return txt_res5

        if self.exp.age in (13, 14):
            if self.index >= 16.5:
                return txt_res1
            elif 12.5 <= self.index <= 16.4:
                return txt_res2
            elif 7.5 <= self.index <= 12.4:
                return txt_res3
            elif 2 <= self.index <= 7.4:
                return txt_res4
            else:
                return txt_res5

        if self.exp.age in (11, 12):
            if self.index >= 18:
                return txt_res1
            elif 14 <= self.index <= 17.9:
                return txt_res2
            elif 9 <= self.index <= 13.9:
                return txt_res3
            elif 3.5 <= self.index <= 8.9:
                return txt_res4
            else:
                return txt_res5

        if self.exp.age in (9, 10):
            if self.index >= 19.5:
                return txt_res1
            elif 15.5 <= self.index <= 19.4:
                return txt_res2
            elif 10.5 <= self.index <= 15.4:
                return txt_res3
            elif 5 <= self.index <= 10.4:
                return txt_res4
            else:
                return txt_res5
        
        if self.exp.age in (7, 8):
            if self.index >= 21:
                return txt_res1
            elif 17 <= self.index <= 20.9:
                return txt_res2
            elif 12 <= self.index <= 16.9:
                return txt_res3
            elif 6.5 <= self.index <= 11.9:
                return txt_res4
            else:
                return txt_res5