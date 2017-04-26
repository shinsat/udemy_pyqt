from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
windo = QWidget()
windo.setWindowTitle('Hello PyQT')
windo.setWindowIcon(QIcon('what-image.png'))
windo.setGeometry(50,50,600,400)

### (qwidget, title, questoin, controls, defaut value)
message = QMessageBox.question(windo, 'Message box', 'Do you want to exit?', QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

# information, critical, question.warning, about
windo.show()
app.exec_()