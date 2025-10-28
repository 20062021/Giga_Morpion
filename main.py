#--------------------------------------
#--------------- IMPORT ---------------
#--------------------------------------

from Morpion_simple import *
#from pygame import *


#--------------------------------------
#--------------- GLOBAL ---------------
#--------------------------------------
class Joueur:
    """Un joueur du Morpion
    Args :
        pseudo [str] : pseudo du joueur
        
    Attributes :
        __pseudos [list(str)] : liste des pseudos utilisés par les joueurs

    Methods :

    """

    __pseudos:list = []

    def __init__(self, pseudo:str): #constructeur
        print(f"\n> : Creation du joueur")
        self.__pseudo:str = pseudo #attribut privé

    @property #accesseur de l'attribut pseudo
    def pseudo(self): return self.__pseudo

    @pseudo.setter #mutateur de l'attribut pseudo
    def pseudo(self, pseudo:str):
        """changer de pseudo"""
        print(f"> DEBUG : @pseudo.setter")
        if pseudo not in self.__pseudos:
            self.__pseudo = pseudo; self.__pseudos.append(pseudo)
        else: print(f"\n> ATTENTION : '{pseudo}' est déjà prit.\n")

    @classmethod #méthode de class
    def afficher_pseudos(cls):
        """afficher les pseudos utilisés par les joueurs"""
        return cls.__pseudos

#--------------------------------------
#-------------- FUNCTIONS -------------
#--------------------------------------


#--------------------------------------
#---------------- MAIN ----------------
#--------------------------------------
def programme():
    """ Exécute le programme principal """
    print(f"////////////////////////// INITIALISATION //////////////////////////\n"
          f"//   INFORMATION                                                  //\n"
          f"//    - X est une croix;                                          //\n"
          f"//    - O est un rond.                                            //\n"
          f"////////////////////////////////////////////////////////////////////\n")

    """
    a=''

    affiche_la_grille(grille_fini)
    if (Grille_gagnante(QuiGagne(grille_fini))): a = f"> FIN : Le gagnant est {QuiGagne(grille_fini)}.\n"
    else: a = f"> !! Pas de gagnant\n"
    print(a)

    affiche_la_grille(grille_fini2)
    if (Grille_gagnante(QuiGagne(grille_fini2))): a = f"> FIN : Le gagnant est {QuiGagne(grille_fini2)}.\n"
    else: a = f"> !! Pas de gagnant\n"
    print(a)

    affiche_la_grille(grille_fini3)
    if (Grille_gagnante(QuiGagne(grille_fini3))): a = f"> FIN : Le gagnant est {QuiGagne(grille_fini3)}.\n"
    else: a = f"> !! Pas de gagnant\n"
    print(a)

    affiche_la_grille(grille_fini4)
    if (Grille_gagnante(QuiGagne(grille_fini4))): a = f"> FIN : Le gagnant est {QuiGagne(grille_fini4)}.\n"
    else: a = f"> !! Pas de gagnant\n"
    print(a)
    """

    """
    forme: str = input("Quelle est votre forme ? X/O : ")
    jouer_une_forme(grille_finit1, forme, reflechir(grille_finit1))
    """

    """
    print(f"\n> DEBUT :"); grille_partie1 = partie_classique(nouvelle_grille())
    if grille_gagnante(grille_partie1): print(f"\n> FIN : Le joueur jouant {qui_gagne(grille_partie1)} a gagné.")
    else: print(f"\n> FIN : Pas de gagnant.")
    """

    J1 = Joueur()
    print(f"\nJ1.pseudo = {J1.pseudo}")
    J2 = Joueur()

if __name__ == "__main__" : programme() #on appelle le programme uniquement si ce fichier spécifiquement a été exécuté