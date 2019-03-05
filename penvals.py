# Microbit_pendulum.py

from microbit import *
import math

dt = .0001

def tilt(x, y, z):  # getting data from accelerometer in microbit
    # xradians = math.atan2(x, math.sqrt(y**2 + z**2))
    yradians = math.atan2(y, math.sqrt(x**2 + z**2))
    return yradians  # gets angle; main input for angular kinematic equations


def all_pendulum_values_creation(name, data, m):  # file for data in each run
    # input name defines which value type to look at out of time, pos, vel, and accel
    # input data is the list for that type of value
    # m is trial run number
    filename = name + str(m) + ".csv"
    file = open(filename, "w+")
    for x in data:
        file.write(str(x) + "\n")
    file.close()
    return


def pendulum_values(run_time, init_ang_pos, init_ang_vel, time0, m,
                    list_of_times, x, y, z, ang_pos, ang_vel, ang_accel, g, L):
        i = 1
        while i <= (run_time / dt):
            list_of_times.append(running_time() - time0)
            # with microbit library imported
            new_ang_pos = tilt(x, y, z)
            ang_pos.append(new_ang_pos)
            new_ang_vel = ang_vel[i-1] + dt * ang_accel[i-1]
            ang_vel.append(new_ang_vel)
            new_ang_accel = (g/L) * math.sin(new_ang_pos)
            ang_accel.append(new_ang_accel)
            i += 1
        return