from microbit import *
import math

dt = .0001
run_time = 5

# input data from microbit accelerometer to calculate and return
# tilt of y-axis in radians
def tilt(x, y, z):
    yradians = math.atan2(y, math.sqrt(x**2 + z**2))
    return yradians

# input run time, empty arrays, and acclerometer data to calculate
# the angular position of the microbit
def position_values(run_time, list_of_times, ang_pos, x, y, z):
        i = 1
        while i <= (run_time / dt):
            list_of_times.append(running_time())
            new_ang_pos = tilt(x, y, z)
            ang_pos.append(new_ang_pos)
            i += 1
        for n in range(len(list_of_times), 1, -1):
            list_of_times[n] -= list_of_times[1]
        return

# collect data from microbit accelerometer and
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    init_ang_pos = tilt(x, y, z)

    # lists that will be appended
    list_of_times = [0]
    ang_pos = [init_ang_pos]

    position_values(run_time, list_of_times, ang_pos, x, y, z)