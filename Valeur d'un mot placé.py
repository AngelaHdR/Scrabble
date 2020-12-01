def init_dico ():                        
    d={"A":{"occ":9 , "val":1},
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
    
    return d            #Fonction (reprenant la liste des point, associés à chaque lettre) qui va sommer l'ensemble des valeurs de chaque lettre que contient le mot et va renvoyer le total de point du mot.

def valeur_mot(dico, mot):
    somme = 0
    i = 0
    while i<len(mot):
        pos=(mot[i])
        val=dico[pos]["val"]
        somme=somme+val
        i=i+1
    return somme


#Programme principal
dico=init_dico ()
mot="CERISE"
x=valeur_mot(dico,mot)
print(mot,"-->",x,"points")
