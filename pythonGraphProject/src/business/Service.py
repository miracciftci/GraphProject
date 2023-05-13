import string
import nltk
from nltk import pos_tag, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def Tokennize(text):   #Tokenization: metnin küçük parçalara ayrılmasıdır.
    words = nltk.word_tokenize(text)
    return words

def Punctuation(text): #Punctuation: Cümledeki noktalama işaretlerinin kaldırılmasıdır.
    clearText = text.translate(str.maketrans('', '', string.punctuation))
    return text

def Ayristir(text):    #Metni cumlelere ayirma
    texts = nltk.sent_tokenize(text)
    return texts

def cumledeNumaricVeriSayisi(text):
    words = nltk.word_tokenize(text)
    taggent_sent = pos_tag(words)
    total = 0

    for i in taggent_sent:
        if (i[1] == 'CD'):
            total+=1
    return total

def cumledeOzelIsimSayisi(text):
    words = nltk.word_tokenize(text)
    taggent_sent = pos_tag(words)
    total = 0

    for i in taggent_sent:
        if (i[1] == 'NNP'):
            total += 1
    return total




text = "Gallery 16 unveils London interactive Jack tree A Christmas tree that can receive text messages has been unveiled at London's Tate Britain art gallery.The spruce has an antenna which can receive Bluetooth texts sent by visitors to the Tate. The messages will be \"unwrapped\" by sculptor Richard Wentworth, who is responsible for decorating the tree with broken plates and light bulbs. It is the 17th year that the gallery has invited an artist to dress their Christmas tree. Artists who have decorated the Tate tree in previous years include Tracey Emin in 2002. The plain green Norway spruce is displayed in the gallery's foyer. Its light bulb adornments are dimmed, ordinary domestic ones joined together with string. The plates decorating the branches will be auctioned off for the children's charity ArtWorks. Wentworth worked as an assistant to sculptor Henry Moore in the late 1960s. His reputation as a sculptor grew in the 1980s, while he has been one of the most influential teachers during the last two decades. Wentworth is also known for his photography of mundane, everyday subjects such as a cigarette packet jammed under the wonky leg of a table."

cumleler = nltk.sent_tokenize(text)  # metni cumlelere ayirma

taggent_sent = pos_tag(Tokennize(text))

