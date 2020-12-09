#Plateau de jeu
cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

    #creer une liste de listes de 15 ligne et 15 colognes
def init_jetons():
    plateau=[]
    for i in range(15):
        plateau.append(15*["  "])
    return plateau

    #afficher chaque bonus dans sa position correspondante
def init_bonus():      
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
    

    #afficher le jeton dans la position choisit
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
#PLACEMENT DE MOT
    #Flitrer les coordonées jusqu'à trouver une case vide
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

def placer_mot(plateau,ll,mot,i,j,dire):
    test=tester_placement(plateau,i,j,dire,mot)
    if(test==[]):
        return plateau
    else:
        if(dire=="h"):
            a=1
            b=1
            c=0
            d=0
            for lt in mot:
                if (plateau[i][j]=="MT"):
                    a=3
                elif(plateau[i][j]=="MD"):
                    b=2
                elif(plateau[i][j]=="LT"):
                    c=dico[lt]["val"]
                    c=3*c
                elif(plateau[i][j]=="LD"):
                    d=dico[lt]["val"]
                    d=2*d
                affichage_jetons(i,j,plateau,lt)
                j+=1
            valeur=valeur_mot(mot,dico)
            valeur=(a*b*valeur)+c+d
        elif(dire=="v"):
            a=1
            b=1
            c=0
            d=0
            for lt in mot:
                position=[i,j]
                if (plateau[i][j]=="MT"):
                    a=3
                elif(plateau[i][j]=="MD"):
                    b=2
                elif(plateau[i][j]=="LT"):
                    c=dico[lt]["val"]
                    c=3*c
                elif(plateau[i][j]=="LD"):
                    d=dico[lt]["val"]
                    d=2*d
                affichage_jetons(i,j,plateau,lt)
                i+=1
            valeur=valeur_mot(mot,dico)
            valeur=(a*b*valeur)+c+d
        for lt in test:   
            ll.remove(lt)
        print(valeur)
        return plateau
def mots_plateau(plateau):
    mot=[]
    i=0
    j=0
    mots=[]
#reviser mots en horizontal
    for i in range(15):
        while(j<=14):
            while((plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD") and (j<=14)):
                j+=1
            while(not(plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD") and j<=14):
                mot.append(plateau[i][j])
                j+=1
            mot=print(*mot,sep="")
            mots.append(mot)
            mot=[]
#reviser mots en vertical
    for j in range(15):
        while(i<=14):
            while((plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD") and (i<=14)):
                i+=1
            while(not(plateau[i][j]=="  " or plateau[i][j]=="MT" or plateau[i][j]=="MD" or plateau[i][j]=="LT" or plateau[i][j]=="LD") and (i<=14)):
                mot.append(plateau[i][j])
                i+=1
            mot=print(*mot,sep="")
            mots.append(mot)
            mot=[]
    return mots
        
                        
    
#PROGRAMME PRINCIPAL
    
plateauBonus=init_bonus()
#for ligne in plateauBonus:
    #print(*ligne, sep="|")
    
#plateauJoue=affichage_jetons(0,1,plateauBonus)
#for ligne in plateauJoue:
    #print(*ligne, sep="|")
ll=["C","U","B","A","J","E","R"]
#test=tester_placement(plateauBonus, 0,5,"h","CUBA")
#print(test)

plateau=placer_mot(plateauBonus,ll,"CUBA", 0,5,"h")
for ligne in plateau:
    print(*ligne, sep="|")
print(ll)

x=lire_coords(plateau)
print(x)

motplat=mots_plateau(plateau)
print(mots)
#Pour ecrire un mot il faudrait creer un boucle pour prendre toujours le dernier tableau comme paramètre
#Et determiner automatiquement la direction (i+-1 et j+-1) pour ecrire le mot en ordre

#mot=input("Mot a jouer: ").upper()
    #if (len(mot)>15-j):
        #return "[]"
    #for lettre in mot:
        #affichage_jetons(ligne,cologne,panneau,lettre)
        #j+=1 si le mot va en horizontal
        #i+=1 si le mot va en vertical
    #return plateau
