import math

g = -9.81
L = 1
dt = .5

run_time = float(input("What would you like the run time of this function to be in seconds? "))
init_ang_pos = (math.pi)/6
init_ang_vel = 0
init_ang_accel = (g/L) * math.sin(init_ang_pos)

# lists that will be appended
list_of_times = [0]
ang_pos = [init_ang_pos]
ang_vel = [init_ang_vel]
ang_accel = [init_ang_accel]

def pendulum_values(run_time, init_ang_pos, init_ang_vel):
    i = 1
    while i <= (run_time / dt):
        time = list_of_times[i-1] + dt
        list_of_times.append(time)
        new_ang_pos = ang_pos[i-1] + dt * ang_vel[i-1]
        ang_pos.append(new_ang_pos)
        new_ang_vel = ang_vel[i-1] + dt * ang_accel[i-1]
        ang_vel.append(new_ang_vel)
        new_ang_accel = (g/L) * math.sin(new_ang_pos)
        ang_accel.append(new_ang_accel)
        print("Time" + str(i) + ", Position = " + str(ang_pos[i]) + ", Velocity = " + str(ang_vel[i]) + ", Acceleration = " + str(ang_accel[i]))
        i += 1
    return "pendulum calculation finished at " + str(time) + " seconds"

print(pendulum_values(run_time, init_ang_pos, init_ang_vel))