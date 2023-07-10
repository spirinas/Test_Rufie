from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QVBoxLayout, QHBoxLayout, 
       QLineEdit, QPushButton, 
       QLabel
)
from PyQt5.QtCore import (
        Qt, QTimer, QTimer
)

from final_win import FinalWin
from instr import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()          # устанавливает, как будет выглядеть окно
        self.initUI()              # создаём и настраиваем граф элементы
        self.connects()            # устанавливает связи между элементами
        self.show()                # старт 

    def set_appear(self):
        self.setWindowTitle(txt_title2)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)

    def initUI(self):
        self.name_text = QLabel(txt_name)
        self.hintname = QLineEdit('')
        self.age = QLabel(txt_age)
        self.hintage = QLineEdit('',)
        self.hintname.setPlaceholderText(txt_hintname)
        self.hintage.setPlaceholderText(txt_hintage)
        self.test1 = QLabel(txt_test1)
        self.test1_button = QPushButton(txt_starttest1)
        self.hinttest1 = QLineEdit('')
        self.hinttest1.setPlaceholderText(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.test2_button = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.test3_button = QPushButton(txt_starttest3)
        self.hinttest2 = QLineEdit('')
        self.hinttest2.setPlaceholderText(txt_hinttest2)
        self.hinttest3 = QLineEdit('')
        self.hinttest3.setPlaceholderText(txt_hinttest3)
        self.sendresults = QPushButton(txt_sendresults)
        self.timer = QLabel('00:00:00')

        h_line = QHBoxLayout()
        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()

        v_line1.addWidget(self.name_text, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.hintname, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.age, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.hintage, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.test1, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.test1_button,alignment=Qt.AlignLeft)
        v_line1.addWidget(self.hinttest1, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.test2, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.test2_button, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.test3, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.test3_button, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.hinttest2, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.hinttest3, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.sendresults, alignment=Qt.AlignLeft)
        v_line2.addWidget(self.timer, alignment=Qt.AlignCenter)
        h_line.addLayout(v_line1)
        h_line.addLayout(v_line2)

        self.setLayout(h_line)

    def next_click(self):
        self.hide()
        self.window_final = FinalWin()

        
    def connects(self):
        self.sendresults.clicked.connect(self.next_click)



