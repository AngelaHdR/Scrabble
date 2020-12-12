#SCRABBLE
from random import*
cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
      

#PLATEAU DE JEU
    #creer une liste de listes de 15 lignes et 15 colonnes
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
    position=[i,j]
    if(position in cases_MT):
        plateau[i][j]=lettre+"#"
    elif(position in cases_MD):
        plateau[i][j]=lettre+"*"
    elif(position in cases_LD):
        plateau[i][j]=lettre+"^"
    elif(position in cases_LT):
        plateau[i][j]=lettre+"+"
    else:
        plateau[i][j]=lettre+" "
    return plateau



#LA PIOCHE
    #creer un dictionnaire avec le nombre et le valeur de chaque lettre
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
    nb=int(input("Combien de lettres voulez-vous échanger: "))
    for i in range (nb):
        lt=input("Lettres a échanger: ").upper()
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
        print("Il n'y a pas suffisamment des jetons dans le sac")
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

    #prouver le mot dans une position pour pouvoir calculer sa valeur avec les bonus
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

    #paser un mot avec les symboles des bonus a un mot sans les symboles des bonus
def mot_normal(mot):
    lettres=[]
    for lt in mot:
        if(not(lt=="#" or lt=="*" or lt=="+" or lt=="^")):
            lettres.append(lt)
        mots="".join(lettres)
    return mots


#VALEUR DES MOTS
    #Dans le dico on trouve les valeurs de chaque lettre et on calcule la somme totale avec les bonus
def valeur_mot(mot,dico):
    somme = 0
    a=1
    b=1
    for lt in mot:
        if(lt=="#"):
            a=a*3
        elif(lt=="*"):
            b=b*2
        elif(lt=="+"):
            somme=somme+valeur*2
        elif(lt=="^"):
            somme=somme+valeur
        else:
            val=dico[lt]["val"]
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
    normal=mot_normal(mot)
    test=tester_placement(plateau,i,j,dire,normal)
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
            if ((lt not in ll) and ("?" in ll)):
                ll.remove("?")
            else:
                ll.remove(lt)
        
        return plateau

#FONCTIONS INVENTÉS
    #Retrouver tous les mots qui sont placés dans le plateau
def mots_plateau(plateau,motsfr):
    mot=[]
    i=0
    j=0
    mots={}
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
            mots[mot]={"val":0}
        
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
            mots[mot]={"val":0}
        
        mot=[]   
    return mots

#Trouver le meilleur mot qui peut se jouer en utilisant un des jetons du tableau, renvoi le mot, la position, la direction, la valeur et la lettre utilisé
def position_jouable(plateau,ll):
    lettres=list(ll)
    mots={}
    jouable={}
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
                lettres.append(x)
                #on cherche le mots jouables et qui ont la lettre x
                joue=mots_jouables(motsfr,lettres)
                for mot in joue:
                    mot2=list(mot)
                    if(x not in mot2):
                        joue.remove(mot)
                    else:
                        b=mot2.index(x)
                        pi=i
                        pj=j
                        if((plateau[i+1][j]=="MT" or plateau[i+1][j]=="MD" or plateau[i+1][j]=="LT" or plateau[i+1][j]=="LD" or plateau[i+1][j]=="  ") and (plateau[i-1][j]=="MT" or plateau[i-1][j]=="MD" or plateau[i-1][j]=="LT" or plateau[i-1][j]=="LD" or plateau[i-1][j]=="  ")):
                            dire="v"
                            pi=i-b
                            pj=j
                            test=tester_placement(plateau,pi,pj,dire,mot)
                        elif((plateau[i][j+1]=="MT" or plateau[i][j+1]=="MD" or plateau[i][j+1]=="LT" or plateau[i][j+1]=="LD" or plateau[i][j+1]=="  ") and (plateau[i][j-1]=="MT" or plateau[i][j-1]=="MD" or plateau[i][j-1]=="LT" or plateau[i][j-1]=="LD" or plateau[i][j-1]=="  ")):
                            dire="h"
                            pi=i
                            pj=j-b
                        #on teste le placement de chaque mot
                            test=tester_placement(plateau,pi,pj,dire,mot)
                        else:
                            test=[]
                        if(test!=[]):
                            jouable[mot]={"i":0,"j":0,"dire":0,"lettre":0}
                            jouable[mot]["i"]=pi
                            jouable[mot]["j"]=pj
                            jouable[mot]["dire"]=dire
                            jouable[mot]["lettre"]=x
                #on calcule les meilleurs mots de la liste de mots jouables avec la lettre x
                jou=list(jouable.keys())
                if(len(jou)>0):
                    for mot in jou:
                        val=valeur_mot(mot,dico)
                        normal=mot_normal(mot)
                        mots[normal]=jouable[normal]
                        mots[normal]["val"]=val
                
                lettres.remove(x)
                jouable={}
            j+=1
        i+=1
    #on filtre tous les meilleurs mots de chaque lettre pour trouver la valeur plus haute
    valmax=0
    motmax=[]
    for mot in mots:
        if(mots[mot]["val"]>valmax):
            motmax=[]
            valmax=mots[mot]["val"]
            motmax.append(mot)
        elif(mots[mot]["val"]==valmax):
            motmax.append(mot)
    
    for mot in motmax:    
        jouable[mot]=mots[mot]
    return jouable

      #calculer le total des points apres avoir mis des lettres
