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

#CONSTRUCTION DES MOTS
#Ameliorer les fonctions mot_jouable et mots_jouables pour les jokers et les mots places 

#mettre dans une liste tous les mots autorisés dans le Scrabble
def generer_dico(nf):
    fichier=open(nf,"r")
    motsfr=[ligne.rstrip() for ligne in fichier]
    fichier.close()
    return motsfr

#position
def position_jouable(i,j,plateau,lt,ll):
    lettres=list(ll)
    mots=[]
    for i in plateau:
        for j in plateau[i]:
            if(plateau[i][j]=="MT" and plateau[i][j]=="MD" and plateau[i][j]=="LT" and plateau[i][j]=="LD" or plateau[i][j]=="  "):
                a=0
            else:
                lettres.append(plateau[i][j])
                joue=meilleur_mot(motsfr,lettres,dico)
                a=joue.index(plateau[i][j])
                if(plateau[i+1][j]=="" and plateau[i-1][j]==""):
                    dire="h"
                    j=j-a
                elif(plateau[i][j+1]=="" and plateau[i][j-1]==""):
                    dire="v"
                    i=i-a
                test=tester_placement(plateau,i,j,dire,joue)
                if(not test==[]):
                    mots.append(joue)
    return mot

a=position_jouable(0,2,plateau,lt,ll)

lettres=list(ll)
mots=[]
for lt in mot:
    i=plateau.index(lt)
    j=plateau[i].index(lt)
    if(plateau[i+1][j]=="" and plateau[i-1][j]==""):
        i=0
    elif(plateau[i][j+1]=="" and plateau[i][j-1]==""):
        #se puede colocar palabra en vertical
        lettre.append(plateau[i][j])
        joue=mots_jouables(motsfr,lettres)
        mot.append(joue)
        


        
#voir si une place est libre
def libre(i,j,plateau):
    if(plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD"):
        return True
    else:
        return False
    
#Vérifie si le mot joué contient les lettre de la main
def mot_jouable(mot,ll):           
    lettres_restantes = list(ll)
    for lt in mot:
        if (lt in lettres_restantes):
            lettres_restantes.remove(lt)
        elif (lt=="?"):
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

#Dans le dico on trouve les valeurs de chaque lettre
def valeur_mot(mot,dico):
    somme = 0
    i = 0
    while i<len(mot):
        pos=(mot[i])
        val=dico[pos]["val"]
        somme=somme+val
        i=i+1
    return somme

#Trouver le mot avec la valeur la plus haute
def meilleur_mot(motsfr,ll,dico):
    selection=mots_jouables(motsfr,ll)
    valmax=0
    motmax=0
    for mot in selection:
        val=valeur_mot(mot,dico)
        if (val>valmax):
            motmax=mot
            valmax=val       
    return motmax,valmax

def meilleurs_mots(motsfr,ll,dico):
    selection=mots_jouables(motsfr,ll)
    valmax=0
    motmax=[]
    for mot in selection:
        val=valeur_mot(mot,dico)
        if (val>valmax):
            motmax=[]
            motmax.append(mot)
            valmax=val
        elif(val==valmax):
            motmax.append(mot)
            valmax=val        
    return motmax,valmax


#PROGRAMME PRINCIPAL
dico=init_dico()
motsfr=generer_dico("littre.txt")
ll=["P","A","D","S","R","E","U"]

m=mots_jouables(motsfr,ll)
#print(m)

#val=valeur_mot("CERISE",dico)
#print(val,"points")

meill=meilleur_mot(motsfr,ll,dico)
print(meill,"points")

meis=meilleurs_mots(motsfr,ll,dico)
print(meis,"points")

#mots=["PIED","COURRIR","DEPIT","TAPIR","MARCHER"]
#n=mot_jouable("PIED",ll)
#print(n)
#j=mots_jouables(mots,ll)
#print(j)
