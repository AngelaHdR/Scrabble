#SCRABBLE
from random import*
cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
      

#PLATEAU DE JEU
    #creer une liste de listes de 15 ligne et 15 colognes
def init_jetons():
    plateau=[]
    for i in range(15):
        plateau.append(15*["  "])
    return plateau

    #afficher chaque bonus dans sa position correspondante
def init_bonus():
    plateauBonus=init_jetons()
    i=0
    for i in range(15):
        j=0
        for j in range(15):
            position=[i,j]
            if (position in cases_MT):
                plateauBonus[i][j]="MT"
            elif (position in cases_MD):
                plateauBonus[i][j]="MD"
            elif (position in cases_LT):
                plateauBonus[i][j]="LT"
            elif (position in cases_LD):
                plateauBonus[i][j]="LD"
    return plateauBonus

    #afficher le jeton dans la position choisit
def affichage_jetons(i,j,plateau,lettre):
    if(plateau[i][j]=="MT"):
        plateau[i][j]=lettre+"#"
    elif(plateau[i][j]=="MD"):
        plateau[i][j]=lettre+"*"
    elif(plateau[i][j]=="LD"):
        plateau[i][j]=lettre+"^"
    elif(plateau[i][j]=="LT"):
        plateau[i][j]=lettre+"+"
    else:
        plateau[i][j]=lettre+" "
    return plateau



#LA PIOCHE
    #creer un dictioner avec le nombre et le valeur de chaque lettre
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

    #creer une liste avec toutes les lettres 
def init_pioche(dico):
    sac=[]
    for lettre in dico :
        for i in range (dico[lettre]["occ"]):
            sac.append(lettre)
    return sac

    #prendre x jetons de la pioche
def piocher(x,sac):
    main=[]
    for i in range (x):
        lt=randint(0,len(sac)-1)
        main.append(sac[lt])
        sac.pop(lt)
    return main

    #completer la main pour avoir 7 jetons
def completer_main(main,sac):
    reste=7-len(main)
    if(len(sac)<=reste):
        reste=len(sac)
        main.extend(piocher(reste,sac))
    else:
        reste=7-len(main)
        main.extend(piocher(reste,sac))
    return main

    #creer une liste avec les jetons qu'on veut echanger
def jetons_change(main):
    jetons=[]
    nb=int(input("Nombre de lettres a echanger: "))
    for i in range (nb):
        lt=input("Lettre a echanger: ").upper()
        if (lt in main):
            jetons.append(lt)
    return jetons

    #changer x jetons de la main par x jetons de la pioche
def echanger(jetons,main,sac):
    if(len(sac)>=7):
        for i in range(len(jetons)):
            y=main.index(jetons[i])
            lt=main.pop(y)
            sac.append(lt)
        main=completer_main(main,sac)
    else:
        print("Il n'y a pas suffisant des jetons dans le sac")
    return main


#CONSTRUCTION DES MOTS
    #mettre dans une liste tous les mots autorisés dans le Scrabble
def generer_dico(nf):
    fichier=open(nf,"r")
    motsfr=[ligne.rstrip() for ligne in fichier]
    fichier.close()
    return motsfr

    #Vérifie si le mot joué contient les lettre de la main
def mot_jouable(mot,ll):           
    lettres_restantes = list(ll)
    for lt in mot:
        if (lt in lettres_restantes):
            lettres_restantes.remove(lt)
        elif ("?" in lettres_restantes):
            lettres_restantes.remove(lt)
        else:
            return False
    return True

    #Donne la liste de tout les mots français jouables avec la main du joueur
def mots_jouables(motsfr, ll):         
    selection = []
    for i in motsfr:
        if (mot_jouable(i, ll)):
            selection.append(i)
    return selection


#VALEUR DES MOTS
    #Dans le dico on trouve les valeurs de chaque lettre et on calcule la somme totale avec les bonus
