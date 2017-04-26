from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('what-image.png'))
windo.setGeometry(50,50,600,400)

button = QPushButton('Close', windo)
button.resize(200,100)
button.move(50,100)
button.clicked.connect(exit)



windo.show()
app.exec_()