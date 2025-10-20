#!/usr/bin/env python
#  -*- coding: utf-8 -*-




class Ship:
    # dimensions = 0
    # ship_type = ""
    # coord = (0, 0)
    # hit = False
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


    @classmethod
    def get_ship_by_coord(cls, coord):
        """Construction d'un dictionnaire permettant de connaitre l'éventuel bateau
           présent sur chaque case de la grille.

        :return: dictionnaire dont chaque clé est les coordonnées
                 d'une case d'un navire, et sa valeur le navire en question
        """
        ship_found = next((ship for ship in cls.ships_list if ship.coord == coord), None)
        return ship_found

    def ship_is_hit(self, shot_coord):
        """Indique si un navire est touché par un tir aux coordonnées indiquées."""
        return shot_coord in self.ships_list