#program to split a list according to first character of word
from itertools import groupby
from operator import itemgetter


word_list = ['bridge','lab','trying','dignity','director','chamber','govandi']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)



