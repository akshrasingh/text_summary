import nltk
from nltk.corpus import stopwords
# stopwords words like he she
from nltk.tokenize import word_tokenize, sent_tokenize
# word for converting sentence to word
# sent for converting text  to sentence
from string import punctuation
from nltk.stem.snowball import SnowballStemmer

nltk.download('stopwords')
nltk.download('punkt')


class Summary:
    stem_word = SnowballStemmer("english")
    stop_word = set(stopwords.words("english") + list(punctuation))
    text = ""
    sentence = ""

    def word_con(self):
        words = word_tokenize(self.text)
        print("the words  in the text are displayed in a list as -")
        print(words)
        return words

    def input(self):

        self.text = input("enter the text you want to summarise\n ")

    def frequency(self,words):
        freq_count=dict()
        for i in words:
             i = i.lower()
             if i in self.stop_word:
                 continue
             if i in freq_count:
                 freq_count[i]+=1
             else:
                 freq_count[i]=1
        return  freq_count
    def compute(self,freq_count):
        self.sentence = sent_tokenize(self.text)
        sentence_dict = dict()
        for i in self.sentence:
            for j, k in enumerate(freq_count, start=1):
                # j stores values 1,2 ; k stores each word

                for k in i.lower():
                    if i in sentence_dict:
                        sentence_dict[i] = sentence_dict[i]+1
                    else:
                        sentence_dict[i] = j
        print(sentence_dict)
        return sentence_dict
    def average(self,sentence_dict):
        sum=0
        for i in sentence_dict:
            sum = sum+sentence_dict[i]
        avg = int(sum/len(sentence_dict))
        return avg
    def print_text(self,sentence_dict ,avg):
        summary=""
        for j in self.sentence:
            if (j in sentence_dict) and (sentence_dict[j]>(avg)):
                summary +=" " + j
        print(summary)
        return summary


aa = Summary()
aa.input()
a_word = aa.word_con()
a_frequency = aa.frequency(a_word)
a_sentence = aa.compute(a_frequency)
averagee = aa.average(a_sentence)
final= aa.print_text(a_sentence, averagee)

print("Final summary is:\n\n")
print("------------------------------")
print("------------------------------")
print(final)
print("------------------------------")
print("------------------------------")


