# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:46:13 2019

@author: alyci
"""

import Simulation as sim

x, y, z = sim.read_file(7862)
t = []
n = 0
while n < len(x) - 1:
    t.append(n/1000)
    n += 1
p = sim.tilt(x, y, z)
sim.plot_p(t, p, 1)