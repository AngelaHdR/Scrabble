#Construction des mots

#mettre dans une liste tous les mots autorisés dans le Scrabble
def generer_dico(nf):
    dico=[]
    fichier=open(nf)
    for ligne in fichier:
        dico.append(ligne)
    fichier.close()
    return dico

#voir si on peut construir un mot avec les lettres disponibles
def mot_jouable(mot,ll):
    return True
    return False

#voir d'une liste de mots lesquels on peut jouer avec les lettres disponibles
def mots_jouables(motsfr,dico):
    for mot in motsfr:
        if(not mot in dico):
            motsfr.remove(mot)
    return motsfr

dico=generer_dico("littre.txt")
motsfr=["PIED","MAISON","JARDIN","COMER"]
ll=["A","F","P","O","U","R","K","R"]
m=mots_jouables(motsfr,dico)
print(m)
