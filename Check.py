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

# print(sim.find_period(p))

"""import math
import Simulation as sim

g = -9.81
L = 1

run_time = 5
init_ang_pos = (math.pi)/6
init_ang_vel = 0
init_ang_accel = (g/L) * math.sin(init_ang_pos)

# lists that will be appended
list_of_times = [0]
ang_pos = [init_ang_pos]
ang_vel = [init_ang_vel]
ang_accel = [init_ang_accel]

sim.pendulum_values(run_time, init_ang_pos, init_ang_vel, g, L,
                           list_of_times, ang_pos, ang_vel, ang_accel)
sim.plot_pva(list_of_times, ang_pos, ang_vel, ang_accel, run_time)
print(sim.find_period(ang_pos))"""