def valeur_mot(mot,dico):
    somme = 0
    a=1
    b=1
    for i in mot:
        if(i=="#"):
            a=a*3
        elif(i=="*"):
            b=b*2
        elif(i=="+"):
            somme=somme+valeur*2
        elif(i=="^"):
            somme=somme+valeur
        else:
            val=dico[i]["val"]
        somme=somme+val
        valeur=val
        val=0
    
    somme=somme*a*b
    return somme

    #Trouver le mot avec la valeur la plus haute dans une positon donnée
def meilleur_mot(motsfr,ll,dico,i,j,dire):
    selection=mots_jouables(motsfr,ll)
    selection2=[]
    for mot in selection:
        test=tester_placement(plateau,i,j,dire,mot)
        if (test!=[]):
            mot2=tester_mots(plateau,i,j,dire,mot)
            selection2.append(mot2)
    valmax=0
    motmax=0
    for mot in selection2:
        val=valeur_mot(mot,dico)
        if (val>valmax):
            motmax=mot
            valmax=val       
    return motmax

    #Trouver tous les mots avec la valeur la plus haute dans une position donée
def meilleurs_mots(motsfr,ll,dico,i,j,dire):
    selection=mots_jouables(motsfr,ll)
    selection2=[]
    for mot in selection:
        test=tester_placement(plateau,i,j,dire,mot)
        if (test!=[]):
            mot2=tester_mots(plateau,i,j,dire,mot)
            selection2.append(mot2)
    valmax=0
    motmax=[]
    for mot in selection2:
        val=valeur_mot(mot,dico)
        if (val>valmax):
            motmax=[]
            motmax.append(mot)
            valmax=val
        elif(val==valmax):
            motmax.append(mot)
            valmax=val        
    return motmax


#PLACEMENT DES MOTS
    #Flitrer les coordonées jusqu'à trouver une case vide
#aun no la he usado
def lire_coords(tableau): 
    a=0
    while(a==0):
        i=int(input("Coordonée i: "))
        j=int(input("Coordonée j: "))
        position=[i,j]
        if ((tableau[i][j]=="MT") or (tableau[i][j]=="MD") or (tableau[i][j]=="LT") or (tableau[i][j]=="LD")or (tableau[i][j]=="  ")):
            a=1
        else:
            a=0
    return position

    #trouver le mot dans une position pour pouvoir calculer sa valeur avec les bonus
def tester_mots(plateau,i,j,dire,mot):
    mot2=[]
    if(dire=="h"):
        for lt in mot:
            if(plateau[i][j]=="MT" or plateau[i][j]==lt+"#"):
                mot2.append(lt)
                mot2.append("#")
            elif(plateau[i][j]=="MD" or plateau[i][j]==lt+"*"):
                mot2.append(lt)
                mot2.append("*")
            elif(plateau[i][j]=="LD" or plateau[i][j]==lt+"^"):
                mot2.append(lt)
                mot2.append("^")
            elif(plateau[i][j]=="LT" or plateau[i][j]==lt+"+"):
                mot2.append(lt)
                mot2.append("+")
            else:
                mot2.append(lt)
            j+=1
    elif(dire=="v"):
        for lt in mot:
            if(plateau[i][j]=="MT" or plateau[i][j]==lt+"#"):
                mot2.append(lt)
                mot2.append("#")
            elif(plateau[i][j]=="MD" or plateau[i][j]==lt+"*"):
                mot2.append(lt)
                mot2.append("*")
            elif(plateau[i][j]=="LD" or plateau[i][j]==lt+"^"):
                mot2.append(lt)
                mot2.append("^")
            elif(plateau[i][j]=="LT" or plateau[i][j]==lt+"+"):
                mot2.append(lt)
                mot2.append("+")
            else:
                mot2.append(lt)
            i+=1
    mot2="".join(mot2)
    return mot2

    #avec les coordones et la direction voir si le mot peut se placer en tenant en compte les lettres deja posés sur le plateau
