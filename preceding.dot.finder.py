# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:10:40 2015

@author: root
"""
import nltk
f=open("train.en","r")
s=f.read()
a=s.split("\n")
for i in range (len(a)):
    b=nltk.word_tokenize(a[i])
    if "." in b[0]:
        print i