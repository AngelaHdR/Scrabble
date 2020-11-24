#La pioche
from random import*
#creer un dictioner avec le nombre et le valeur de chaque lettre
def init_dico ():                        
    dico={"A":{"occ":9 , "val":1},
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
    return dico


def init_pioche(dico):
    pioche=[]
    for lettre in dico :
        for i in range (dico[lettre]["occ"]):
            
            pioche.append(lettre)
    return pioche

#prendre x jetons de la pioche
def piocher(x,sac):
    main=[]
    for i in range (x):
        lt=randint(0,len(sac)-1)
        main.append(sac[lt])
        sac.pop(lt)
    return main

#completer la main pour avoir 7 jetons
def completer_main(main,sac):
    reste=7-len(main)
    if(len(sac)<=reste):
        reste=len(sac)
        main.extend(piocher(reste,sac))
    else:
        reste=7-len(main)
        main.extend(piocher(reste,sac))
    return main

#changer x jetons de la main par x jetons de la pioche
def echanger(jetons,main,sac):
    for i in range(len(jetons)):
        y=main.index(jetons[i])
        lt=main.pop(y)
        sac.append(lt)
    main=completer_main(main,sac)
    return main


#le sac c'est la fonction 2
dico=init_dico ()
sac=
main=["t","r","i"]
mainCom=completer_main(main,sac)
print(mainCom)
print(sac)
jetons=["t","r","i"]
z=echanger(jetons,mainCom,sac)
print(z)
print(sac)

