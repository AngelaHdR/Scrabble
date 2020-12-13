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

    #liste avec les prenoms des joueurs en ordre
nom=prochain_joueur(joueur)
print("\nOrdre des joueurs: ",nom)

    #affichage du plateau vide
for ligne in plateau:
    print(*ligne, sep="|")
    
#PROGRAMME PRINCIPAL
jeu=input("\nVous voulez jouer manuellement (m) ou automatiquement (a): ")
if(jeu=="m"):
    res=True
    while(res==True):
        for i in range(len(nom)):
            if(fin_partie(joueur[nom[i]]["Main"],pioche)):
                x=tour_joueur(plateau,pioche,nom[i])
                for ligne in x:
                    print(*ligne, sep="|")
            
            else:
                res=False
elif(jeu=="a"):
    roun=0
    res=True
    while(res==True):
        for i in range(len(nom)):
            if(fin_partie(joueur[nom[i]]["Main"],pioche)):
                x=tour_ordi(roun,plateau,nom[i],pioche)
                for ligne in x:
                    print(*ligne, sep="|")
            
            else:
                res=False
            roun+=1
