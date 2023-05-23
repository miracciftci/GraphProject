
import networkx as nx
import matplotlib.pyplot as plt
from Node import Node



word = Node(1,"first","3.4",[1,2])

sentences = []
sentences.append(word)
sentences.append(Node(2,"second","3.5",[1,2]))
sentences.append(Node(3,"third","3.6",[1,2]))
sentences.append(Node(4,"forth","3.7",[1,2]))


posNodeAtt = {
    1:(-0.2,5),
    2:(4.5,7.5),
    3:(2.4,1.4),
    4:(5.8,2.5)
}

nodeLabels = []
if __name__ == "__main__":
    K33 = nx.Graph()
    for i in sentences:
        K33.add_node(i.textNo,size = i.textPoint)
        if i.textNo != 4:
            K33.add_edge(i.textNo,i.textNo+1,weight = 1)
        else:
            K33.add_edge(4,1,weight = 1)
        nodeLabels.append(i.textPoint)
        #K33.add_edge(6,1)
    labels = nx.get_node_attributes(K33,'size')
    nx.draw(K33,with_labels=True)
    #nx.draw_networkx_labels(K33,pos = posNodeAtt,labels = labels)
    plt.show()