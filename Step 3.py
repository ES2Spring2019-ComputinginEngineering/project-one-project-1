import microbit
import random

# collect data from microbit accelerometer and
m = random.randint(0, 9999)
filename = "Data" + str(m) + ".csv"
file = open(filename, 'w')
while True:
    x = str(microbit.accelerometer.get_x())
    y = str(microbit.accelerometer.get_y())
    z = str(microbit.accelerometer.get_z())
    file.write(x + ',' + y + ',' + z + "\n")
file.close()
