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
    list_number = ["0","1","2","3","4","5","6","7","8","9"]
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
        return 0
    # return mot_index


# def recursif(inpute):
#     liste =list_mot()
#     mot =  recherche_recur(liste)
#     if mot != inpute:
#         return 1+ recursif(inpute)
#     else :
#         return 0



# recherche_recur()


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


# sortir = False
# compte = 0
# while not sortir:
#     index = randint(0, len(ma_liste_mot)-1)
#     mot_index = ma_liste_mot[index]
    
#     print(mot_index)
#     try:
#         if mot_index != inpute:
#             ma_liste_mot.pop(index)
#             compte+=1
#     except:
#         pass

#     else :
#         print(compte)
#         sortir = True 


# list =["a","b","v","h","","5","6","7","8","9"]
# def myst(l: list) -> int:
#     if l==[]:
#         return 0
#     else:          
#         l.pop(0)          # suppression du premier terme de la liste l
#         return 1+myst(l)

# print(myst(list))
        




