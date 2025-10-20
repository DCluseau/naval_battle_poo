#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import ship_class

class TorpedoBoat(ship_class.Ship):

    def __init__(self):
        """

        """
        super().__init__(5, "Torpedo Boat", (0, 0), False)