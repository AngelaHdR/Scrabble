#Construction des mots

#mettre dans une liste tous les mots autorisés dans le Scrabble
def generer_dico(nf):
    fichier=open(nf,"r")
    dico=[ligne.rstrip() for ligne in fichier]
    fichier.close()
    return dico

#Vérifie si le mot joué contient les lettre de la main
def mot_jouable(mot,ll):           
    lettres_restantes = list(ll)
    for l in mot:
        if l in lettres_restantes:
            lettres_restantes.remove(l)
        else:
            return False
    return True

#Donne la liste de tout les mots français jouables avec la main du joueur
def mots_jouables(dico, ll):         
    selection = []
    for i in dico:
        if mot_jouable(i, ll):
            selection.append(i)
    return selection


dico=generer_dico("littre.txt")
motsfr=["PIED","COURRIR","DEPIT","TAPIR","MARCHER"]
ll=["P","A","I","D","E","T","R"]
n=mot_jouable("PIED",ll)
print(n)
m=mots_jouables(dico,ll)
print(m)
j=mots_jouables(motsfr,ll)
print(j)

