from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()

s = QSlider(window)
s.move(330,30)

d = QDial(window)
d.move(30,30)

button = QPushButton(window , text='change Value')
button.move(200,300)

def change_slider_value():
    s.setValue(50)

button.clicked.connect(change_slider_value)

s.valueChanged.connect(d.setValue)
d.valueChanged.connect(s.setValue)

window.show()
app.exec_()