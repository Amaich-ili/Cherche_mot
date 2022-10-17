"""
Iliass Amaich
Laboratoire 5
Session été 2022

"""
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
    print(list_mot)
    
    return list_mot
# list_mot()

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
            # je doit ajouter le comteur ici
            sortir = True
    
    
    return inpute
recherche_mot()



            




