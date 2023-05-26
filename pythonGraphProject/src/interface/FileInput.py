from PyQt5 import QtWidgets , QtCore , QtGui 
from PyQt5.QtWidgets import QInputDialog , QLineEdit , QFileDialog,QApplication , QWidget, QMainWindow
from PyQt5.QtGui import QIcon
import networkx as nx
import matplotlib.pyplot as plt
import Service as sc
from Node import Node


class Input:
    text = ""
    textBaslik = ""
    textOzet = ""
    cumleBenzerlikTreshold = 0
    cumleSkorTreshold = 0
    nodes = []


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
        self.Buttonpush2.clicked.connect(self.Buttonpush_handler2)
    
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
            Input.textOzet = file.readlines()[0]
    
    def open_dialog_box_model(self):
        self.doldur()
        self.saveToFile()
        self.getGraph()
    
    def open_dialog_box_treshold(self):
        def showDialog():
            Int,Ifokay = QInputDialog.getDouble(None,'Similarity','Enter number:',decimals=3)
            Input.cumleBenzerlikTreshold = Int
            if Ifokay:
                showDialog2()
            
        def showDialog2():
            Int,Ifokay = QInputDialog.getDouble(None,'Score ','Enter number:',decimals=3)
            Input.cumleSkorTreshold = Int
        showDialog()
    
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        filepath = filename[0]

        with open(filepath, "r") as file:
            Input.textBaslik = file.readline().strip()
            Input.text = file.read().strip()

    def getGraph(self):
        G = nx.Graph()
        service = sc.Service()
        for i in Input.nodes:
            treshold_gecen_sayisi = service.cumleBenzerligiThresholdunuGecen(Input.cumleBenzerlikTreshold,i,Input.nodes)
            G.add_node(i.textNo,score = i.textPoint,amount = (treshold_gecen_sayisi-1)),

        for i in Input.nodes:
            for k in Input.nodes:
                if k.textNo>i.textNo:
                        if Input.cumleBenzerlikTreshold >= i.nodeBenzerlikleri[Input.nodes.index(k)]:
                            G.add_edge(i.textNo,k.textNo,color = 'red',edge_value = i.nodeBenzerlikleri[Input.nodes.index(k)])
                        else:
                            G.add_edge(i.textNo,k.textNo,color = 'blue',edge_value = i.nodeBenzerlikleri[Input.nodes.index(k)])

        pos = nx.fruchterman_reingold_layout(G)
        colors = nx.get_edge_attributes(G,'color').values()
        edge_values = {(f,s):d["edge_value"] for f,s,d in G.edges(data=True)}
        # for f,s in G.nodes(data=True):
        #    if len(s) != 0:
        #         print(f"s printing {s['score']}")
        node_values = {f:s for f,s in G.nodes(data=True)}
        new_node_values={}
        for i in node_values:
            if len(node_values[i]) != 0:
                new_node_values[i] = node_values[i]['score']

        labels = nx.get_node_attributes(G,'score')
        pos_higher = self.getHigherPos(pos,0.12)
        colorMap = ['lightgrey' if node.textPoint < Input.cumleSkorTreshold else 'lightgreen' for node in Input.nodes]
        nx.draw(G,pos,edge_color = colors,node_color = colorMap ,with_labels=True, node_size=300,edgecolors='black')
        nx.draw_networkx_labels(G,pos=pos_higher , labels = node_values,font_color = "purple",font_size = 12)
        nx.draw_networkx_edge_labels(G,pos = pos,edge_labels = edge_values, label_pos = 0.3)
        plt.margins(0.2)
        figureManager = plt.get_current_fig_manager()
        figureManager.window.showMaximized()
        plt.show()
        
    def doldur(self):
        service = sc.Service()
        cumleler = service.Ayristir(Input.text)
        for i in range(len(cumleler)):
            node = Node()
            node.textNo = i
            node.text = cumleler[i]
            node.nodeBenzerlikleri = []
            Input.nodes.append(node)

        for node in Input.nodes:
            for i in range(len(Input.nodes)):
                node.nodeBenzerlikleri.append(service.cumleBenzerligiHesaplama(node, Input.nodes[i]))

        for node in Input.nodes:
            print(f"{node.textNo}) puan = {node.textPoint} - {node.text}")
            node.textPoint = service.cumleSkoruHesaplama(node, Input.text, Input.cumleBenzerlikTreshold, Input.textBaslik,Input.nodes)

        for node in Input.nodes:
            print(f"{node.textNo}) puan = {node.textPoint} - {node.text}")

    def saveToFile(self):
        service = sc.Service()
        ozet = service.textOzetleme(Input.nodes)
        rougeSkoru = service.textOzetlemeROUGEskoru(ozet, Input.textOzet)
        f = open("metinOzeti.txt", "w")
        f.write("Metin Ozeti ;\n")
        f.write(ozet)
        f.write(f"\n\nROUGE benzerlik skoru: {rougeSkoru}")
        f.close()

        file = open("cumleler.txt", "w")
        for node in Input.nodes:
            file.write(f"{node.textNo} - {node.text}\n")
        file.close()

    def getHigherPos(self,pos,shiftY):
        pos_higher = {}
        for k, v in pos.items():
            if v[1]<0:
                pos_higher[k] = (v[0], v[1]-shiftY)
            else:
                pos_higher[k] = (v[0], v[1]+shiftY)
            
        return pos_higher


if __name__ == "__main__":
    import sys
    application = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(application.exec_())
