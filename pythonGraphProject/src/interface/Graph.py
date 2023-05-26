
import networkx as nx
import matplotlib.pyplot as plt
from GraphProject.pythonGraphProject.src.interface.Node import Node



nodes = []
nodes.append(Node(1,"first","3.4",[1,2]))
nodes.append(Node(2,"second","3.5",[1,2]))
nodes.append(Node(3,"third","3.6",[1,2]))
nodes.append(Node(4,"forth","3.7",[1,2]))


def getPosHigher(pos):
    pos_higher = []
    for k,v in pos.items():
        if(v[1]>0):
            pos_higher[k] = (v[0]-0.1,v[1]+0.1)
        else:
            pos_higher[k] = (v[0]-0.1,v[1]-0.1)
    return pos_higher


if __name__ == "__main__":
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



            
