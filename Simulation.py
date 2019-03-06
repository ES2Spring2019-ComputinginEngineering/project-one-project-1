import math
import matplotlib.pyplot as plt
import scipy.signal as sig

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

def plot_pva(list_of_times, ang_pos, ang_vel, ang_accel, run_time):
    plt.figure(figsize=(12, 12))

    plt.subplot(5, 1, 1)
    plt.plot(list_of_times, ang_pos, 'r-')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Position (radians)")
    plt.title("Angular Position vs. Time")
    plt.xlim(0, run_time)
    plt.grid()

    plt.subplot(5, 1, 3)
    plt.plot(list_of_times, ang_vel, 'b-')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Velocity (radians/second)")
    plt.title("Angular Velocity vs. Time")
    plt.xlim(0, run_time)
    plt.grid()

    plt.subplot(5, 1, 5)
    plt.plot(list_of_times, ang_accel, 'g-')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angular Acceleration (radians/second/second)")
    plt.title("Angular Acceleration vs. Time")
    plt.xlim(0, run_time)
    plt.grid()
    return

# returns an array of a median filtered y
def apply_filter(y):
    y_filt = sig.medfilt(y)
    return y_filt

#returns the indices in which y has peaks
def find_peaks(y):
    y_pks, _ = sig.find_peaks(y)
    return y_pks

def plot_filtered(list_of_times, y, y_noisy, y_filt, y_noisy_filt,
                  y_pks, y_noisy_pks, y_filt_pks, y_noisy_filt_pks):
    plt.subplot(2, 2, 1)
    for x in y_pks:
        plt.plot(list_of_times, y, 'r-', list_of_times[x], y[x], 'b.')
    plt.title("Original")

    plt.subplot(2, 2, 2)
    for x in y_noisy_pks:
        plt.plot(list_of_times, y_noisy, 'r-', list_of_times[x], y[x], 'b.')
    plt.title("Noisy")

    plt.subplot(2, 2, 3)
    for x in y_filt_pks:
        plt.plot(list_of_times, y_filt, 'r-', list_of_times[x], y[x], 'b.')
    plt.title("Original Median Filtered")

    plt.subplot(2, 2, 4)
    for x in y_noisy_filt_pks:
        plt.plot(list_of_times, y_noisy_filt, 'r-', list_of_times[x], y[x],
                 'b.')
    plt.title("Noisy Median Filtered")

    plt.tight_layout()
    plt.show()
    return

def read_file(m):
    x = []  # will be time, pos, vel, or accel; values collected by microbit
    file = open("Data" + str(m) + ".csv")
    for line in file:
        data_pt = line.strip()
        array.append(float(data_pt))
    file.close()
    return array

def plot_p(list_of_times, pos, run_time):
    plt.figure(figsize=(12, 12))

    plt.plot(list_of_times, pos, 'm-')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (radians)")
    plt.title("Position vs. Time")
    plt.xlim(0, run_time)
    plt.grid()
    return

def tilt(x, y, z):
    yradians = math.atan2(y, math.sqrt(x**2 + z**2))
    return yradians
