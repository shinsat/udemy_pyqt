from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('what-image.png'))

#windo.resize(600,400)
#windo.move(50,50)

#windo.setGeometry((move)()resize)
windo.setGeometry(50,50,600,400)

windo.show()
app.exec_()