from microbit import *
import math

g = -9.81
L = 1
# float(input("What is the length of this pendulum in meters? "))
dt = .0001

def tilt(x, y, z):  # getting data from accelerometer in microbit
    yradians = math.atan2(y, math.sqrt(x**2 + z**2))
    return yradians  # gets angle; main input for angular kinematic equations

def position_values(run_time, list_of_times, ang_pos, x, y, z):
        i = 1
        while i <= (run_time / dt):
            list_of_times.append(running_time())
            new_ang_pos = tilt(x, y, z)
            ang_pos.append(new_ang_pos)
            i += 1
        for x in range(len(list_of_times), 1, -1):
            list_of_times[x] -= list_of_times[1]
        return

# change back to have user input run time
run_time = 5
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    init_ang_pos = tilt(x, y, z)

    # lists that will be appended
    list_of_times = [0]
    ang_pos = [init_ang_pos]

    position_values(run_time, list_of_times, ang_pos, x, y, z)