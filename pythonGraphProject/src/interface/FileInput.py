from PyQt5 import QtWidgets , QtCore , QtGui 
from PyQt5.QtWidgets import QInputDialog , QLineEdit , QFileDialog,QApplication , QWidget, QMainWindow
from PyQt5.QtGui import QIcon

import networkx as nx
import matplotlib.pyplot as plt
from Node import Node

     

class Input:
    text = ""
    textBaslik = ""
    textOzet = ""
    cumleBenzerlikTreshold = 0
    cumleSkorTreshold = 0


class Ui_Form(QMainWindow):
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
        self.ButtonpushTreshold = QtWidgets.QPushButton(Form)
        self.ButtonpushTreshold.setGeometry(QtCore.QRect(280, 130, 180, 34))
        self.ButtonpushTreshold.setStyleSheet("background-color:blue;\n"
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
        self.ButtonpushTreshold.setObjectName("ButtonpushTreshold")
        self.retranslateUi(Form)
        self.retranslateUi2(Form)
        self.retranslateUiConnect(Form)
        self.retranslateUiTreshold(Form)
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
    
    def retranslateUiTreshold(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonpushTreshold.setText(_translate("Form", "Select Treshold"))
        self.ButtonpushTreshold.clicked.connect(self.Buttonpush_handlerTreshold)


    def Buttonpush_handler(self):
        print("Button pressed")
        self.open_dialog_box()
    
    def Buttonpush_handler2(self):
        print("Button pressed")
        self.open_dialog_box2()

    def Buttonpush_handlerModel(self):
        print("Button pressed")
        self.open_dialog_box_model()
    
    def Buttonpush_handlerTreshold(self):
        print("Button pressed")
        self.open_dialog_box_treshold()
    
    def open_dialog_box2(self):
        filename2 = QFileDialog.getOpenFileName()
        filepath2 = filename2[0]

        with open(filepath2, "r") as file:
            Input.textOzet = file.readlines()
    
    def open_dialog_box_model(self):
        self.getGraph()
    
    def open_dialog_box_treshold(self):
        def showDialog():
            Int,Ifokay = QInputDialog.getDouble(None,'Similarity','Enter number:')
            print(Int)
            print(Ifokay)
            if Ifokay:
                showDialog2()
            
        def showDialog2():
            Int,Ifokay = QInputDialog.getDouble(None,'Score ','Enter number:')
            print(Int)
            print(Ifokay)
        showDialog()
    
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        filepath = filename[0]

        with open(filepath, "r") as file:
            Input.textBaslik = file.readline().strip()
            Input.text = file.read().strip()

    def getGraph(self):
        nodes = []
        nodes.append(Node(1,"first","3.4",[1,2]))
        nodes.append(Node(2,"second","3.5",[1,2]))
        nodes.append(Node(3,"third","3.6",[1,2]))
        nodes.append(Node(4,"forth","3.7",[1,2]))
        G = nx.Graph()
        for i in nodes:
            G.add_node(i.textNo,size = i.textPoint)
            if i.textNo != 4:
                G.add_edge(i.textNo,i.textNo+1,color = 'r',edge_value = 0.5)
            else:
                G.add_edge(4,1,color='r',edge_value = 0.5)
            
            pos = nx.circular_layout(G)
            colors = nx.get_edge_attributes(G,'color').values()
            edge_values = {(f,s):d["edge_value"] for f,s,d in G.edges(data=True)}
            # for f,s in G.nodes(data=True):
            #    if len(s) != 0:
            #         print(f"s printing {s['size']}")
            node_values = {f:s for f,s in G.nodes(data=True)}
            new_node_values={}
            for i in node_values:
                if len(node_values[i]) != 0:
                    #print(f" i  ==  {node_values[i]['size']}")
                    new_node_values[i] = node_values[i]['size']
            print(new_node_values)         
            #print(node_values)

            #G.add_edge(6,1)
        labels = nx.get_node_attributes(G,'size')
        #pos_higher = getPosHigher(pos)
        nx.draw(G,pos,edge_color = colors,node_color = 'lightgreen' ,with_labels=True)
        nx.draw_networkx_labels(G,pos=pos , labels = node_values,font_color = "blue",font_size = 12)
        nx.draw_networkx_edge_labels(G,pos = pos,edge_labels = edge_values, label_pos = 0.5)
        plt.margins(0.2)
        plt.show()
        




if __name__ == "__main__":
    import sys
    application = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(application.exec_())
