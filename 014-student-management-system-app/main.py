from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from PyQt6.QtGui import QAction
import sys
import sqlite3

DB_PATH = r"014-student-management-system-app\database.db"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
    
        file_menu_item = self.menuBar().addMenu('&File')
        help_menu_item = self.menuBar().addMenu('&help')

        add_student_action = QAction('Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def loadData(self):
        connection = sqlite3.connect(DB_PATH)
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

program = MainWindow()
program.show()
program.loadData()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        
        student_name = QLineEdit()
        student_name.setPlaceholderText('Name')
        layout.addWidget(student_name)

        course_name = QComboBox()
        courses = ["Biology", "Math", 'Astronomy', 'Physics']
        course_name.addItems(courses)
        layout.addWidget(course_name)

        mobile = QLineEdit()
        mobile.setPlaceholderText("Mobile")
        layout.addWidget(mobile)

        button = QPushButton("Register")
        def func(): self.addStudent(student_name.text(), course_name.currentText(), mobile.text())
        button.clicked(func)

        self.setLayout(layout)
    
    def addStudent(self, name, course, mobile):
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        program.loadData()

app = QApplication(sys.argv)
sys.exit(app.exec())