# import relevant Moudules to design the GUI
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QMessageBox

from random import choice

words = ["Apple", "Grape", "BOB", "Python", "Banana", "Orange"]
# numbers = [10, 2,5,12,30,45,100]
numbers = range(1, 100)
# App Setting

App = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My First App")
main_window.resize(500,200)

# Create all objects / widgets below here
master_layout = QVBoxLayout()
title_text = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLineEdit()
text3.setPlaceholderText("Type here...")

button1 = QPushButton("Random Numbers")
button2 = QPushButton("Random Words")
button3 = QPushButton("Click Me")

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title_text, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

def random_word1():
  word = choice(numbers)
  text1.setText(str(word))

def random_word2():
  word = choice(words)
  text2.setText(word)

def random_word3():
  # word = choice(words)  
  # text3.setText()
  QMessageBox.information(None, "Info", f"Hello {text3.text()}")

button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)
# Display the window App

main_window.show()
App.exec()