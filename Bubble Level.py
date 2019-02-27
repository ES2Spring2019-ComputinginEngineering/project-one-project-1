# Bubble Level --- ES2
# Name: Alycia Wong
# Collaboration Statement: I worked with Ben Pradko on this assignment

import microbit
import math

# Use a while loop so that the program runs forever
while True:
    # Define variables as input from accelerometer
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()

    # Calculate the degrees that the microbit is tilting in the x direction
    def calculate_xtilt(x, z):
        degrees_x = math.atan2(x, z) * 180 / math.pi
        return degrees_x

    # Calculate the degrees that the microbit is tilting in the y direction
    def calculate_ytilt(y, z):
        degrees_y = math.atan2(y, z) * 180 / math.pi
        return degrees_y

    # set variables for the degrees the microbit is tilting
    n = calculate_xtilt(x, z)
    m = calculate_ytilt(y, z)

    # Determine the x coordinate on the microbit for different degrees of tilt
    def determine_x(n):
        if(n > -135 and n < 0):
            i = 0
        elif(n > -180 and n <= -135):
            i = 1
        elif (n == 180 or n == 0):
            i = 2
        elif(n >= 135 and n < 180):
            i = 3
        elif(n > 0 and n < 135):
            i = 4
        return i

    # Determine the y coordinate on the microbit for different degrees of tilt
    def determine_y(m):
        if(m > -135 and m < -10):
            j = 0
        elif(m > -170 and m <= -135):
            j = 1
        elif((m >= -180 and m <= -170) or (m >= 170 and m <= 180)
                or (m >= -10 and m <= 10)):
            j = 2
        elif(m >= 135 and m < 170):
            j = 3
        elif(m > 10 and m < 135):
            j = 4
        return j

    # Set variables for the x and y coordinates on the microbit
    i = determine_x(n)
    j = determine_y(m)

    # Display an LED light at the given coordinates on the microbit
    # Intensity: 5
    # Microbit put to sleep and cleared so that there is one steady light
    microbit.display.set_pixel(i, j, 9)
    microbit.sleep(10)
    microbit.display.clear()