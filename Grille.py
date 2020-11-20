def init_bonus(N,M):
    grille=[]
    for _ in range (0,N):
       grille.append(M*["[]"])
    return grille

p=init_bonus(15,15)
print (p)
