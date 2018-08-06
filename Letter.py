class Letter:
    def __init__(self, aLetter):
        self.letter = aLetter

    def checkProposition(self, aLetter):
        if len(self.letter) > 1 or not self.letter.isalpha():
            print("Vous n'avez pas entré un caractère valide")

