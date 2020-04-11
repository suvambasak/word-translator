import nltk
from stat_parser import Parser

parser=Parser()

s="I go to school."

parser.parse(s)

parser.parse(s).draw()
