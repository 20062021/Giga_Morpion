from pygame import *

class Giga_Morpion:
    def __init__(self):
        '''GM = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}  # GM Giga Morpion''' #j'ai pensé a faire ça avec un dico
        GM = [[[[None, None, None],
                [None, None, None],
                [None, None, None]], [[None, None, None],
                                      [None, None, None],
                                      [None, None, None]], [[None, None, None],
                                                            [None, None, None],
                                                            [None, None, None]]],
              []]
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
