import nltk
from stat_parser import Parser
parser=Parser()
file=open("file.txt","r+")
data=file.read()

sent=nltk.sent_tokenize(data)


for i in sent:
    print "Sentence : ",i,"\n"
    print "POS-Structure : ",parser.parse(i),"\n"
    
