#--------------------------------------
#--------------- GLOBAL ---------------
#--------------------------------------

#une_grille_vide = [['*','*','*'],['*','*','*'],['*','*','*']]
type Tgrille = list[list[str]]  #liste de listes de 3 formes (aussi lignes)

grille_finit1 = [['O','X','X'], ['O','*','O'], ['*','X','X']] #gagnant en ligne
grille_finit2 = [['O','O','X'], ['X','O','X'], ['O','X','X']] #gagnant en colone
grille_finit3 = [['X','O','O'], ['O','X','O'], ['O','X','X']] #gagnant en diagonale
grille_finit4 = [['X','O','X'], ['X','O','X'], ['O','X','O']] #pas de gagnant


#--------------------------------------
#---------------- CLASS ---------------
#--------------------------------------

class MorpionSimple:
    """Classe pour l'objet MorpionSimple, une partie de morpion classique
    Args :
    . . None

    Attributes :
    . . __nb_grille [int] : nombre de grilles créées (≠ du nb de grille en cours de jeu)

    Methods :
    . . partie_classique :
    . . . . Args :
    . . . . . . self
    . . . . Returns :
    . . . . . . [list] : liste de la grille de jeu et de la forme du gagnant (ou de la forme nulle)

    Class methods :
    . . nouvelle_grille :
    . . . . créer une nouvelle grille vide
    . . . . Args :
    . . . . . . None
    . . . . Returns :
    . . . . . . [Tgrille] : une grille de jeu vide

    . . afficher_la_grille :
    . . . . Afficher une grille par ses lignes
    . . . . Args :
    . . . . . . grille [Tgrille] : La grille à afficher
    . . . . Returns :
    . . . . . . None

    . . grille_gagnante :
    . . . . Est-ce que la grille est gagnante ?
    . . . . Args :
    . . . . . . grille [Tgrille] : La grille à tester
    . . . . Returns :
    . . . . . . [bool] : grille gagnante -> True, gille non gagnante -> False

    . . grille_complete :
    . . . . Est-ce que la grille est complete (une forme dans toutes les cases)?
    . . . . Args :
    . . . . . . grille [Tgrille] : La grille à tester
    . . . . Returns :
    . . . . . . [bool] : grille complete -> True, grille non complete -> False

    . . grille_finit :
    . . . . Est-ce que la grille est finit (grille complete ou alors gagnante) ?
    . . . . Args :
    . . . . . . grille [Tgrille] : La grille à tester
    . . . . Returns :
    . . . . . . [bool] : grille finit -> True, gille non finit -> False

    . . qui_gagne :
    . . . . Dit qui gagne selon une grille donnée
    . . . . Args :
    . . . . . . grille [Tgrille] : La grille à tester
    . . . . Returns :
    . . . . . . [str] : Forme du gagnant, X (croix) ou O (rond)

    . . reflechir :
    . . . . Donne toutes les informations de la grille de jeu, permet au joueur de choisir une position où jouer sa forme
    . . . . Args :
    . . . . . . grille [Tgrille] : la grille en cours de jeu
    . . . . Returns :
    . . . . . . [int] : position de la forme à jouer dans la grille

    . . jouer_une_forme :
    . . . . Jouer une forme ; X (croix) ou O (rond)
    . . . . Args :
    . . . . . . grille [Tgrille] : la grille en cours de jeu
    . . . . . . forme [str] : forme à jouer sur la grille
    . . . . . . position [int] : position de la forme dans la grille
    . . . . Returns :
    . . . . . . [Tgrille] : la grille agrémentée de la forme

    . . . . Notes : jouer_une_forme() nécessite d'avoir reflechir()
    """

    __nb_grille:int = 0

    @property #accesseur
    def nb(self):
        return MorpionSimple.__nb_grille


    def __init__(self):
        self.__grille:Tgrille = MorpionSimple.nouvelle_grille()
        self.__id_grille:str = f"#{MorpionSimple.__nb_grille}"

    @property #accesseur de l'id de la grille
    def id(self):
        return self.__id_grille

    @property #accesseur de la grille de jeu
    def grille(self):
        return self.__grille


    #|\/\/\/\/\/\/\/\/\/\/\/\/ CLASSMETHOD /\/\/\/\/\/\/\/\/\/\/\/\|

    @classmethod
    def nouvelle_grille(cls) -> Tgrille:
        """créer une nouvelle grille vide
        Args :
            None

        Returns :
            [Tgrille] : une grille de jeu vide
        """

        MorpionSimple.__nb_grille += 1
        return [['*', '*', '*'],
                ['*', '*', '*'],
                ['*', '*', '*']]

    @classmethod
    def afficher_la_grille(cls, grille:Tgrille): #affichage en ligne
        """Afficher une grille par ses lignes
        Args :
            grille [Tgrille] : La grille à afficher

        Returns :
            None
        """

        ligne1,ligne2, ligne3 = grille[0], grille[1], grille[2]

        grille = [ligne1, ligne2, ligne3]

        for decoupage_ligne in grille:
            print(f"{decoupage_ligne[0]} {decoupage_ligne[1]} {decoupage_ligne[2]}")

    @classmethod
    def grille_gagnante(cls, grille: Tgrille) -> bool:
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
                if forme[0] == forme[1] == forme[2] and '*' not in forme: return True
        return False

    @classmethod
    def grille_complete(cls, grille: Tgrille) -> bool:
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

    @classmethod
    def grille_finit(cls, grille: Tgrille) -> bool:
        """Est-ce que la grille est finit (grille complete ou alors gagnante) ?
        Args :
            grille [Tgrille] : La grille à tester

        Returns :
            [bool] : grille finit -> True, gille non finit -> False
        """

        if cls.grille_complete(grille) or cls.grille_gagnante(grille):
            return True
        else:
            return False

    @classmethod
    def qui_gagne(cls, grille: Tgrille) -> str:
        """Dit qui gagne selon une grille donnée
        Args :
            grille [Tgrille] : La grille à tester

        Returns :
            [str] : Forme du gagnant, X (croix) ou O (rond)
        """

        if not cls.grille_gagnante(grille): return '*'  #retourne la forme nulle si pas de gagnant

        colone1, colone2, colone3 = [], [], []
        diagonale_DG, diagonale_GD = [], []

        ligne1 = grille[0]  # définition des lignes
        ligne2 = grille[1]
        ligne3 = grille[2]

        for i in grille:  # définition des colones
            colone1.append(i[0])
            colone2.append(i[1])
            colone3.append(i[2])

        lignes = [ligne1, ligne2, ligne3]
        colones = [colone1, colone2, colone3]

        for l in lignes:  # définition des diagonales
            for i in range(3):
                if lignes.index(l) == i:
                    diagonale_GD.append(l[i])
                if lignes.index(l) == (l.__len__() - 1) - i:
                    diagonale_DG.append(l[i])

        diagonales = [diagonale_GD, diagonale_DG]

        grille_decoupe = (lignes, colones, diagonales)
        # victoire_en = ('ligne', 'colone', 'diagonale')

        # si 3 croix ou 3 ronds sont alignés : victoire
        for types_decoupage in grille_decoupe:
            for forme in types_decoupage:
                if forme[0] == forme[1] == forme[2] and '*' not in forme:
                    # print(f"> FIN : la personne jouant : {forme[0]} a gagné en {victoire_en[grille_decoupe.index(types_decoupage)]}\n")
                    return forme[0]
        # print(f"> FIN : pas de gagnant\n")
        return ''  # ne retourne rien si pas de gagnant

    @classmethod
    def reflechir(cls, grille: Tgrille):
        """Donne toutes les informations de la grille de jeu, permet au joueur de choisir une position où jouer sa forme
        Args :
            grille [Tgrille] : la grille en cours de jeu

        Returns :
            [int] : position de la forme à jouer dans la grille
        """

        print(f"\nGrille de jeu"); cls.afficher_la_grille(grille)  # grille de jeu en cours
        grille_des_positions: Tgrille = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        print(f"\nGrille des positions"); cls.afficher_la_grille(grille_des_positions)  # grille des positions

        choix_pos: list = []
        for l in range(3):
            for forme in range(3):
                if grille[l][forme] == '*': choix_pos.append(grille_des_positions[l][forme])
        print(f"\nles positions disponibles sont : {choix_pos}.")

    @classmethod
    def jouer_une_forme(cls, grille: Tgrille, forme: str, position: int) -> Tgrille:
        """Jouer une forme ; X (croix) ou O (rond)
        Args :
            grille [Tgrille] : la grille en cours de jeu
            forme [str] : forme à jouer sur la grille
            position [int] : position de la forme dans la grille

        Returns :
            [Tgrille] : la grille agrémentée de la forme

        Notes :
            jouer_une_forme() nécessite d'avoir reflechir()
        """

        if cls.grille_finit(grille):  # si déjà une grille finit
            print(f"> ATTENTION : Cette grille est déjà finit.")
            return grille  # éviter des calculs inutiles

        grille_numerote = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        for l in grille_numerote:  # l pour ligne
            for num in l:
                if num == position:
                    if grille[grille_numerote.index(l)][(num % 3) - 1] == '*':
                        grille[grille_numerote.index(l)][
                            (num % 3) - 1] = forme  # [(num%3)-1] -> l'index en fonction de num
                    else:
                        print(f"> ATTENTION : Impossible de jouer dans cette case.\n")
                        cls.reflechir(grille); pos: int = int(input(f"Ou placer votre forme ? : "))
                        return cls.jouer_une_forme(grille, forme, pos)
        return grille


    #|\/\/\/\/\/\/\/\/\/\/\/\/\/ METHOD \/\/\/\/\/\/\/\/\/\/\/\/\|
    #NOTE : d'après ce que je comprends, seulement les méthodes sont accessibles depuis l'extérieur, et pas les méthodes de classe. De plus les méthodes peuvent utiliser les méthodes de classe.

    def partie_classique(self) -> tuple:
        """Jouer une partie de Morpion classique
        Args :
            None

        Returns :
            tuple[Tgrille, str] : un tuple avec la grille de jeu finit et la forme gagnante ou neutre
        """

        print(f"\n> DEBUT : Partie de Morpion classique.")

        grille = self.grille #ref à __grille
        forme_precedente:str = input(f"Qui commence ? X/O : ")
        while not self.grille_finit(grille):
            self.reflechir(grille); pos = int(input(f"Ou placer votre forme ? : "))
            self.jouer_une_forme(grille, forme_precedente, pos)
            if forme_precedente == 'X': forme_precedente = 'O'
            else: forme_precedente = 'X'

        if self.grille_gagnante(grille):
            a: str = self.qui_gagne(grille)
            print(f"\n> FIN : Le joueur jouant '{a}' a gagné.\n")
        else:
            print(f"\n> FIN : Pas de gagnant.\n"); a: str = '*'

        return grille, a  # a -> forme du gagnant ou neutre