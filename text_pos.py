import nltk
from stat_parser import Parser
parser=Parser()
file=open("file.txt","r+")
p=open("parsetree","w")
data=file.read()

sent=nltk.sent_tokenize(data)


for i in sent:
    p.write("Sentence : "+str(i)+"\n")
    p.write("Structure : "+str(parser.parse(i))+"\n")
    p.write("\n")

p.close()
    
