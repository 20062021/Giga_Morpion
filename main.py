#--------------------------------------
#--------------- IMPORT ---------------
#--------------------------------------
import inspect

from QuiGagne import *
#from pygame import *



#--------------------------------------
#-------------- FUNCTIONS -------------
#--------------------------------------
def affiche_la_grille(grille:Tgrille): #affichage en ligne
    ligne1 = grille[0]
    ligne2 = grille[1]
    ligne3 = grille[2]

    grille = [ligne1, ligne2, ligne3]

    for decoupage_ligne in grille:
        print(f"{decoupage_ligne[0]} {decoupage_ligne[1]} {decoupage_ligne[2]}")



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

    affiche_la_grille(grille_fini)
    QuiGagne(grille_fini)
    affiche_la_grille(grille_fini2)
    QuiGagne(grille_fini2)
    affiche_la_grille(grille_fini3)
    QuiGagne(grille_fini3)
    affiche_la_grille(grille_fini4)
    QuiGagne(grille_fini4)

if __name__ == "__main__" : programme() #on appelle le programme uniquement si ce fichier spécifiquement a été exécuté