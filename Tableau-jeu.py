#Plateau de jeu
    #creer une liste de listes de 15 ligne et 15 colognes
def init_jetons():
    plateau=[]
    for i in range(15):
        plateau.append(15*["  "])
    return plateau
    #afficher chaque bonus dans sa position correspondante
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
    

    #afficher le jeton dans la position choisit
def affichage_jetons(ligne,cologne,plateau):
    lettre=input("Jeton?: ").upper()
    
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



 
#plateau=init_jetons()
#for ligne in plateau:
    #print(*ligne, sep="|")
    
plateauBonus=init_bonus()
for ligne in plateauBonus:
    print(*ligne, sep="|")
    
plateauJoue=affichage_jetons(0,1,plateauBonus)
for ligne in plateauJoue:
    print(*ligne, sep="|")
    
#Pour ecrire un mot il faudrait creer un boucle pour prendre toujours le dernier tableau comme paramètre
#Et determiner automatiquement la direction (i+-1 et j+-1) pour ecrire le mot en ordre

#mot=input("Mot a jouer: ").upper()
    #mot=list(mot)
    #if (len(mot)>15-j):
        #return "[]"
    #for lettre in mot:
        #plateau[i][j]=lettre
        #j+=1 si le mot va en horizontal
        #i+=1 si le mot va en vertical
    #return plateau
