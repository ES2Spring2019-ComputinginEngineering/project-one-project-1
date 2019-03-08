import microbit
import random

# collect data from microbit accelerometer and
m = random.randint(0, 999)
filename = "Data" + str(m) + ".csv"
file = open(filename, 'w')
n = 0
while n < 505:
    microbit.sleep(10)
    x = str(microbit.accelerometer.get_x())
    y = str(microbit.accelerometer.get_y())
    z = str(microbit.accelerometer.get_z())
    file.write(x + ',' + y + ',' + z + "\n")
    n += 1
file.close()