#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import grid_class
import ship_class
from aircraft_carrier_class import AircraftCarrier
from cruiser_class import Cruiser
from destroyer_class import Destroyer
from submarine_class import Submarine
from torpedo_boat_class import TorpedoBoat

grid = grid_class.Grid()
aircraft_carrier = AircraftCarrier()
cruiser = Cruiser()
destroyer = Destroyer()
submarine = Submarine()
torpedo_boat = TorpedoBoat()


# -------------------------------------------------------------------------- #
# programme principal :                                                      #
# tant que tous les navires ne sont pas coulés, on demande au joueur         #
# d'indiquer une case où il souhaite effectuer un tir                        #
# -------------------------------------------------------------------------- #

ship_found = ship_class.Ship.get_ship_by_coord()
while ship_class.Ship.ships_list:
    grid.display_grid()
    next_shot_coord = grid.ask_coord()
    grid.played_shots.add(next_shot_coord)
    ship_shot = ship_class.Ship.ship_by_coord(next_shot_coord)
    if ship_shot and ship_shot in ship_class.Ship.ships_list:
        ship_class.Ship.analyze_shot(ship_shot, next_shot_coord)
    else:
        print("Votre tir est tombé dans l'eau")
    print()

grid.display_grid()
print('Bravo, vous avez coulé tous les navires')