from microbit import *
import math
import Microbit_pendulum as mp

g = -9.81
L = 1
# float(input("What is the length of this pendulum in meters? "))

m = 0
time0 = running_time()
# change back to have user input run time
run_time = 5
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    init_ang_pos = mp.tilt(x, y, z)  # this is coming from the microbit
    init_ang_vel = 0
    init_ang_accel = (g/L) * math.sin(init_ang_pos)

    # lists that will be appended
    list_of_times = [0]
    ang_pos = [init_ang_pos]
    ang_vel = [init_ang_vel]
    ang_accel = [init_ang_accel]

    mp.pendulum_values(run_time, init_ang_pos, init_ang_vel, time0, m,
                       list_of_times, x, y, z, ang_pos, ang_vel, ang_accel,
                       g, L)

    mp.all_pendulum_values_creation("time", list_of_times, m)
    mp.all_pendulum_values_creation("position", ang_pos, m)
    mp.all_pendulum_values_creation("velocity", ang_vel, m)
    mp.all_pendulum_values_creation("acceleration", ang_accel, m)

    m += 1