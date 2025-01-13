from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        name_label = QLabel("Name: ")
        self.name_line_edit = QLineEdit()

        date_birth_label = QLabel("Year of Birth: ")
        self.date_birth_line_edit = QLineEdit()

        self.calculate_label = QLabel("")
        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)

        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)

        grid.addWidget(self.calculate_label, 2, 0, 1, 2)
        grid.addWidget(calculate_button, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        name = self.name_line_edit.text()
        date_of_birth = self.date_birth_line_edit.text()
        age = datetime.now().year - int(date_of_birth.split("/")[0])
        self.calculate_label.setText(f"{name} is {int(age)} years old")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())