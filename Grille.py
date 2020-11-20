def init_bonus(N,M):
    grille=[]
    for _ in range (0,N):
       grille.append(M*["[]"])
    return grille

p=init_bonus(15,15)
print (p)


"""from random import*

def creer_grille(N,M):
   grille=[]
   for _ in range (0,N):
       grille.append(M*["0"])
   return grille

def placer_mines(grille,X):
    mines=1
    N=len(grille)
    M=len(grille[0])
    while mines<=1:
        i=randint(0,N-1)
        j=randint(0,M-1)
        grille[i][j]=1
        mines=mines+1
    return grille

grille=creer_grille(5,3)
print(placer_mines(grille,7))"""
