from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)

p = QPushButton(window , text='Welcome')
#p.move(200,200)
p.setGeometry(150 , 150 , 80 , 40)


window.show()
app.exec_()