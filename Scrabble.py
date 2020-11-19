#Plateau de jeu

def init_bonus():
    bonus=[]
    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

        #creer une liste de 15 lignes avec les 15 colognes
    for i in range(15):
        bonus.append(15*[""])
    print(bonus,"\n")
    
        #inserer dans la position correspondante les bonus, passer pour toutes les positions de toutes les lignes
    ligne=0
    for ligne in range (15):
        colum=0
        for colum in range (15):
            position=[ligne,colum]
            p=0
            if (position in cases_MT):
                bonus[ligne].pop(colum)
                bonus[ligne].insert(colum,"MT")
            elif (position in cases_MD):
                bonus[ligne].pop(colum)
                bonus[ligne].insert(colum,"MD")
            elif (position in cases_LT):
                bonus[ligne].pop(colum)
                bonus[ligne].insert(colum,"LT")
            elif (position in cases_LD):
                bonus[ligne].pop(colum)
                bonus[ligne].insert(colum,"LD")
    return bonus
            
x=init_bonus()
print(x)