def valeur_tableau(mots_nouveaux):
    somme=0
    mots=list(mots_nouveaux.keys())
    for mot in mots:
        valeur=mots_tableau[mot]["val"]
        somme=somme+valeur
    return somme

#trouver les nouveaux mots affichés
def mots_nouveaux(chercher1,chercher2):
    mots={}
    nouveaux={}
    c1=list(chercher1.keys())
    c2=list(chercher2.keys())
    for mot in c1:
        if(mot not in c2):
            del chercher1[mot]
    for mot in c2:
        if(mot not in c1):
            mots[mot]=chercher2[mot]
            nouveaux[mot]=chercher2[mot]
    m=list(mots.keys())
    for mot in m:
        regis=registre(mots_tableau,mot,mots[mot]["val"])
    return nouveaux

    #creer un dictionaire avec les mots écrits dans le tableau et sa valeur
def registre(mots_tableau,mot,val):
    mots_tableau[mot]={"val":0}
    mots_tableau[mot]["val"]=val
    return mots_tableau


#BOUCLE DE JEU A X JOUEURS
    #Creer un dictionnaire avec les joueurs, leurs mains et leurs points
def joueurs(sac):
    joueur={}
    nbj=int(input("Combien de joueurs êtes-vous ?"))
    for i in range (nbj) :
        prenom=input("Quel est ton prénom ?")
        joueur[prenom]= {"Main":0,"Points":0}
        j=[]
        j=completer_main(j,sac)
        joueur[prenom]["Main"]=j
    return joueur

       #BONUS AIDE DE JEU
    #Détermine le joueur qui doit jouer tout en conservant ses données (points, main et plateau)
def tour_joueur(plateau,sac,i):
    print("\nC'est le tour de :",i)
    print("Ta main est :",joueur[i]["Main"])
    x=int(input("\nQue veux-tu faire ?\n1-Placer   2-Echanger   3-Passer   4-Aide de vocabulaire->"))
            #Placer un mot
    if (x==1):
        mot=input("Quelle mot souhaitez-vous placer ? --->")
        l=int(input("Ligne de la premier lettre: "))
        c=int(input("Colonne de la premier lettre: "))
        dire=input("Direction horzontal (h) ou vertical (v): ")
        test=tester_placement(plateau, l,c,dire,mot)
        while(test==[]):
            print("ERREUR")
            mot=input("Quelle mot souhaitez-vous placer ? --->")
            l=int(input("Ligne de la premier lettre: "))
            c=int(input("Colonne de la premier lettre: "))
            dire=input("Direction horzontal (h) ou vertical (v): ")
            test=tester_placement(plateau, l,c,dire,mot)
        plateau=placer_mot(plateau,joueur[i]["Main"],mot, l,c,dire)
        j1=completer_main(joueur[i]["Main"],sac)
        joueur[i]["Main"]=j1

            #Echanger des lettres    
    elif (x==2):
        jetons1=jetons_change(joueur[i]["Main"])
        J1=echanger(jetons1,joueur[i]["Main"],sac)
        joueur[i]["Main"]=J1
        print("Ta nouvelle main est:",J1)
            
            #Aide pour creer des mots avec une main
    elif (x==4):
        mot=mots_jouables(motsfr,joueur[i]["Main"])
        print(mot)
        mot=input("Quelle mot souhaitez-vous placer ? --->")
        l=int(input("Ligne de la premier lettre: "))
        c=int(input("Colonne de la premier lettre: "))
        dire=input("Direction horzontal (h) ou vertical (v): ")
        test=tester_placement(plateau, l,c,dire,mot)
        while(test==[]):
            print("ERREUR")
            mot=input("Quelle mot souhaitez-vous placer ? --->")
            l=int(input("Ligne de la premier lettre: "))
            c=int(input("Colonne de la premier lettre: "))
            dire=input("Direction horzontal (h) ou vertical (v): ")
            test=tester_placement(plateau, l,c,dire,mot)
        plateau=placer_mot(plateau,joueur[i]["Main"],mot, l,c,dire)
        j1=completer_main(joueur[i]["Main"],sac)
        joueur[i]["Main"]=j1
    return plateau

       #Détecte la fin de la partie (sac vide)        
