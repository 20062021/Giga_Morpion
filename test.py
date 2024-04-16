a = [1, 2, 5, 'r']

a.index(1,0,1)

grille = [['X','O','O'], ['O','X','O'], ['W','O','X']]

diagonale_DG, diagonale_GD = [[],[],[]], [[],[],[]]

for ligne in grille:
    for i in range(3):  # la grille est de dimension 3 * 3
        if grille.index(ligne) == i:
            diagonale_GD[i].append(ligne[i])
        else:
            diagonale_GD[i].append(None)

        if grille.index(ligne) == i:
            pass

print(diagonale_GD)
print(diagonale_DG)