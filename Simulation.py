import math
import matplotlib.pyplot as plt

dt = .0001

def pendulum_values(run_time, init_ang_pos, init_ang_vel, g, L,
                    list_of_times, ang_pos, ang_vel, ang_accel):
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
        i += 1
    return

def plot(list_of_times, ang_pos, ang_vel, ang_accel):
    plt.figure(figsize = (12, 12))

    plt.subplot(5, 1, 1)
    plt.plot(list_of_times, ang_pos, 'r-')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Position (radians)")
    plt.title("Angular Position vs. Time")
    plt.xlim(0, 20)
    plt.grid()

    plt.subplot(5, 1, 3)
    plt.plot(list_of_times, ang_vel, 'b-')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Velocity (radians/second)")
    plt.title("Angular Velocity vs. Time")
    plt.xlim(0, 20)
    plt.grid()

    plt.subplot(5, 1, 5)
    plt.plot(list_of_times, ang_accel, 'g-')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Acceleration (radians/second/second)")
    plt.title("Angular Acceleration vs. Time")
    plt.xlim(0, 20)
    plt.grid()
    return