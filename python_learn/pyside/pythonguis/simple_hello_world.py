# Source: https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

import sys

app = QApplication(sys.argv)

#window = QWidget()
#window = QPushButton("Push Me")
window = QMainWindow()
window.show()

app.exec_()
