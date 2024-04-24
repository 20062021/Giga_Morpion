from QuiGagne import *
from pygame import *

"""
def
"""
def affiche_la_grille(grille:Tgrille):
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

# on sécurise le programme principal à l'interieur d'une fonction
def programme():
    """ Exécute le programme principal """
    print(f'X est une croix, O est un rond ---------------------------------------------------- \n')
    print(affiche_la_grille(grille_fini2))

#on appelle le programme uniquement si ce fichier spécifiquement à été exécuté
if __name__ == "__main__" : programme()