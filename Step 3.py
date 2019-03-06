from microbit import *
import random

# collect data from microbit accelerometer and
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    m = random.randint(0, 9999)

    filename = "Data" + str(m) + ".csv"
    file = open(filename, "w")
    file.write(str(x) + ',' + str(y) + ',' + str(z) + "\n")
    file.close()
