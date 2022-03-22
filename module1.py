# Créé par lhertho, le 17/03/2022 en Python 3.7
A=float(input("Le joueur a participé a combien de partie ?"))
B=input("Est-ce que le joueur a affronté plusieurs adversaires différents ? (répondre par : oui ou non)")
C=input("Est-ce que vous avez strictement plus de victoires que de défaites ? (répondre par : oui ou non)")


def Bonus(A,B,C):
    if A >= 20:
        A = True
    elif A < 20:
        A = False
    if B == 'oui':
        B = True
    elif B == 'non':
        B = False
    if C == 'oui':
        C = True
    elif C == 'non':
        C = False


    print(A, B, C)

    if (A == True and B == True  ) or (B == False and C == True) or (C == False and A == True): #Condition Booléenne
        reponse = "Le joueur peut obtenir un bonus"
    else:
        reponse = "Le joueur ne peut pas obtenir un bonus"
    return reponse



print(Bonus(A,B,C))