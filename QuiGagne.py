#from main import affiche_la_grille
#une_grille_type = [['E','E','E'],['E','E','E'],['E','E','E']]
# une liste pour une ligne, trois forment une grille de morpion 3*3


grille_fini = [['O','O','X'], ['O','X','O'], ['O','X','X']]
grille_fini2 = [['X','O','X'], ['X','O','O'], ['O','X','X']]
grille_fini3 = [['X','O','O'], ['O','X','X'], ['O','X','O']]
grille_fini4 = [['X','E','E'], ['O','E','X'], ['O','E','O']]

type Tgrille = tuple[tuple[str, str, str], tuple[str, str, str], tuple[str, str, str]]


def QG(grille:Tgrille) -> str :
    """Dis qui gagne selon une grille donnée

    Args:
        grille [Tgrille] : La grille à tester

    Returns:
        [str] : Qui a gagné et où, si personne : renvoie que personne n'a gagné
    """

    colone1, colone2, colone3 = [], [], []
    diagonale_DG, diagonale_GD = [], []
    ligne1 = grille[0]
    ligne2 = grille[1]
    ligne3 = grille[2]

    for i in grille:
        colone1.append(i[0])
        colone2.append(i[1])
        colone3.append(i[2])

    for ligne in grille:
        for i in range(3):
            if grille.index(ligne) == i:
                diagonale_GD.append(ligne[i])
            elif grille.index(ligne) == (ligne.__len__() - 1) - i :
                diagonale_DG.append(ligne[i])                

    lignes = [ligne1, ligne2, ligne3]
    colones = [colone1, colone2, colone3]
    diagonales = [diagonale_GD, diagonale_DG]

    grille_découpé = (lignes, colones, diagonales)
    victoire_en = ('ligne', 'colone', 'diagonale')

    # si 3 croix ou 3 ronds ne forment pas des lignes (sont alignès), pas de victoire tesrt
    for types in grille_découpé:
        for rang_x in types:
            if rang_x[0] == rang_x[1] == rang_x[2] and rang_x[0] != 'E':
                return f'{rang_x[0], rang_x[1], rang_x[2]}  ->  la personne jouant; {rang_x[0]}, à gagné en {victoire_en[grille_découpé.index(types)]}'
            else:
                print(f"{rang_x[0], rang_x[1], rang_x[2]}   ->  personne ne gagne sur cet {victoire_en[grille_découpé.index(types)]}")

        print('\n')
    return f"personne n'as gagné !"


print(QG(grille_fini4))