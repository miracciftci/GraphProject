import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget,QPushButton,QLineEdit,QInputDialog,QApplication)


class ThresApp(QWidget):
    def __init__(self,form):
        super().__init__(form)
        self.initGUI()

    def initGUI(self):
        self.resize(320,200)
        self.move(100,100)

        btn = QPushButton('Enter Filters', self)
        btn.move(30,30)
        btn.clicked.connect(self.showDialog)

        btn = QPushButton('Model', self)
        btn.move(30,70)
        #btn.clicked.connect()

    def showDialog(self):
        Int,Ifokay = QInputDialog.getDouble(None,'Similarity','Enter number:')
        print(Int)
        print(Ifokay)
        if Ifokay:
            self.showDialog2()
            
    def showDialog2(self):
        Int,Ifokay = QInputDialog.getDouble(None,'Score ','Enter number:')
        print(Int)
        print(Ifokay)




app = QApplication(sys.argv)
Form = QWidget()
ex = ThresApp(Form)
Form.show()
sys.exit(app.exec_())
