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

def plot_pva(list_of_times, ang_pos, ang_vel, ang_accel):
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

def apply_filter(y):
    y_filt = sig.medfilt(y)
    return y_filt

def find_peaks(y):
    y_pks, _ = sig.find_peaks(y)
    return y_pks

def plot_filtered(list_of_times, y, y_noisy, y_filt, y_noisy_filt,
                  y_pks, y_noisy_pks, y_filt_pks, y_noisy_filt_pks):
    plt.subplot(2, 2, 1)
    plt.plot(list_of_times, y, 'r-', list_of_times[y_pks], y[y_pks], 'b.')
    plt.title("Original")

    plt.subplot(2, 2, 2)
    plt.plot(list_of_times, y_noisy, 'r-', list_of_times[y_noisy_pks],
             y[y_noisy_pks], 'b.')
    plt.title("Noisy")

    plt.subplot(2, 2, 3)
    plt.plot(list_of_times, y_filt, 'r-', list_of_times[y_filt_pks],
             y[y_filt_pks], 'b.')
    plt.title("Original Median Filtered")

    plt.subplot(2, 2, 4)
    plt.plot(list_of_times, y_noisy_filt, 'r-',
             list_of_times[y_noisy_filt_pks], y[y_noisy_filt_pks], 'b.')
    plt.title("Noisy Median Filtered")

    plt.tight_layout()
    plt.show()
    return