#--------------------------------------
#--------------- IMPORT ---------------
#--------------------------------------

from Morpion_simple import *
#from pygame import *


#--------------------------------------
#--------------- GLOBAL ---------------
#--------------------------------------
class Joueur:
    """Désigne les joueurs du Morpion
    Attributes :
        pseudo [str] : pseudo du joueur

    Methods :

    """

    def __init__(self): #constructeur
        self.pseudo = str(input("Quelle est votre pseudo ? : "))
        self.forme_pref = str(input("Quelle est votre forme préféré ? X/O : "))

    def changer_pseudo(self):
        self.pseudo = str(input("Quelle est votre nouveau pseudo ? : "))

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

    J1 = Joueur(); print(J1.__doc__) #affiche le paragraphe de documentation de la class de la variable J1
    J1.pseudo = "antonin"; print(f"pseudo J1 = {J1.pseudo}\n")


if __name__ == "__main__" : programme() #on appelle le programme uniquement si ce fichier spécifiquement a été exécuté