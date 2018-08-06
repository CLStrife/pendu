from random import *
from Letter import *
class Word:

    def __init__(self):
        self.theWord = ['crayon', 'stylo', 'feutre', 'pointe', 'mine', 'gomme', 'dessin', 'coloriage', 'rayure', 'peinture']

    def choiceWord(self):
        return choice(self.theWord)

    def hideWord(self, aWord):
        list_hidden = []
        for i in range(len(aWord)):
            list_hidden.insert(i, '*')
        return list_hidden

    def getHiddenWord(self, aWord, lettre):
        hiddenWord = list()
        for lettre in aWord:
            if lettre in aWord:
                hiddenWord += lettre
            else:
                hiddenWord += "*"
        return hiddenWord

    def checkIsCorrect(self, aWord, aLetter):
        hiddenWord = []
        for i in range(len(aWord)):
            if aLetter == aWord[i]:
                hiddenWord.insert(i, aLetter)

        return hiddenWord

