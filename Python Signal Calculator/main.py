import sys
from Generator_klasa import Generator
from PyQt5.QtWidgets import QLineEdit, QGroupBox, QGridLayout, QMessageBox, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QAction, QPushButton
from PyQt5.QtWidgets import QMainWindow, QWidget, QFileDialog, QTableWidget, QSpinBox, QDoubleSpinBox


class App (QMainWindow, QWidget):
    def __init__(self):
        super().__init__()

        self.function = ""

        self.left = 470
        self.top = 60
        self.width = 1000
        self.height = 1000
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.title = "WriteTable"
        self.setWindowTitle(self.title)

        # Lower Time Button

        self.Lower = QDoubleSpinBox(self)
        self.Lower.move(350, 150)
        self.Lower.resize(120, 100)
        self.Lower.setMaximum(float('inf'))

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.Lower, 0, 0)

        self.group1 = QGroupBox(self)
        self.group1.setTitle("Lower time range")
        self.group1.setLayout(self.layout)

        # Higher Time Button

        self.Higher = QDoubleSpinBox(self)
        self.Higher.move(500, 150)
        self.Higher.resize(120, 100)
        self.Higher.setMaximum(float('inf'))

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.Higher, 0, 0)

        self.group2 = QGroupBox(self)
        self.group2.setTitle("Higher time range")
        self.group2.setLayout(self.layout)

        # Steps Button

        self.Steps = QSpinBox(self)
        self.Steps.move(750, 150)
        self.Steps.resize(120, 100)
        self.Steps.setMaximum(2147483647)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.Steps, 0, 0)

        self.group3 = QGroupBox(self)
        self.group3.setTitle("Steps")
        self.group3.setLayout(self.layout)

        # Amplitude Button

        self.Amplitude = QDoubleSpinBox(self)
        self.Amplitude.move(350, 350)
        self.Amplitude.resize(120, 100)
        self.Amplitude.setMaximum(float('inf'))
        self.Amplitude.setMinimum(float('-inf'))

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.Amplitude, 0, 0)

        self.group4 = QGroupBox(self)
        self.group4.setTitle("Amplitude")
        self.group4.setLayout(self.layout)

        # Frequency Button

        self.Frequency = QDoubleSpinBox(self)
        self.Frequency.move(500, 350)
        self.Frequency.resize(120, 100)
        self.Frequency.setMaximum(float('inf'))
        self.Frequency.setMinimum(float('-inf'))

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.Frequency, 0, 0)

        self.group5 = QGroupBox(self)
        self.group5.setTitle("Frequency")
        self.group5.setLayout(self.layout)

        # Table

        self.table = QTableWidget(self)
        self.table.move(50, 50)
        self.table.resize(275, 500)
        self.table.setRowCount(30)
        self.table.setColumnCount(2)
        self.table.setColumnWidth(1, 175)
        self.table.setColumnWidth(0, 175)
        self.table.setItem(0, 0, QTableWidgetItem("Time (t)"))
        self.table.setItem(0, 1, QTableWidgetItem("Data (y)"))

        # Time settings group

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.group1, 0, 0)
        self.vbox.addWidget(self.group2, 2, 0)
        self.vbox.addWidget(self.group3, 3, 0)

        self.group = QGroupBox(self)
        self.group.setTitle("Time settings")
        self.group.move(450, 50)
        self.group.resize(500, 400)
        self.group.setLayout(self.vbox)

        # Parameters settings group

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.group4, 0, 0)
        self.vbox.addWidget(self.group5, 1, 0)

        self.group = QGroupBox(self)
        self.group.setTitle("Parameters settings")
        self.group.move(450, 450)
        self.group.resize(500, 400)
        self.group.setLayout(self.vbox)

        # Results table group

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.table, 0, 0)

        self.group = QGroupBox(self)
        self.group.setTitle("Results table")
        self.group.move(10, 150)
        self.group.resize(425, 800)
        self.group.setLayout(self.vbox)

        # Calculate button

        self.push = QPushButton(self)
        self.push.setText("Calculate")
        self.push.move(500, 875)
        self.push.resize(400, 50)
        self.push.clicked.connect(self.on_click)

        # Function name Button

        self.function_name = QLineEdit(self)
        self.function_name.move(10, 50)
        self.function_name.resize(350, 100)

        self.vbox = QGridLayout(self)
        self.vbox.addWidget(self.function_name, 0, 0)

        self.group = QGroupBox(self)
        self.group.setTitle("Function type")
        self.group.move(10, 50)
        self.group.resize(425, 100)
        self.group.setLayout(self.vbox)

        # QAction Menu Buttons

        sine = QAction("Sine", self)
        sine.triggered.connect(self.set_function_sine)

        rectangle = QAction("Rectangle", self)
        rectangle.triggered.connect(self.set_function_rectangle)

        triangle = QAction("Triangle", self)
        triangle.triggered.connect(self.set_function_triangle)

        sawtooth = QAction("Sawtooth", self)
        sawtooth.triggered.connect(self.set_function_sawtooth)

        white_noise = QAction("White Noise", self)
        white_noise.triggered.connect(self.set_function_white)

        save = QAction("Save", self)
        save.triggered.connect(self.save_fun)

        # MenuBar

        menu_bar = self.menuBar()
        menu = menu_bar.addMenu("Calculate")
        menu.addAction(sine)
        menu.addAction(rectangle)
        menu.addAction(triangle)
        menu.addAction(sawtooth)
        menu.addAction(white_noise)

        menu_bar2 = self.menuBar()
        menu2 = menu_bar2.addMenu("Options")
        menu2.addAction(save)

        self.show()

    # Function choose

    def set_function_sine(self):
        self.function = "Sine"
        self.function_name.setText(self.function)

    def set_function_rectangle(self):
        self.function = "Rectangle"
        self.function_name.setText(self.function)

    def set_function_triangle(self):
        self.function = "Triangle"
        self.function_name.setText(self.function)

    def set_function_sawtooth(self):
        self.function = "Sawtooth"
        self.function_name.setText(self.function)

    def set_function_white(self):
        self.function = "White Noise"
        self.function_name.setText(self.function)

    # Save Function

    def save_fun(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getOpenFileName(", "", options=options)
        file = open(filename, 'w')
        i = 0
        while i < self.gen1.steps:
            file.write(self.table.item(i, 0).text() + "\t" + self.table.item(i, 1).text() + "\n")
            i = i + 1
        file.close()

    # On_Click function for calculate

    def on_click(self):
        self.gen1 = Generator(self.Lower.value(), self.Higher.value(), self.Steps.value())
        amp = self.Amplitude.value()
        frq = self.Frequency.value()
        if self.function == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("You need to choose function before calculating.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif self.function == "Sine":
            self.gen1.sine(frq, amp)
            self.write_table()
        elif self.function == "Rectangle":
            self.gen1.square(frq, amp)
            self.write_table()
        elif self.function == "Triangle":
            self.gen1.triangle(frq, amp)
            self.write_table()
        elif self.function == "Sawtooth":
            self.gen1.sawtooth(frq, amp)
            self.write_table()
        else:
            self.gen1.white_noise(amp)
            self.write_table()

    # Function mod for table

    def write_table(self):
        i = 1
        self.table.setRowCount(self.gen1.steps)
        while i < self.gen1.steps:
            self.table.setItem(i, 0, QTableWidgetItem(str(self.gen1.t[i])))
            i = i + 1
        i = 1
        while i < self.gen1.steps:
            self.table.setItem(i, 1, QTableWidgetItem(str(self.gen1.form[i])))
            i = i + 1


app = QApplication(sys.argv)
app.setStyle("Fusion")
ex = App()
app.exec()
