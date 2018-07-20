from random import *
from function import *

word = "qqchose"
hidden_word = '*'
letter = str
'''word = liste-mot[randrange]'''
i=0
y=0
mistake = 8
tried_letter = 0

for i in range(len(word)):
    print(hidden_word, end='')
    i = i+1
    
letter = input("\nVeuillez saisir une proposition: ")
while tried_letter < 8:
    tried_letter = tried_letter +1
    check_letter_len(letter)
    enter_proposition()
    print(tried_letter)
