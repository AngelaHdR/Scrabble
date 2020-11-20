#Plateau de jeu
def init_bonus():
    bonus=[]
    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
        #creer une liste de 15 lignes avec les 15 colognes
        
    #inserer dans la position correspondante les bonus, passer pour toutes les colognes de toutes les lignes
def init_jetons():
    plateau=[]
    for i in range(15):
        plateau.append(15*[" "])
    return plateau

    #afficher le jeton dans la position correspondante
def affichage_jetons(i,j,plateau):
    lettre=input("Jeton?: ")
    plateau[i][j]=lettre
    return plateau



 
plateau=init_jetons()
for ligne in plateau:
    print(*ligne, sep="|")

plateauJoue=affichage_jetons(4,7,plateau)
for ligne in plateauJoue:
    print(*ligne, sep="|")

plateauJoue=affichage_jetons(10,3,plateauJoue)
for ligne in plateauJoue:
    print(*ligne, sep="|")
    
#Pour ecrire un mot il faudrait creer un boucle pour prendre toujours le dernier tableau comme paramètre
#Et determiner automatiquement la direction (i+-1 et j+-1) pour ecrire le mot en ordre

#mot=input("Mot a jouer: ").upper()
    #mot=list(mot)
    #if (len(mot)>15-j):
        #return ""
    #for lettre in mot:
        #plateau[i][j]=lettre
        #j+=1
    #return plateau
