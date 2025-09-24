#import Modules for GUI
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox

#App Setting
App = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Student Registration Form")
main_window.resize(600,300)

master_col = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()

#Application design
lbl_fName = QLabel("First Name: ")
lbl_lName = QLabel("Last Name: ")
lbl_address = QLabel("Current Address: ")

txt_fName = QLineEdit()
txt_fName.setPlaceholderText("Enter first name")
txt_lName =QLineEdit()
txt_lName.setPlaceholderText("Enter last name")

txt_address = QTextEdit()
txt_address.setFixedSize(600, 100)

btn_register = QPushButton("Register")

row1.addWidget(lbl_fName)
row1.addWidget(txt_fName)

row1.addWidget(lbl_lName)
row1.addWidget(txt_lName)

row2.addWidget(lbl_address)
row3.addWidget(txt_address)

row4.addWidget(btn_register, alignment = Qt.AlignCenter)

master_col.addLayout(row1)
master_col.addLayout(row2)
master_col.addLayout(row3)
master_col.addLayout(row4)

main_window.setLayout(master_col)

#Create a function to display the input information
def info_registered():
  QMessageBox.information(None, "Registration Data", f"Your FulL Name is {txt_lName.text()} {txt_fName.text()} and current address is {txt_address.toPlainText()}")

btn_register.clicked.connect(info_registered)
#Run Application
main_window.show()
App.exec()