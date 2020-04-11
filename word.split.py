import nltk
import re
import codecs
f=codecs.open("/home/suvam/es-en/europarl-v7.es-en.en","r",encoding="utf-8").read()
p=codecs.open("/home/suvam/TreeTagger/corpus.tok.en","w",encoding="utf-8")
s=f.split("\n")
for i in range (0,150000):
    b=nltk.word_tokenize(s[i])
    for j in range (len(b)):
        p.write(b[j]+"\n")
    p.write("<>\n")
    
p.close()
