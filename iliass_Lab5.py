"""
Iliass Amaich
Laboratoire 5
Session été 2022

"""
from msvcrt import kbhit
from random import randint
from re import T
def verifier_mot(mot):
    list_number = ["0","1","2","3","4","5","6","7","8","9"]
    for lettre in mot:
        if lettre in list_number:
            return True

def list_mot():
    list_mot = []
    sortir = False
    while not sortir:
        try:
            mot = input("Saisir un mot : ")
            if verifier_mot(mot):
                raise Exception
        except:
            sortir = True
        else:
            list_mot.append(mot)
    return list_mot

def recherche_recur(inpute, ma_liste_mot):
    index = randint(0, len(ma_liste_mot)-1)
    mot_index = ma_liste_mot[index]
    if mot_index != inpute:
        return 1+ recherche_recur(inpute, ma_liste_mot)
    else :
        return 1

def recherche_mot():
    ma_liste_mot = list_mot()
    sortir = False
    while not sortir:
        try:
            inpute = input("Saisir un mot present dans la liste: ")
            if inpute not in ma_liste_mot:
                    raise Exception

        except:
            print("Le mot saisi n'est pas dans la liste !!")

        else:
            print(recherche_recur(inpute,ma_liste_mot))
            sortir = True
    

recherche_mot()