def tester_placement(plateau,i,j,dire,mot):
    lettres=[]
    if(mot in motsfr):
        if(dire=="h"):
            if(len(mot)<=(15-j)):
                for lt in mot:
                    if(plateau[i][j]==lt or plateau[i][j]==lt+"*" or plateau[i][j]==lt+"+" or plateau[i][j]==lt+"#" or plateau[i][j]==lt+"^"):
                        j+=1
                    elif(lt=="*" or lt=="#" or lt=="+" or lt=="^"):
                        j=j
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
                    if(plateau[i][j]==lt or plateau[i][j]==lt+"*" or plateau[i][j]==lt+"+" or plateau[i][j]==lt+"#" or plateau[i][j]==lt+"^"):
                        i+=1
                    elif(lt=="*" or lt=="#" or lt=="+" or lt=="^"):
                        i=i
                    elif(plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD"):
                        i+=1
                        lettres.append(lt)
                    elif(plateau[i][j]!=lt):
                        lettres=[]
                        return lettres
            else:
                return lettres
            return lettres
    else:
        return lettres
    
    #placer un mot avec la position initial et la direction, modifier le plateau et la main
def placer_mot(plateau,ll,mot,i,j,dire):
    test=tester_placement(plateau,i,j,dire,mot)
    #print(test)
    mot2=list(mot)
    lettre=[]
    if(test==[]):
        return plateau
    else:
        if(dire=="h"):
            for lt in mot:
                if (lt=="#" or lt=="*" or lt=="+" or lt=="^"):
                    mot2.remove(lt)
                else:
                    affichage_jetons(i,j,plateau,lt)
                    j+=1
                lettre.append(lt)
            mot="".join(lettre)
            
        elif(dire=="v"):
            for lt in mot:
                if (lt=="#" or lt=="*" or lt=="+" or lt=="^"):
                    mot2.remove(lt)
                else:
                    affichage_jetons(i,j,plateau,lt)
                    i+=1
                lettre.append(lt)
            mot="".join(lettre)
            
        for lt in test:
            ll.remove(lt)
        
        return plateau
    
    #Retrouver tous les mots qui sont placés dans le plateau
def mots_plateau(plateau,motsfr):
    mot=[]
    i=0
    j=0
    mots=[]
    #reviser mots en horizontal
    for i in range(15):
        j=0
        while((plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD") and (j<14)):
            j+=1
        while(not(plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD") and (j<14)):
            lt=plateau[i][j]
            lt=list(lt)
            lt.pop(1)
            mot.append(*lt)
            j+=1
        mot="".join(mot)
        if (mot in motsfr):
            mots.append(mot)
        else:
            "ERREUR"
        mot=[]
            
    #reviser mots en vertical
    for j in range(15):
        i=0
        while((plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD") and (i<14)):
            i+=1
        while(not(plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD") and (i<14)):
            lt=plateau[i][j]
            lt=list(lt)
            lt.pop(1)
            mot.append(*lt)
            i+=1
        mot="".join(mot)
        if (mot in motsfr):
            mots.append(mot)
        mot=[]   
    return mots

#aun no la he usado
def position_jouable(plateau,ll):
    lettres=list(ll)
    mots=[]
    jouable=[]
    i=0
    for l in plateau:
        j=0
        for c in l:
            
            if(plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD" or plateau[i][j]=="  "):
                b=0
            else:
                x=list(plateau[i][j])
                x.pop(1)
                x="".join(x)
                #print(x)
                lettres.append(x)
                print(lettres)
                joue=mots_jouables(motsfr,lettres)
                for mot in joue:
                    mot2=list(mot)
                    if(x not in mot2):
                        joue.remove(mot)
                    else:
                        b=mot2.index(x)
                        
                        if((plateau[i+1][j]=="MT" or plateau[i+1][j]=="MD" or plateau[i+1][j]=="LT" or plateau[i+1][j]=="LD" or plateau[i+1][j]=="  ") and (plateau[i-1][j]=="MT" or plateau[i-1][j]=="MD" or plateau[i-1][j]=="LT" or plateau[i-1][j]=="LD" or plateau[i-1][j]=="  ")):
                            dire="v"
                            i=i-b
                        elif((plateau[i][j+1]=="MT" or plateau[i][j+1]=="MD" or plateau[i][j+1]=="LT" or plateau[i][j+1]=="LD" or plateau[i][j+1]=="  ") and (plateau[i][j-1]=="MT" or plateau[i][j-1]=="MD" or plateau[i][j-1]=="LT" or plateau[i][j-1]=="LD" or plateau[i][j-1]=="  ")):
                            dire="h"
                            j=j-b
                        print(dire)
                        print(i,j)
                        test=tester_placement(plateau,i,j,dire,mot)
                        if(test!=[]):
                            jouable.append(mot)
                        print(jouable)
                if(jouable!=[]):
                    meilleur=meilleurs_mots(jouable,lettres,dico,i,j,dire)
                    for mot in meilleur:
                        mots.append(mot)
                lettres.remove(x)
                jouable=[]
            j+=1
        i+=1
    return mots

    #paser un mot avec les symboles des bonus a un mot sans les symboles des bonus
def mot_normal(mot):
    lettres=[]
    for lt in mot:
        if(not(lt=="#" or lt=="*" or lt=="+" or lt=="^")):
            lettres.append(lt)
        mots="".join(lettres)
    return mots

      #calculer le total des points apres avoir mis des lettres
def valeur_tableau(chercher1,chercher):
    for mot in chercher1:
        if(mot not in chercher):
            del chercher1[mot]
    somme=0
    for mot in chercher:
        if(mot not in chercher1):
            valeur=mots_tableau[mot]["val"]
            somme=somme+valeur
    return somme

    #creer un dictionaire avec les mots ecrites dans le tableau et sa valeur
def registro(mots_tableau,mot,val):
    mots_tableau[mot]={"val":0}
    mots_tableau[mot]["val"]=val
    return mots_tableau


#BOUCLE DE JEU A X JOUEURS
    #Creer un dictionaire avec les joueurs, leurs mains et leurs points
def joueurs(sac):
    joueur={}
    nbj=int(input("Combien de joueur êtes vous ?"))
    for i in range (nbj) :
        prenom=input("Quel est ton prénom ?")
        joueur[prenom]= {"Main":0,"Points":0}
        j=[]
        j=completer_main(j,sac)
        joueur[prenom]["Main"]=j
    return joueur

    #Détermine le joueur qui doit jouer tout en conservant ses données (points, main et plateau)
def tour_joueur():
    for i in (nom):
        print("                                                                                          C'est le tour de :",i)
        print("Ta main est :",joueur[i]["Main"])

    
        x=int(input("                                                                                Que veux-tu faire ?                                                             1-Placer       2-Echanger         3-Passer       ->"))
        if (x==1):
            mot=str(input("Quelle mot souhaitez-vous placer ? --->"))
            
            test=tester_placement(plateauBonus, 0,3,"h",mot)
            print(test)

            plateau=placer_mot(plateauBonus,j1,mot, 0,5,"h")
            for ligne in plateau:
                print(*ligne, sep="|")
            print("Main après coup :",j1)

            
        elif (x==2):
            dico=init_dico ()
            jetons1=jetons_change(j1)
            J1=echanger(jetons1,j1,sac)
            print("Ta nouvelle main est:",J1)

        
    #Détecte la fin de la partie (sac vide)        
def fin_partie(main,sac):                              
    completer=7-len(main)
    if(completer>len(sac)):
        print("La partie est terminée, le sac est vide")
        return False
    else:
        return True        

    #liste des joueurs en ordre
def prochain_joueur(joueur):                                    
    nom=list(joueur.keys())
    return nom


#Programme principal
    #plateau de jeu avec les bonus
plateau=init_bonus()

    #dictoner avec les valeurs
dico=init_dico()

    #sac avec les jetons
pioche=init_pioche(dico)

    #liste de mots existants
motsfr=generer_dico("FICHIERLETTRE.txt")

    #dictioner avec les mots placés au tableau et ses valeurs
mots_tableau={}

    #dictioner avec les prenoms des joueurs, ses mains et ses points
joueur=joueurs(pioche)
print(joueur)

    #liste avec les prenoms des joueurs en ordre
nom=prochain_joueur(joueur)
print(nom)

    #affichage du plateau vide
for ligne in plateau:
    print(*ligne, sep="|")
