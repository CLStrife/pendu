from donnees import *


def hide_word(word):
    for i in range(len(word)):
        list_hidden[i] = '*'
        
def play_again():
    answer = input("Voulez vous rejouer?: ")
    if answer == 'y':
        pendu()
    elif answer == 'n':
        print("Au revoir")
        exit()
        
def check_letter(letter):
    global tried
    for i in range(len(word)):
        if letter == list_word[i]:
            list_hidden[i] = letter
    print(list_hidden, end='') 
    if list_hidden == list_word:
        print("\nBravo! Vous avez trouvé!!")           
        play_again()

        
def pendu():
    letter = input("\nVeuillez saisir une proposition: ")

    check_letter_len(letter)
        
def check_letter_len(letter):
    global tried
        
    hide_word(word)
    
    while tried < 8:

        check_letter(letter)      
        
        if len(letter) > 1:
            print("Pas plus d'une proposition")
        elif letter == '':
            print("Veuillez entrer au moins une lettre")
            
        elif letter not in list_word:
            print("\nVous avez fait une erreur")
            tried = tried +1
            
        print(tried)
        letter = input("\nVeuillez saisir une nouvelle proposition: ")
        
        if tried == 8:
            print("Vous avez perdu")
    
      
