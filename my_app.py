from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QVBoxLayout,
       QPushButton, QLabel
)
from PyQt5.QtCore import Qt

from second_win import TestWin
from instr import (
    WIN_WIDTH, WIN_HEIGHT, WIN_X, WIN_Y, txt_title1,
    txt_hello, txt_instruction, txt_next 
)


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()          # устанавливает, как будет выглядеть окно
        self.initUI()              # создаём и настраиваем граф элементы
        self.connects()            # устанавливает связи между элементами
        self.show()                # старт 
    
    def set_appear(self):
        self.setWindowTitle(txt_title1)
        self.resize(WIN_WIDTH, WIN_HEIGHT)
        self.move(WIN_X, WIN_Y)
    
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.hide()
        self.window_test = TestWin()

    def connects(self):
        self.button.clicked.connect(self.next_click)



app = QApplication([])
main_window = MainWin()
app.exec_()