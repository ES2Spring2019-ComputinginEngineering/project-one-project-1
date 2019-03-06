from microbit import *
import math
import random

dt = .0001
run_time = 5

# input data from microbit accelerometer to calculate and return
# tilt of y-axis in radians
def tilt(x, y, z):
    yradians = math.atan2(y, math.sqrt(x**2 + z**2))
    return yradians

# input file and write
def pendulum_values(file):
        i = 1
        time0 = running_time()
        while i <= (run_time / dt):
            time = running_time() - time0
            ang_pos = tilt(x, y, z)
            file.write(str(time) + ' ' + str(ang_pos) + "\n")
            i += 1
        return

# open file with random name and input time and position
def all_pendulum_values_creation(m):
    filename = "Data" + str(m) + ".csv"
    file = open(filename, "w")
    pendulum_values(file)
    file.close()
    return

# collect data from microbit accelerometer and
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    m = random.randint(0, 9999)
    all_pendulum_values_creation(m)
