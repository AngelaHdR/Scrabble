#Programme principal

joueur={}
nbj=int(input("Combien de joueur êtes vous ?"))
for i in range (nbj) :
    prenom=str(input("Quel est ton prénom ?"))
    joueur[prenom]= {"Main":0,"Points":0}
    j=[]
    j=completer_main(j,sac)
    joueur[prenom]["Main"]=j
    print (joueur[prenom])
nom=prochain_joueur(joueur)    
while fin_partie(joueur[prenom]["Main"],sac)!=(-1):
    x=tour_joueur()
