import math
import string
import nltk
from nltk import pos_tag, PorterStemmer
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from rouge import Rouge

from FileInput import Input
from Node import Node


class Service:
    def __init__(self):
        self.number = 1
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

    def Ayristir(self, text):  #Metni cumlelere ayirma
        str = ""
        array = []

        for i in text:
            if(i == "." or i == "!" or i== "?" or i== ":" or i== ";"):
                str += i
                array.append(str.strip())
                str = ""
                continue

            str += i

        return array


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
        service = Service()
        text1 = service.Punctuation(node1.text.lower())
        text2 = service.Punctuation(node2.text.lower())
        words1 = service.Tokennize(text1)
        words2 = service.Tokennize(text2)
        totalText = service.Tokennize(text1)

        for str in words2:
            count = 0
            for wordsText1 in words1:
                if(wordsText1 == str):
                    count = 1
                    break
            if(count == 0):
                totalText.append(str)

        dot1 = []
        dot2 = []

        for str in totalText:
            count = 0
            for w1 in words1:
                if(w1 == str):
                    count = 1
                    break
            dot1.append(count)
            count = 0
            for w2 in words2:
                if (w2 == str):
                    count = 1
                    break
            dot2.append(count)

        up = 0.0
        d1 = 0.0
        d2 = 0.0
        for i in range(len(dot1)):
            up += dot1[i]*dot2[i]
            d1 += dot1[i]
            d2 += dot2[i]

        down = abs(math.sqrt(d2))*abs(math.sqrt(d1))
        point = up/down

        return round(point,3)

    def cumleBenzerligiThresholdunuGecen(self, threshold,node,nodes):   #Cümle benzerliği threshold’unu geçen node’ların bulunması (P3)
        total = 0
        for i in range(len(node.nodeBenzerlikleri)):
            if threshold < node.nodeBenzerlikleri[i]:
                if(nodes[i].nodeBenzerlikleri[node.textNo]>threshold):
                    total += 1
        return total

    def basliktakiKelimelerinOrani(self, node, BaslikCumlesi):    # p4
        service = Service()
        textBaslik = service.Punctuation(BaslikCumlesi.lower())
        baslikWords = service.Tokennize(textBaslik)
        text = service.Punctuation(node.text.lower())
        textWords = service.Tokennize(text)

        count = 0
        for str in baslikWords:
            for word in textWords:
                if(word == str):
                    count += 1

        point = count / len(textWords)
        return point

    def textOzetleme(self, nodes):
        text = ""
        array = []

        for node in nodes:
            array.append(node.textPoint)

        array.sort(reverse=True)
        for i in range(int(len(array)/2)):
            for node in nodes:
                if(node.textPoint == array[i]):
                    text += f"{node.text} "

        return text.strip()

    def textOzetlemeROUGEskoru(self,textOzet,textGercekOzet):    # ROUGE
        rouge = Rouge()
        total = 0
        result = rouge.get_scores(textOzet,textGercekOzet,True)
        array = result['rouge-1']

        for str in array:
            total += array[str]
        score = total/3

        return round(score,7)

    def cumleSkoruHesaplama(self,node,text,thresholdCumleBenzerligi,baslikText,nodes):
        service = Service()
        point = 0.0
        total = len(service.Tokennize(node.text))

        point += service.cumledeNumaricVeriSayisi(node.text) / total  #p1
        point += service.cumledeOzelIsimSayisi(node.text) / total    #p3
        point += service.cumleBenzerligiThresholdunuGecen(thresholdCumleBenzerligi,node,nodes) / (len(node.nodeBenzerlikleri) - 1)  # p3
        point += service.basliktakiKelimelerinOrani(node,baslikText)   #p4
        point += service.cumledeTemaKelimeOrani(text,node)  #p5

        return round(point,2)


