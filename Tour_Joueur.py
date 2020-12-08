#La pioche
from random import*

#creer un dictioner avec le nombre et le valeur de chaque lettre OUI
def init_dico ():                        
    dico={"A":{"occ":9 , "val":1},
       "B":{"occ":2 , "val":3},
       "C":{"occ":2 , "val":3},
       "D":{"occ":3 , "val":2},
       "E":{"occ":15 , "val":1},
       "F":{"occ":2 , "val":4},
       "G":{"occ":2 , "val":2},
       "H":{"occ":2 , "val":4},
       "I":{"occ":8 , "val":1},
       "J":{"occ":1 , "val":8},
       "K":{"occ":1 , "val":10},
       "L":{"occ":5 , "val":1},
       "M":{"occ":3 , "val":2},
       "N":{"occ":6 , "val":1},
          
       "O":{"occ":6 , "val":1},
       "P":{"occ":2 , "val":3},
       "Q":{"occ":1 , "val":8},
       "R":{"occ":6 , "val":1},
       "S":{"occ":6 , "val":1},
       "T":{"occ":6 , "val":1},
       "U":{"occ":6 , "val":1},
       "V":{"occ":2 , "val":4},
       "W":{"occ":1 , "val":10},
       "X":{"occ":1 , "val":10},
       "Y":{"occ":1 , "val":10},
       "Z":{"occ":1 , "val":10},
       "?":{"occ":2 , "val":0}}
    return dico

#creer une liste avec toutes les lettres  OUI
def init_pioche(dico):
    sac=[]
    for lettre in dico :
        for i in range (dico[lettre]["occ"]):
            sac.append(lettre)
    return sac

#prendre x jetons de la pioche OUI
def piocher(x,sac):
    main=[]
    for i in range (x):
        lt=randint(0,len(sac)-1)
        main.append(sac[lt])
        sac.pop(lt)
    return main

#completer la main pour avoir 7 jetons  OUI
def completer_main(main,sac):
    reste=7-len(main)
    if(len(sac)<=reste):
        reste=len(sac)
        main.extend(piocher(reste,sac))
    else:
        reste=7-len(main)
        main.extend(piocher(reste,sac))
    return main

#creer une liste avec les jetons qu'on veut echanger  OUI
def jetons_change(main):
    jetons=[]
    nb=int(input("Nombre de lettres a échanger: "))
    for i in range (nb):
        lt=input("Lettre a échanger: ").upper()
        if (lt in main):
            jetons.append(lt)
    return jetons




#Plateau de jeu
    #creer une liste de listes de 15 ligne et 15 colonnes OUI
def init_jetons():
    plateau=[]
    for i in range(15):
        plateau.append(15*["  "])
    return plateau

    #afficher chaque bonus dans sa position correspondante OUI
def init_bonus():
    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
        
    plateauBonus=init_jetons()
    ligne=0
    for ligne in range(0,15,1):
        cologne=0
        for cologne in range(0,15,1):
            position=[ligne,cologne]
            
            if (position in cases_MT):
                plateauBonus[ligne][cologne]="MT"
            elif (position in cases_MD):
                plateauBonus[ligne][cologne]="MD"
            elif (position in cases_LT):
                plateauBonus[ligne][cologne]="LT"
            elif (position in cases_LD):
                plateauBonus[ligne][cologne]="LD"
    return plateauBonus
    

    #afficher le jeton dans la position choisit OUI
def affichage_jetons(ligne,cologne,plateau,lettre):
    if(plateau[ligne][cologne]=="MT"):
        plateau[ligne][cologne]=lettre+"#"
    elif(plateau[ligne][cologne]=="MD"):
        plateau[ligne][cologne]=lettre+"*"
    elif(plateau[ligne][cologne]=="LD"):
        plateau[ligne][cologne]=lettre+"^"
    elif(plateau[ligne][cologne]=="LT"):
        plateau[ligne][cologne]=lettre+"+"
    else:
        plateau[ligne][cologne]=lettre+" "
    return plateau

#avec les coordones et la direction voir si le mot peut se placer en tenant en compte les lettres deja posés sur le plateau
def tester_placement(plateau,i,j,dire,mot):
    lettres=[]
    if(dire=="h"):
        if(len(mot)<=(15-j)):
            for lt in mot:
                if(plateau[i][j]==lt):
                    j+=1
                elif(plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD"):
                    j+=1
                    lettres.append(lt)
                elif(plateau[i][j]!=lt):
                    lettres=[]
                    return lettres
        else:
            return lettres
        return lettres
               
    elif(dire=="v"):
        if(len(mot)<=(15-i)):
            for lt in mot:
                if(plateau[i][j]==lt):
                    i+=1
                elif(plateau[i][j]=="" or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD"):
                    i+=1
                    lettres.append(lt)
                elif(plateau[i][j]!=lt):
                    lettres=[]
                    return lettres
        else:
            return lettres
        return lettres

def placer_mot(plateau,main,mot,i,j,dire):
    test=tester_placement(plateau,i,j,dire,mot)
    if(test==[]):
        return False
    else:
        if(dire=="h"):
            for lt in mot:
                affichage_jetons(i,j,plateau,lt)
                j+=1
        elif(dire=="v"):
            for lt in mot:
                affichage_jetons(i,j,plateau,lt)
                i+=1
        for lt in test:   
            main.remove(lt)
        return plateau

#changer x jetons de la main par x jetons de la pioche OUI
def echanger(jetons,main,sac):
    if(len(sac)>=7):
        for i in range(len(jetons)):
            y=main.index(jetons[i])
            lt=main.pop(y)
            sac.append(lt)
        main=completer_main(main,sac)
    else:
        print("Il n'y a pas suffisamment des jetons dans le sac")
    return main




   #prendre x jetons de la pioche OUI
def piocher(x,sac):
    main=[]
    for i in range (x):
        lt=randint(0,len(sac)-1)
        main.append(sac[lt])
        sac.pop(lt)
    return main    
        



#creer une liste avec les jetons qu'on veut echanger  OUI
def jetons_change(main):
    jetons=[]
    nb=int(input("Nombre de lettres a échanger: "))
    for i in range (nb):
        lt=input("Lettre a échanger: ").upper()
        if (lt in main):
            jetons.append(lt)
    return jetons


    

    
plateauBonus=init_bonus()   
dico=init_dico ()
sac=init_pioche(dico)
j1=[]
j1=completer_main(j1,sac)

print()
print("La main du joueur 1 est :",j1)

def tour_joueur():
    x=int(input("Que voulez-vous faire ?                                                         1-Placer       2-Echanger         3-Passer       ->"))
    if (x==1):
        mot=str(input("Quelle mot souhaitez-vous placer ? --->"))
        
        test=tester_placement(plateauBonus, 0,3,"h",mot)
        print(test)

        plateau=placer_mot(plateauBonus,j1,mot, 0,5,"h")
        for ligne in plateau:
            print(*ligne, sep="|")
        print("Main après coup :",j1)

        """test=tester_placement(plateauBonus, 0,3,"h",mot)
        print(test)
        plateau=placer_mot(plateauBonus,j1,mot, 0,5,"h")"""


    elif (x==2):
        dico=init_dico ()
        print("Joueur 1")
        jetons1=jetons_change(j1)
        J1=echanger(jetons1,j1,sac)
        print("La main de j1:",J1)

    elif (x==3):
        dico=init_dico ()


        


       

#Programme principal

t=tour_joueur()
print(t)



