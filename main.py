from QuiGagne import *

print(f'X est une croix, O est un rond ---------------------------------------------------- \n')


def affiche_la_grille(grille):
    colone1, colone2, colone3 = [], [], []
    ligne1 = grille[0]
    ligne2 = grille[1]
    ligne3 = grille[2]

    for i in grille:
        colone1.append(i[0])
        colone2.append(i[1])
        colone3.append(i[2])

    grille_en_ligne = (f"{ligne1}\n"
                       f"{ligne2}          ↓ vue réel\n"
                       f"{ligne3}\n")

    # ↑↓→←

    grille_en_colone = (f"{colone1}\n"
                        f"{colone2}          ← vue de la gauche\n"
                        f"{colone3}\n")

    a = f"{grille_en_ligne}\n{grille_en_colone}"
    return a

print(affiche_la_grille(grille_fini2))