def fin_partie (main,sac):
    completer=7-len(main)
    if(completer>len(sac)):
        print("La partie est terminée, le sac est vide")
        print("Les scores de tous les joueurs sont:")
        valmax=0
        for nom in joueur:
            malus=0
            for lettre in joueur[nom]["Main"]:
                val=dico[lettre]["val"]
                malus=malus+val
            points=joueur[nom]["Points"]-malus
            print(nom, ":",points,"points")
            if(joueur[nom]["Points"]>valmax):
                valmax=joueur[nom]["Points"]
                gagnant=nom
        print("Le gagnant est",gagnant,"avec",valmax,"points")
        
    else:
        return True      

    #liste des joueurs en ordre
def prochain_joueur(joueur):                                    
    nom=list(joueur.keys())
    return nom

#BONUS INTELLIGENCE ARTIFICIELLE
#Determiner le joueur qui doit jouer tout en conservant ses données (points, main et plateau) faire les actions de maniere automatique
def tour_ordi(roun, plateau,i,sac):
    print("\nC'est le tour de :",i)
    print("Ta main est :",joueur[i]["Main"])
    plateau2=plateau
    main2=joueur[i]["Main"]
    chercher1=mots_plateau(plateau,motsfr)
    if(roun==0):
        mei=meilleurs_mots(motsfr,joueur[i]["Main"],dico,7,7,"h")
        print(mei)
        if(len(mei)>1):
            mot=int(input("Choisir l'index d'un mot pour placer: "))
            plateau=placer_mot(plateau,joueur[i]["Main"],mei[mot],7,7,"h")
            joueur[i]["Main"]=completer_main(joueur[i]["Main"],sac)
            chercher2=mots_plateau(plateau,motsfr)
            val=valeur_mot(mei[mot],dico)
            normal=mot_normal(mei[mot])
            chercher2[normal]["val"]=val
            
        elif(len(mei)==0):
            jetons1=jetons_change(joueur[i]["Main"])
            J1=echanger(jetons1,joueur[i]["Main"],sac)
            joueur[i]["Main"]=J1
            chercher2={}
        else:
            mei=mei[0]
            plateau=placer_mot(plateau,joueur[i]["Main"],mei,7,7,"h")
            joueur[i]["Main"]=completer_main(joueur[i]["Main"],sac)
            chercher2=mots_plateau(plateau,motsfr)
            val=valeur_mot(mei,dico)
            normal=mot_normal(mei)
            chercher2[normal]["val"]=val
        roun+=1
    else:
        pos=position_jouable(plateau,joueur[i]["Main"])
        print(pos)
        if(len(pos.keys())>1):
            mot=input("Choisir un mot pour placer: ")
            plateau=placer_mot(plateau,joueur[i]["Main"],mot,pos[mot]["i"],pos[mot]["j"],pos[mot]["dire"])
            joueur[i]["Main"]=completer_main(joueur[i]["Main"],sac)
            chercher2=mots_plateau(plateau,motsfr)
            if (chercher2==[]):
                joueur[i]["Main"]=main2
                return plateau2
            else:
                val=pos[mot]["val"]
                chercher2[mot]["val"]=val
        elif(len(pos.keys())==0):
            jetons1=jetons_change(joueur[i]["Main"])
            J1=echanger(jetons1,joueur[i]["Main"],sac)
            joueur[i]["Main"]=J1
            chercher2={}
        else:
            mot=list(pos.keys())
            mot=mot[0]
            plateau=placer_mot(plateau,joueur[i]["Main"],mot,pos[mot]["i"],pos[mot]["j"],pos[mot]["dire"])
            joueur[i]["Main"]=completer_main(joueur[i]["Main"],sac)
            chercher2=mots_plateau(plateau,motsfr)
            if (chercher2==[]):
                joueur[i]["Main"]=main2
                return plateau2
            else:
                val=pos[mot]["val"]
                chercher2[mot]["val"]=val
    mt=mots_nouveaux(chercher1,chercher2)
    print(mt)
    val=valeur_tableau(mt)
    print(val)
    x=joueur[i]["Points"]
    joueur[i]["Points"]=val+x
    return plateau
