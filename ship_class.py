#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from naval_battle_no_poo import ships_list


class Ship:
    ships_list = []

    def __init__(self, dimensions, name, coord, hit):
        """

        :param dimensions:
        :param name:
        :param coord:
        :param hit:
        """
        self.dimensions = dimensions
        self.ship_type = name
        self.coord = coord
        self.hit = hit
        Ship.ships_list.append(self)

    def get_ship_by_coord(self):
        """Construction d'un dictionnaire permettant de connaitre l'éventuel bateau
       présent sur chaque case de la grille.

        :rtype: dict[Any, Any]
        :return: dictionnaire dont chaque clé est les coordonnées
                 d'une case d'un navire, et sa valeur le navire en question
        """

        return {ship_coord: ship for ship in self.ships_list[ships_list]
                                 for ship_coord in ship}

    def ship_is_hit(self, shot_coord):
        """Indique si un navire est touché par un tir aux coordonnées indiquées.
        :rtype: bool
        """
        return shot_coord in self.ships_list

    def ship_is_sunk(self):
        """Indique si un navire est coulé.
        :rtype: bool
        :return:
        """
        return not any(self.ships_list.values())

    def analyze_shot(self, shot_coord):
        """Analyse les conséquences d'un tir sur un navire :

        - teste si le navire est touché par le tir, le signale et le mémorise alors
        - teste si le navire est ainsi coulé, le signale dans ce cas,
          et le supprime de la flotte

        :param shot_coord:
        """
        if self.ship_is_hit(shot_coord):
            print('Un navire a été touché par votre tir !')
            self.ships_list[shot_coord] = False
            if self.ship_is_sunk():
                print('Le navire touché est coulé !!')
                # le navire est supprimé de la flotte
                self.ships_list.remove(shot_coord)