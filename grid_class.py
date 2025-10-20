#!/usr/bin/env python
#  -*- coding: utf-8 -*-

class Grid:
    size = 0

    # détermination de la liste des lettres utilisées pour identifier les colonnes :
    letters = []

    # différents états possibles pour une case de la grille de jeu
    sea, missed_shot, hit_shot, sunk_shot = 0, 0, 0, 0
    # représentation du contenu de ces différents états possible pour une case
    # (tableau indexé par chacun de ces états)
    square_state_repr = []
    played_shots = []

    def __init__(self):
        self.size = 10
        # détermination de la liste des lettres utilisées pour identifier les colonnes :
        self.letters = [chr(letter_code) for letter_code in range(ord('A'), ord('A') + self.size)]
        # différents états possibles pour une case de la grille de jeu
        self.sea, self.missed_shot, self.hit_shot, self.sunk_shot = 0, 1, 2, 3
        # représentation du contenu de ces différents états possible pour une case
        # (tableau indexé par chacun de ces états)
        self.square_state_repr = [' ', 'X', '#', '-']
        self.played_shots = []

    def grid_square_state(self, coord, ship):
        """Retourne l'état de la case coord de la grille
           (cf. constantes SEA, MISSED_SHOT, HIT_SHOT, SUNK_SHOT)."""

        if coord in self.played_shots:
            square_ship = ship.get_ship_by_coord(coord)
            if square_ship:
                square_state = self.sunk_shot if ship.ship_is_sunk() else self.hit_shot
            else:
                square_state = self.missed_shot
        else:
            square_state = self.sea

        return square_state

    def display_grid(self):
        """
        Usage : Affichage de la grille de jeu.
        :rtype: None
        """

        print('    ', end='')
        for x in range(self.size):
            letter = self.letters[x]
            print(' {}  '.format(letter), end='')
        print()
        print('  ', '+---' * self.size + '+')
        for line_no in range(1, self.size + 1):
            print('{:>2} |'.format(line_no), end='')
            for column_no in range(1, self.size + 1):
                coord = (line_no, column_no)
                square_state = self.grid_square_state(coord)
                state_str = self.square_state_repr[square_state]
                print(' {} |'.format(state_str), end='')
            print()
            print('  ', '+---' * self.size + '+')