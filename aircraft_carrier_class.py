#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import ship_class

class AircraftCarrier(ship_class.Ship):
    dimensions = 5
    ship_type = "Aircraft carrier"
    coord = (0, 0)
    hit = False

    def __init__(self, dimensions, name, coord, hit):
        """

        :param dimensions:
        :param name:
        :param coord:
        :param hit:
        """
        super().__init__(dimensions, name, coord, hit)