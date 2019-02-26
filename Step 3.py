from microbit import *
import math

def tilt(x, y, z):
    # xradians = math.atan2(x, math.sqrt(y**2 + z**2))
    yradians = math.atan2(y, math.sqrt(x**2 + z**2))
    return yradians

while(True):
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    g = -9.81
    L = 1
    # float(input("What is the length of this pendulum in meters? "))
    dt = .0001

    # change back to have user input run time
    run_time = 20
    init_ang_pos = tilt(x, y, z)# this is coming from the microbit
    # have time = 0 be when button is released when pendulum is released
    init_ang_vel = 0
    init_ang_accel = (g/L) * math.sin(init_ang_pos)

    if button_a.is_pressed():
        while True:


    # lists that will be appended
    list_of_times = [0]
    ang_pos = [init_ang_pos]
    ang_vel = [init_ang_vel]
    ang_accel = [init_ang_accel]

    def pendulum_values(run_time, init_ang_pos, init_ang_vel):
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
            print("Time" + str(i) + ", Position = " + str(ang_pos[i]) + ", Velocity = " + str(ang_vel[i]) + ", Acceleration = " + str(ang_accel[i]))
            i += 1
        return "pendulum calculation finished at " + str(time) + " seconds"