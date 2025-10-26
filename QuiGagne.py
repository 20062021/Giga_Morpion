#from main import affiche_la_grille
#une_grille_type = [['NaN','NaN','NaN'],['NaN','NaN','NaN'],['NaN','NaN','NaN']]
#une liste pour une ligne, trois forment une grille de morpion 3*3


grille_fini = [['O','O','X'], ['O','X','O'], ['O','X','X']]
grille_fini2 = [['X','O','X'], ['X','O','O'], ['O','X','X']]
grille_fini3 = [['X','O','O'], ['O','X','X'], ['O','X','O']]
grille_fini4 = [['X','NaN','NaN'], ['O','NaN','X'], ['O','NaN','O']]

type Tgrille = [[str, str, str], [str, str, str], [str, str, str]] #liste de listes de 3 formes (aussi lignes)


def QuiGagne(grille:Tgrille) -> bool:
    """Dis qui gagne selon une grille donnée

    Args:
        grille [Tgrille] : La grille à tester

    Returns :
        [bool] : Un gagnant, si oui : true, si non : false. Afficher un message en console dans les deux cas.
    """

    colone1, colone2, colone3 = [], [], []
    diagonale_DG, diagonale_GD = [], []

    ligne1 = grille[0] #définition des lignes
    ligne2 = grille[1]
    ligne3 = grille[2]

    for i in grille: #définition des colones
        colone1.append(i[0])
        colone2.append(i[1])
        colone3.append(i[2])

    for ligne in grille: #définition des diagonales
        for i in range(3):
            if grille.index(ligne) == i:
                diagonale_GD.append(ligne[i])
            elif grille.index(ligne) == (ligne.__len__() - 1) - i :
                diagonale_DG.append(ligne[i])                

    lignes = [ligne1, ligne2, ligne3]
    colones = [colone1, colone2, colone3]
    diagonales = [diagonale_GD, diagonale_DG]

    grille_decoupe = (lignes, colones, diagonales)
    victoire_en = ('ligne', 'colone', 'diagonale')

    # si 3 croix ou 3 ronds sont alignés : victoire
    for types_decoupage in grille_decoupe:
        for forme in types_decoupage:
            if forme[0] == forme[1] == forme[2] and forme[0] != 'NaN':
                print(f"{forme[0], forme[1], forme[2]}  ->  la personne jouant; {forme[0]}, a gagné en {victoire_en[grille_decoupe.index(types_decoupage)]}\n")
                return True
            else:
                print(f"{forme[0], forme[1], forme[2]}   ->  personne ne gagne sur cette {victoire_en[grille_decoupe.index(types_decoupage)]}\n")
                return False


print(QuiGagne(grille_fini4))