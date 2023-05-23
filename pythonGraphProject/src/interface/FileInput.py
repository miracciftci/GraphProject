from PyQt5 import QtWidgets , QtCore , QtGui 
from PyQt5.QtWidgets import QInputDialog , QLineEdit , QFileDialog,QApplication , QWidget 
from PyQt5.QtGui import QIcon




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 350)
        self.Buttonpush = QtWidgets.QPushButton(Form)
        self.Buttonpush.setGeometry(QtCore.QRect(85, 134, 111, 34))
        self.Buttonpush.setStyleSheet("background-color:blue;\n"
                                      "font:bold 15px;\n"
                                      "padding :7px;\n"
                                      "min-width:12px;\n"
                                      "color: white;\n"
                                      "border-radius:12px;\n"
                                      "border-color:blue;\n"                                    
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      
                                      "\n"
                                      "\n"
                                      "")
        self.Buttonpush.setObjectName("Buttonpush")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Buttonpush.setText(_translate("Form", "Browse File"))
        self.Buttonpush.clicked.connect(self.Buttonpush_handler)


    def Buttonpush_handler(self):
        print("Button pressed")
        self.open_dialog_box()
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        filepath = filename[0]
        print(filepath)

        with open(filepath, "r") as file:
            sentences = file.read().split(sep=".")
            print(sentences[0])


if __name__ == "__main__":
    import sys
    application = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(application.exec_())
