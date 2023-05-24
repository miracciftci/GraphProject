class Node:
    textNo = 0
    text = ""
    textPoint = 0.0        #double
    nodeBenzerlikleri = []


    def __init__(self,textNo,text,textPoint,NodeBenzerlikleri):
        self.textNo = textNo
        self.text = text 
        self.textPoint = textPoint
        self.nodeBenzerlikleri = NodeBenzerlikleri

        