from src.business.Service import Service
from src.interface.FileInput import Input
from src.model.Node import Node

text = "A Christmas tree that can receive text messages has been unveiled at London's Tate Britain art gallery. The spruce has an antenna which can receive Bluetooth texts sent by visitors to the Tate. The messages will be \"unwrapped\" by sculptor Richard Wentworth, who is responsible for decorating the tree with broken plates and light bulbs. It is the 17th year that the gallery has invited an artist to dress their Christmas tree. Artists who have decorated the Tate tree in previous years include Tracey Emin in 2002.The plain green Norway spruce is displayed in the gallery's foyer. Its light bulb adornments are dimmed, ordinary domestic ones joined together with string. The plates decorating the branches will be auctioned off for the children's charity ArtWorks. Wentworth worked as an assistant to sculptor Henry Moore in the late 1960s. His reputation as a sculptor grew in the 1980s, while he has been one of the most influential teachers during the last two decades. Wentworth is also known for his photography of mundane, everyday subjects such as a cigarette packet jammed under the wonky leg of a table."
baslikText = "Gallery unveils interactive tree"
textOzet = "The messages will be \"unwrapped\" by sculptor Richard Wentworth, who is responsible for decorating the tree with broken plates and light bulbs.A Christmas tree that can receive text messages has been unveiled at London's Tate Britain art gallery.It is the 17th year that the gallery has invited an artist to dress their Christmas tree.The spruce has an antenna which can receive Bluetooth texts sent by visitors to the Tate.His reputation as a sculptor grew in the 1980s, while he has been one of the most influential teachers during the last two decades."

service = Service()
cumleler = service.Ayristir(text)  # metni cumlelere ayirma

#cumle benzerligi thresholdu = 0.5
nodes = []

for i in range(len(cumleler)):
    node = Node()
    node.textNo = i
    node.text = cumleler[i]
    node.nodeBenzerlikleri = []
    nodes.append(node)

for node in nodes:
    node.textPoint = service.cumleSkoruHesaplama(node,text, 0.5,baslikText)
    for i in range(len(nodes)):
        node.nodeBenzerlikleri.append(service.cumleBenzerligiHesaplama(node,nodes[i]))

'''
for node in nodes:
    print(f"{node.textNo}) puan = {node.textPoint} - {node.text}")
    for i in range(len(node.nodeBenzerlikleri)):
        print(f"{node.textNo} cumle - {i} cumle benzerligi =  {node.nodeBenzerlikleri[i]}")
'''


Ozet = service.textOzetleme(nodes)
rougeBenzerlikSkoru = service.textOzetlemeROUGEskoru(Ozet,textOzet)




