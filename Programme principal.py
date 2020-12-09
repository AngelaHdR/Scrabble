#Programme principal
    #plateau de jeu avec les bonus
plateau=init_bonus()

    #dictoner avec les valeurs
dico=init_dico()

    #sac avec les jetons
pioche=init_pioche(dico)

    #liste de mots existants
motsfr=generer_dico("FICHIERLETTRE.txt")

    #dictioner avec les mots placés au tableau et ses valeurs
mots_tableau={}

    #dictioner avec les prenoms des joueurs, ses mains et ses points
joueur=joueurs(pioche)
print(joueur)

    #liste avec les prenoms des joueurs en ordre
nom=prochain_joueur(joueur)
print(nom)

    #affichage du plateau vide
for ligne in plateau:
    print(*ligne, sep="|")
    
while (fin_partie(joueur[prenom]["Main"],sac)):
    x=tour_joueur()


