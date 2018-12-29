import nltk
import codecs

##s="and Commission not Council"
s=raw_input('Enter TEXT [english] : ')
s1=s.lower()
s2=s1.split(" ")
##print s2

f=codecs.open("ex1-file","r",encoding="utf-8").read()
f1=f.split("\n")

print ("SPANISH : ",)
for j in range (len(s2)):
    c=0
    for i in range (len(f1)):
        f2=f1[i].split("\t")
        if s2[j]==f2[0]:
            print (f2[1]," ",)
            c=c+1
            break
    if c==0:
        print (s2[j],"",)
    
