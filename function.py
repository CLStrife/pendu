def enter_proposition():
    letter = input("\nVeuillez saisir une proposition: ")
    
def check_letter_len(letter):
    if len(letter) > 0:
        print("Pas plus d'une proposition")
    elif len(letter) < 0:
        print("Veuillez entrer au moins une lettre")
    else:
        print("Veuillez faire une nouvelle proposition")
        


        
'''def check_letter(letter):
    i=0
    while letter != word[i]:
        i = i+1
    if letter == word[i]:
        '''
        
    
