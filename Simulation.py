import math
import matplotlib.pyplot as plt
import scipy.signal as sig

dt = .001

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
    plt.figure(figsize=(12, 12))
    
    plt.subplot(2, 2, 1)
    for x in y_pks:
        plt.plot(list_of_times, y, 'r-', list_of_times[x], y[x], 'b.')
    plt.title("Original")
    # plt.xlim(0, run_time)

    plt.subplot(2, 2, 2)
    for x in y_noisy_pks:
        plt.plot(list_of_times[:len(y_noisy)], y_noisy, 'r-', list_of_times[x],
                 y[x], 'b.')
    plt.title("Noisy")
    # plt.xlim(0, run_time)

    plt.subplot(2, 2, 3)
    for x in y_filt_pks:
        plt.plot(list_of_times, y_filt, 'r-', list_of_times[x], y[x], 'b.')
    plt.title("Original Median Filtered")
    # plt.xlim(0, run_time)

    plt.subplot(2, 2, 4)
    for x in y_noisy_filt_pks:
        plt.plot(list_of_times[:len(y_noisy)], y_noisy_filt, 'r-',
                 list_of_times[x], y[x], 'b.')
    plt.title("Noisy Median Filtered")
    # plt.xlim(0, run_time)

    plt.tight_layout()
    plt.show()
    return

def read_file(m):
    x = []
    y = []
    z = []
    delimiter = ','
    filename = "Data" + str(m) + ".csv"
    file = open(filename, 'r')
    for line in file:
        s = line.split(delimiter)
        x.append(float(s[0]))
        y.append(float(s[1]))
        z.append(float(s[2]))
    file.close()
    return x, y, z

def plot_p(list_of_times, pos, run_time):
    plt.figure(figsize=(12, 12))

    plt.plot(list_of_times, pos, 'm-')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (radians)")
    plt.title("Position vs. Time")
    plt.grid()
    plt.xlim(0, run_time)
    return

def tilt(x, y, z):
    yradians = []
    for n in range(0, len(x) - 1):
        ytilt = math.atan2(y[n], math.sqrt(x[n]**2 + z[n]**2))
        yradians.append(ytilt)
    return yradians

"""def find_period(pos):
    i, period = 0
    MIN, MAX = []
    while i < len(pos):
        if pos[i] == min(pos):
            MIN.append = i
        elif pos[i] == max(pos):
            MAX.append = i
    filter_period(MAX, MIN)
        period = (MAX - MIN) * 2
    return period

def filter_period(MAX, MIN, pos):
    MAX1, MIN1 = []
    if MAX[i] - MAX[i-1] range:
        average
        MAX1.append
        else, append
    if MIN[i] - MIN[i-1] range:
        average
        MIN1.append
        else, append
    while loop:
        pos[i] == MIN1 or MAX
    
    
def find_avg_period(p1, p2, p3, p4, p5):
    pp1, pp2, pp3, pp4, pp5, avg = 0
    pp1 = find_period(p1)
    pp2 = find_period(p2)
    pp3 = find_period(p3)
    pp4 = find_period(p4)
    pp5 = find_period(p5)
    avg = (sum(pp1, pp2, pp3, pp4, pp5))/5
    return avG"""