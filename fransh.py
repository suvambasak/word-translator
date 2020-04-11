# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:16:51 2015

@author: suvam
"""

import nltk
from stat_parser import Parser

parser=Parser()

string= raw_input('Enter the text : ')

print (parser.parse(string))