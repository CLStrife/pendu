from Word import *

chance = 0
toContinue = 'o'

while toContinue != 'n':

    a = Word()
    hiddenWord = list(a.choiceWord())
    hi = a.hideWord(list(hiddenWord))
    print(hi)
    letters = []
    answer = list("")
    i = 0

    while chance < 8 and hi != hiddenWord:

        b = Letter(input("Veuillez entrer une proposition:\n"))
        essai = b.letter
        if len(b.letter) > 1 or not essai.isalpha():
            print("Entrée invalide")

        elif essai not in hiddenWord:
            print("L'entrée n'est pas valide")
            chance = chance +1

        for i in range(len(hiddenWord)):
            if b.letter == hiddenWord[i]:
                hi[i] = b.letter
        print(hi)
        print(chance)
        if hi == hiddenWord:
            print("Bravo")
            toContinue = input("Voulez-vous rejouer?: (O/N)\n")

