"""
Iliass Amaich
Laboratoire 5
Session été 2022

"""
list_str = []
list_number = [0,1,2,3,4,5,6,7,8,9]
# c = 0
# while c < 5:
#     c += 1

def mot():
    list_number = [0,1,2,3,4,5,6,7,8,9]
    mot = input("Saisir un mot : ")
    for lettre in mot :
        if lettre in list_number:
            return False
    return mot

c = 0
while c < 5:
    if mot():
        list_str.append(mot())
    c += 1
print(list_str)
   



            




