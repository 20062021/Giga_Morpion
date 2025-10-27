#from main import affiche_la_grille
#une_grille_type = [['*','*','*'],['*','*','*'],['*','*','*']]
#une liste pour une ligne, trois forment une grille de morpion 3*3


grille_fini = [['O','X','X'], ['O','*','O'], ['O','X','X']] #gagnant en ligne
grille_fini2 = [['O','O','X'], ['X','O','X'], ['O','X','X']] #gagnant en colone
grille_fini3 = [['X','O','O'], ['O','X','O'], ['O','X','X']] #gagnant en diagonale
grille_fini4 = [['X','O','X'], ['X','O','X'], ['O','X','O']] #pas de gagnant

type Tgrille = [[str, str, str], [str, str, str], [str, str, str]] #liste de listes de 3 formes (aussi lignes)


def QuiGagne(grille:Tgrille) -> str:
    """Dit qui gagne selon une grille donnée
    Args :
        grille [Tgrille] : La grille à tester

    Returns :
        [str] : Forme du gagnant, X (croix) ou O (rond)
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

    lignes = [ligne1, ligne2, ligne3]
    colones = [colone1, colone2, colone3]

    for l in lignes: #définition des diagonales
        for i in range(3):
            if lignes.index(l) == i:
                diagonale_GD.append(l[i])
            if lignes.index(l) == (l.__len__() - 1) - i :
                diagonale_DG.append(l[i])

    diagonales = [diagonale_GD, diagonale_DG]

    grille_decoupe = (lignes, colones, diagonales)
    #victoire_en = ('ligne', 'colone', 'diagonale')

    # si 3 croix ou 3 ronds sont alignés : victoire
    for types_decoupage in grille_decoupe:
        for forme in types_decoupage:
            if forme[0] == forme[1] == forme[2] and '*' not in forme:
                #print(f"> FIN : la personne jouant : {forme[0]} a gagné en {victoire_en[grille_decoupe.index(types_decoupage)]}\n")
                return forme[0]
    #print(f"> FIN : pas de gagnant\n")
    #return '*'

def Grille_gagnante(grille:Tgrille) -> bool:
    """Est-ce que la grille est gagnante ?
    Args :
        grille [Tgrille] : La grille à tester

    Returns :
        [bool] : grille gagnante -> True, gille non gagnante -> False
    """

    colone1, colone2, colone3, diagonale_DG, diagonale_GD = [], [], [], [], []
    ligne1, ligne2, ligne3 = grille[0], grille[1], grille[2]  # définition des lignes

    for i in grille:  # définition des colones
        colone1.append(i[0]), colone2.append(i[1]), colone3.append(i[2])

    lignes, colones = [ligne1, ligne2, ligne3], [colone1, colone2, colone3]

    for l in lignes:  # définition des diagonales
        for i in range(3):
            if lignes.index(l) == i:
                diagonale_GD.append(l[i])
            if lignes.index(l) == (l.__len__() - 1) - i:
                diagonale_DG.append(l[i])

    diagonales = [diagonale_GD, diagonale_DG]

    grille_decoupe = (lignes, colones, diagonales)

    for types_decoupage in grille_decoupe:
        for forme in types_decoupage:
            if forme[0] == forme[1] == forme[2]: return True
    return False

def Grille_complete(grille:Tgrille) -> bool:
    """Est-ce que la grille est complete (une forme dans toutes les cases)?
    Args :
        grille [Tgrille] : La grille à tester

    Returns :
        [bool] : grille complete -> True, grille non complete -> False
    """

    for decoupage_ligne in grille:
        for forme in decoupage_ligne:
            if forme == '*': return False
    return True

def Grille_finit(grille:Tgrille) -> bool:
    """Est-ce que la grille est finit (grille complete ou alors gagnante) ?
    Args :
        grille [Tgrille] : La grille à tester

    Returns :
        [bool] : grille finit -> True, gille non finit -> False
    """

    if Grille_complete(grille) or Grille_gagnante(grille):
        return True
    else: return False