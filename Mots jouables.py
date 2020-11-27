def mot_jouable(mot,ll):           #Vérifie si le mot joué contient les lettre de la main

    lettres_restantes = list(ll)

    for ll in mot:
        if ll in lettres_restantes:
            lettres_restantes.remove(ll)
        else:
            return False
    return True


  
def mots_jouables(motsfr, ll):         #Donne la liste de tout les mots français jouables avec la main du joueur
    selection = []
    i = 0
    while i<len(motsfr):
        if mot_jouable(motsfr[i], ll):
            selection.append(motsfr[i])

        i += 1
    return selection
    
    


#Programme principal 1
a=mot_jouable("PIED", ["P","A","I","D","E","W","K"])
print(a)

#Programme principal 2

b=mots_jouables(["PIED","COURRIR","DEPIT","TAPIR","MARCHER"], ["P","A","I","D","E","T","R"])
print(b)
