import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.content = ""
        self.calculate = 0
        self.a = 0
        self.b = 0
        self.sign = ""
        self.check = ""
        self.setWindowTitle("Calculator")
        self.setGeometry(680, 240, 510, 300)

        self.button = QPushButton('1', self)
        self.button.move(20, 100)
        self.button.clicked.connect(self.on_click_1)

        self.button = QPushButton('2', self)
        self.button.move(150, 100)
        self.button.clicked.connect(self.on_click_2)

        self.button = QPushButton('3', self)
        self.button.move(280, 100)
        self.button.clicked.connect(self.on_click_3)

        self.button = QPushButton('-', self)
        self.button.move(410, 150)
        self.button.clicked.connect(self.on_click_minus)

        self.button = QPushButton('4', self)
        self.button.move(20, 150)
        self.button.clicked.connect(self.on_click_4)

        self.button = QPushButton('5', self)
        self.button.move(150, 150)
        self.button.clicked.connect(self.on_click_5)

        self.button = QPushButton('6', self)
        self.button.move(280, 150)
        self.button.clicked.connect(self.on_click_6)

        self.button = QPushButton('+', self)
        self.button.move(410, 200)
        self.button.clicked.connect(self.on_click_plus)

        self.button = QPushButton('7', self)
        self.button.move(20, 200)
        self.button.clicked.connect(self.on_click_7)

        self.button = QPushButton('8', self)
        self.button.move(150, 200)
        self.button.clicked.connect(self.on_click_8)

        self.button = QPushButton('9', self)
        self.button.move(280, 200)
        self.button.clicked.connect(self.on_click_9)

        self.button = QPushButton('0', self)
        self.button.move(20, 250)
        self.button.clicked.connect(self.on_click_0)

        self.button = QPushButton('/', self)
        self.button.move(150, 250)
        self.button.clicked.connect(self.on_click_divide)

        self.button = QPushButton('*', self)
        self.button.move(280, 250)
        self.button.clicked.connect(self.on_click_multiply)

        self.button = QPushButton('=', self)
        self.button.move(410, 250)
        self.button.clicked.connect(self.result)

        self.button = QPushButton('C', self)
        self.button.move(410, 100)
        self.button.clicked.connect(self.on_click_c)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 40)
        self.textbox.resize(470, 30)

        self.show()

    def set(self, setter):
        if self.sign != "":
            if self.check == "":
                self.b = str(self.b) + str(setter)
                self.b = int(self.b)
        else:
            if self.sign == "":
                self.a = str(self.a) + str(setter)
                self.a = int(self.a)

    def on_click_1(self):
        self.textbox.setText(self.content + "1")
        self.content = self.content + "1"
        self.set(1)

    def on_click_2(self):
        self.textbox.setText(self.content + "2")
        self.content = self.content + "2"
        self.set(2)

    def on_click_3(self):
        self.textbox.setText(self.content + "3")
        self.content = self.content + "3"
        self.set(3)

    def on_click_4(self):
        self.textbox.setText(self.content + "4")
        self.content = self.content + "4"
        self.set(4)

    def on_click_5(self):
        self.textbox.setText(self.content + "5")
        self.content = self.content + "5"
        self.set(5)

    def on_click_6(self):
        self.textbox.setText(self.content + "6")
        self.content = self.content + "6"
        self.set(6)

    def on_click_7(self):
        self.textbox.setText(self.content + "7")
        self.content = self.content + "7"
        self.set(7)

    def on_click_8(self):
        self.textbox.setText(self.content + "8")
        self.content = self.content + "8"
        self.set(8)

    def on_click_9(self):
        self.textbox.setText(self.content + "9")
        self.content = self.content + "9"
        self.set(9)

    def on_click_0(self):
        self.textbox.setText(self.content + "0")
        self.content = self.content + "0"
        self.set(0)

    def on_click_plus(self):
        self.textbox.setText(self.content + "+")
        self.content = self.content + " + "
        self.sign = "+"

    def on_click_minus(self):
        self.textbox.setText(self.content + "-")
        self.content = self.content + " - "
        self.sign = "-"

    def on_click_divide(self):
        self.textbox.setText(self.content + "/")
        self.content = self.content + " / "
        self.sign = "/"

    def on_click_multiply(self):
        self.textbox.setText(self.content + "*")
        self.content = self.content + " * "
        self.sign = "*"

    def on_click_c(self):
        self.textbox.setText("")
        self.a = 0
        self.b = 0
        self.content = ""
        self.calculate = 0

    def add(self):
        self.calculate = self.a + self.b
        self.textbox.setText(str(self.calculate))

    def minus(self):
        self.calculate = self.a - self.b
        self.textbox.setText(str(self.calculate))

    def divide(self):
        self.calculate = self.a / self.b
        self.textbox.setText(str(self.calculate))

    def multiply(self):
        self.calculate = self.a * self.b
        self.textbox.setText(str(self.calculate))

    def result(self):
        if self.sign == "-":
            self.check = "="
            self.minus()
        elif self.sign == "+":
            self.check = "="
            self.add()
        elif self.sign == "/":
            self.check = "="
            self.divide()
        elif self.sign == "*":
            self.check = "="
            self.multiply()
        self.a = self.calculate
        self.b = 0
        self.sign = ""
        self.check = ""
        self.content = str(self.a) + " "

    def clear(self):
        self.textbox.setText("")
        self.content = ""
        self.calculate = 0
        self.a = 0
        self.b = 0


app = QApplication(sys.argv)
app.setStyle('Fusion')
ex = App()
app.exec_()
