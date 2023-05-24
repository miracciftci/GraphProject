from PyQt5 import QtWidgets , QtCore , QtGui 
from PyQt5.QtWidgets import QInputDialog , QLineEdit , QFileDialog,QApplication , QWidget 
from PyQt5.QtGui import QIcon

class Input:
    text = ""
    textBaslik = ""
    textOzet = ""


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 350)
        self.Buttonpush = QtWidgets.QPushButton(Form)
        self.Buttonpush.setGeometry(QtCore.QRect(85, 130, 180, 34))
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
        self.Buttonpush2 = QtWidgets.QPushButton(Form)
        self.Buttonpush2.setGeometry(QtCore.QRect(85, 190, 180, 34))
        self.Buttonpush2.setStyleSheet("background-color:blue;\n"
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
        self.Buttonpush2.setObjectName("Buttonpush2")
        self.ButtonpushConnect = QtWidgets.QPushButton(Form)
        self.ButtonpushConnect.setGeometry(QtCore.QRect(260, 250, 180, 34))
        self.ButtonpushConnect.setStyleSheet("background-color:black;\n"
                                      "font:bold 18px;\n"
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
        self.ButtonpushConnect.setObjectName("ButtonpushConnect")
        self.retranslateUi(Form)
        self.retranslateUi2(Form)
        self.retranslateUiConnect(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Buttonpush.setText(_translate("Form", "Browse File"))
        self.Buttonpush.clicked.connect(self.Buttonpush_handler)
    
    def retranslateUi2(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Buttonpush2.setText(_translate("Form", "Browse Summary File"))
        self.Buttonpush2.clicked.connect(self.Buttonpush_handler)
    
    def retranslateUiConnect(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonpushConnect.setText(_translate("Form", "Model"))
        self.ButtonpushConnect.clicked.connect(self.Buttonpush_handlerModel)


    def Buttonpush_handler(self):
        print("Button pressed")
        self.open_dialog_box()
    
    def Buttonpush_handler2(self):
        print("Button pressed")
        self.open_dialog_box2()

    def Buttonpush_handlerModel(self):
        print("Button pressed")
        self.open_dialog_box_model()
    
    def open_dialog_box2(self):
        filename2 = QFileDialog.getOpenFileName()
        filepath2 = filename2[0]

        with open(filepath2, "r") as file:
            Input.textOzet = file.readlines()
    
    def open_dialog_box_model(self):
        print("modelling")
    
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        filepath = filename[0]

        with open(filepath, "r") as file:
            Input.textBaslik = file.readline().strip()
            Input.text = file.read().strip()



if __name__ == "__main__":
    import sys
    application = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(application.exec_())
