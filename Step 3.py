from microbit import *
import math

g = -9.81
L = 1
# float(input("What is the length of this pendulum in meters? "))
dt = .0001

def tilt(x, y, z):
    # xradians = math.atan2(x, math.sqrt(y**2 + z**2))
    yradians = math.atan2(y, math.sqrt(x**2 + z**2))
    return yradians

def pendulum_values(run_time, init_ang_pos, init_ang_vel, time0):
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

def all_pendulum_values_creation(array, name, m):
    filename = name + str(m) + ".csv"
    file = open(filename, "w+")
    for x in array:
        file.write(x + "\n")
    file.close()
    return

while True:
    m = 0
    if button_a.is_pressed():
        n = 0
        time0 = running_time()
        while ang_pos[n] != ang_pos[n-1]:
            x = accelerometer.get_x()
            y = accelerometer.get_y()
            z = accelerometer.get_z()

            # change back to have user input run time
            run_time = 20
            init_ang_pos = tilt(x, y, z)  # this is coming from the microbit
            # have time = 0 be when button is released when pendulum is released
            init_ang_vel = 0
            init_ang_accel = (g/L) * math.sin(init_ang_pos)

            # lists that will be appended
            list_of_times = [0]
            ang_pos = [init_ang_pos]
            ang_vel = [init_ang_vel]
            ang_accel = [init_ang_accel]

            pendulum_values(run_time, init_ang_pos, init_ang_vel, time0)

            n += 1

        all_pendulum_values_creation(list_of_times, "time", m)
        all_pendulum_values_creation(ang_pos, "position", m)
        all_pendulum_values_creation(ang_vel, "velocity", m)
        all_pendulum_values_creation(ang_accel, "acceleration", m)

        m += 1