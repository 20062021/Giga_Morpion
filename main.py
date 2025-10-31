#--------------------------------------
#--------------- IMPORT ---------------
#--------------------------------------

from Morpion_simple import *
MS = MorpionSimple() #creation d'un alias pour la class MorpionSimple

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

    def __init__(self): #constructeur
        self.__pseudo:str = '' #attribut privé

    @property #accesseur de l'attribut pseudo
    def pseudo(self): return self.__pseudo

    @pseudo.setter #mutateur de l'attribut pseudo
    def pseudo(self, pseudo:str):
        """changer de pseudo"""
        if pseudo not in self.__pseudos:
            self.__pseudo = pseudo; Joueur.__pseudos.append(pseudo)
        else:
            print(f"\n> ATTENTION : '{pseudo}' est déjà prit.\n")
            print(f"liste des pseudos déjà prit : {self.__pseudos}")
            self.pseudo = input("Choisissez un autre pseudo : ") #recursif

    @classmethod #méthode de class
    def avoir_pseudos(cls):
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
    afficher_la_grille(partie_classique()[0])
    """

    """
    J1 = Joueur()
    pseudo:str = str(input("Choisissez un pseudo : "))
    J1.pseudo = pseudo

    print(f"> DEBUG : Joueur.avoir_pseudos() = {Joueur.avoir_pseudos()}")

    J2 = Joueur()
    pseudo: str = str(input("Choisissez un pseudo : "))
    J2.pseudo = pseudo

    print(f"> DEBUG : Joueur.avoir_pseudos() = {Joueur.avoir_pseudos()}")
    """

    grille_jeu_1 = MS
    gj1 = grille_jeu_1 #création d'un alias pour l'instance grille_jeu_1 de la class MorpionSimple
    gj1.afficher_la_grille(gj1.grille)
    gj1.afficher_la_grille(gj1.partie_classique()[0])

if __name__ == "__main__" : programme() #on appelle le programme uniquement si ce fichier spécifiquement a été exécuté