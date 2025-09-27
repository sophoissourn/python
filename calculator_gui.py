#import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLineEdit,QMessageBox
from functools import partial

#App Setting
App = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(250,300)
master_layout = QVBoxLayout
grid_layout = QGridLayout()

#Create GUI Elements for App
btn_title_lists = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3" , "-", "0" , ".", "=" , "+"]

txt_result = QLineEdit()
grid_layout.addWidget(txt_result, 0, 0,1, 4)

btn_clear = QPushButton("Clear")
btn_delete = QPushButton("<")

#loop to create each calculator button and label
def calculate(btn_label):
  # QMessageBox.information(None, "Calculator", "Hello")
  current_text = txt_result.text()
  txt_result.setText(current_text + btn_label )
  if btn_label == "=":
    txt_result.setText(str(eval(current_text)))
  elif btn_label == "Clear":
    txt_result.clear()
  elif btn_label == "Delete":
    txt_result.setText(current_text[:-1])
  else:
    txt_result.setText(current_text + btn_label )
                  
  
  
row = 1
col = 0
#======using Lamda anonymous function==========
"""
for btn_label in btn_title_lists:
  btn = QPushButton(btn_label)
  btn.clicked.connect(lambda checked, btn_label=btn_label: calculate(btn_label))
  grid_layout.addWidget(btn, row, col)
  grid_layout.setSpacing(5)
  # grid_layout.setContentsMargins(0,20,20,500)
  col += 1
  if col > 3:
    col = 0
    row += 1
"""
#======using Partial from FuncTools module==========
for btn_label in btn_title_lists:
  btn = QPushButton(btn_label)
  btn.clicked.connect(partial(calculate, btn_label))
  grid_layout.addWidget(btn, row, col)
  # grid_layout.setSpacing(5)
  # grid_layout.setContentsMargins(0,20,20,500)
  col += 1
  if col > 3:
    col = 0
    row += 1

btn_clear.clicked.connect(lambda: calculate("Clear"))
btn_delete.clicked.connect(lambda: calculate("Delete"))
grid_layout.addWidget(btn_clear, 5, 0, 1, 2)
grid_layout.addWidget(btn_delete, 5, 2, 1,2 )
      
main_window.setLayout(grid_layout)

#Run App
main_window.show()
App.exec()