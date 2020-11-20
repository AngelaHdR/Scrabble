cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]




def init_jetons():                      #Fonction de la grille vide
    plateau=[]
    for i in range(15):
        plateau.append(15*["  "])
    return plateau


def init_bonus():                    #Fonction des lettre bonus à leur position
    jeton=init_jetons()
    a=0
    b=0
    
    for a in range(0,15,1):
        b=0
        
        for b in range(0,15,1):
            n=[a,b]
            if (n in cases_MT):
                jeton[a][b]="MT"
            elif (n in cases_MD):
                jeton[a][b]="MD"
            elif (n in cases_LT):
                jeton[a][b]="LT"
            elif (n in cases_LD):
                jeton[a][b]="LD"
    return jeton


#Programme principal
lettre_bonus=init_bonus()
plateau=init_jetons()
for ligne in lettre_bonus:
    print(*ligne, sep="|")

   


    
    
