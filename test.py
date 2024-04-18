from pygame import *

class Giga_Morpion:
    def __init__(self):
        # GM : Giga Morpion
        # j'ai pensé a faire ça avec un dico

        GM = {1:[[None, None, None],
                [None, None, None],
                [None, None, None]],
              2:[[None, None, None],
                [None, None, None],
                [None, None, None]],
              3:[[None, None, None],
                [None, None, None],
                [None, None, None]],
              4:[[None, None, None],
                [None, None, None],
                [None, None, None]],
              5:[[None, None, None],
                [None, None, None],
                [None, None, None]],
              6:[[None, None, None],
                [None, None, None],
                [None, None, None]],
              7:[[None, None, None],
                [None, None, None],
                [None, None, None]],
              8:[[None, None, None],
                [None, None, None],
                [None, None, None]],
              9:[[None, None, None],
                [None, None, None],
                [None, None, None]]}


        GM = [[[[None, None, None],
                [None, None, None],
                [None, None, None]], [[None, None, None],
                                      [None, None, None],
                                      [None, None, None]], [[None, None, None],
                                                            [None, None, None],
                                                            [None, None, None]]],
              [[[None, None, None],
                [None, None, None],
                [None, None, None]], [[None, None, None],
                                      [None, None, None],
                                      [None, None, None]], [[None, None, None],
                                                            [None, None, None],
                                                            [None, None, None]]],
              [[[None, None, None],
                [None, None, None],
                [None, None, None]], [[None, None, None],
                                      [None, None, None],
                                      [None, None, None]], [[None, None, None],
                                                            [None, None, None],
                                                            [None, None, None]]]]  # louis pense faire ça avec des listes
        self.GM = GM
    def __str__(self):
        pass
    def __repr__(self):
        pass







class Morpion:
    def __init__(self):

        self.body = [[], [], [],
                     [], [], [],
                     [], [], []]
