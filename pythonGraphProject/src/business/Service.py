import string
import nltk
from nltk import pos_tag, PorterStemmer
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

from src.model.Node import Node


class Service:
    def Stemming(self,text):  #Stemming: kelimelerin kökünü bulma
        ps = PorterStemmer()
        words = nltk.word_tokenize(text)
        resposText = ""
        for w in words:
            resposText += f"{ps.stem(w)} "

        return resposText.strip()

    def stopWords(self,text):    #StopWords: stopWords kelimelerin temizlenmesi
        stopWords = set(stopwords.words('english'))
        words = nltk.word_tokenize(text.lower())
        wordsFiltered = ""
        for w in words:
            if w not in stopWords:
                wordsFiltered += f"{w} "

        return wordsFiltered.strip()

    def Tokennize(self, text):   #Tokenization: metnin küçük parçalara ayrılmasıdır.
        words = nltk.word_tokenize(text)
        return words

    def Punctuation(self, text): #Punctuation: Cümledeki noktalama işaretlerinin kaldırılmasıdır.
        clearText = text.translate(str.maketrans('', '', string.punctuation))
        return clearText

    def Ayristir(self, text):    #Metni cumlelere ayirma
        texts = nltk.sent_tokenize(text)
        return texts

    def cumledeNumaricVeriSayisi(self, text):
        words = nltk.word_tokenize(text)
        taggent_sent = pos_tag(words)
        total = 0
        for i in taggent_sent:
            if (i[1] == 'CD'):
                total+=1
        return total

    def cumledeOzelIsimSayisi(self, text):
        words = nltk.word_tokenize(text)
        taggent_sent = pos_tag(words)
        total = 0

        for i in taggent_sent:
            if (i[1] == 'NNP'):
                total += 1
        return total

    def temaKelimeler(self, text):
        service = Service()
        text = service.Punctuation(text)
        text = service.stopWords(text)
        words = service.Tokennize(text)

        num = len(words) / 10
        fd = nltk.FreqDist(words)
        words = fd.most_common(int(num))
        array = []
        for i in words:
            array.append(i[0])

        return array

    def cumledeTemaKelimeOrani(self,text,node):
        total = 0
        service = Service()
        cumle = service.Punctuation(node.text)
        cumle = service.stopWords(cumle)
        words = service.Tokennize(cumle)
        temaText = service.temaKelimeler(text)

        for i in words:
            for tema in temaText:
                if(i==tema):
                    total+=1

        result = total / len(words)
        return result

    def cumleBenzerligiHesaplama(self, node1,node2):  #kosinus benzerliği
        point = 0.0
        service = Service()
        text1 = service.Punctuation(node1.text.lower())
        text2 = service.Punctuation(node2.text.lower())
        totalText = service.Tokennize(text1)
        array = totalText

        for str in service.Tokennize(text2):
            count = 0
            for wordsText1 in array:
                if(wordsText1 == str):
                    count = 1
                    break
            if(count == 0):
                totalText.append(str)

        dot1 = []
        dot2 = []

        for str in totalText:

        return point

    def cumleBenzerligiThresholdunuGecen(self, threshold,nodes):   #Cümle benzerliği threshold’unu geçen node’ların bulunması (P3)
        total = 0
        for node in nodes:
            if threshold < node.anlamBenzerligi:
                total += 1
        return threshold

    def cumleSkoruHesaplama(self,node,text,thresholdCumleBenzerligi):
        service = Service()
        point = 0.0
        total = len(service.Tokennize(node.text))

        point += service.cumledeNumaricVeriSayisi(node.text) / total  #p1
        point += service.cumledeOzelIsimSayisi(node.text) / total    #p2
        # ön işlemler
        metin = service.Punctuation(node.text)
        metin = service.stopWords(metin)
        metin = service.Stemming(metin)
        point += service.cumleBenzerligiThresholdunuGecen(thresholdCumleBenzerligi,node.nodes) / (len(node.nodes) - 1)  # p3
        # p4
        point += service.cumledeTemaKelimeOrani(text,node)  #p5

        return round(point,2)


