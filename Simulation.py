import math
import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np

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
                  y_pks, y_noisy_pks, y_filt_pks, y_noisy_filt_pks, run_time):
    plt.figure(figsize=(12, 12))
    
    plt.subplot(2, 2, 1)
    for x in y_pks:
        plt.plot(list_of_times, y, 'r-', list_of_times[x], y[x], 'b.')
    plt.title("Original")
    plt.xlim(0, run_time)

    plt.subplot(2, 2, 2)
    for x in y_noisy_pks:
        plt.plot(list_of_times[:len(y_noisy)], y_noisy, 'r-', list_of_times[x],
                 y[x], 'b.')
    plt.title("Noisy")
    plt.xlim(0, run_time)

    plt.subplot(2, 2, 3)
    for x in y_filt_pks:
        plt.plot(list_of_times, y_filt, 'r-', list_of_times[x], y[x], 'b.')
    plt.title("Original Median Filtered")
    plt.xlim(0, run_time)

    plt.subplot(2, 2, 4)
    for x in y_noisy_filt_pks:
        plt.plot(list_of_times[:len(y_noisy)], y_noisy_filt, 'r-',
                 list_of_times[x], y[x], 'b.')
    plt.title("Noisy Median Filtered")
    plt.xlim(0, run_time)

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

def find_period(pos):
    i = 1
    MAX = []
    pos_peaks = find_peaks(pos)
    pos = filter_peaks(pos, pos_peaks)
    while i < len(pos_peaks):
        MAX.append((pos_peaks[i])-(pos_peaks[i-1]))
        i += 1
    period = sum(MAX)/len(MAX)
    return period

def filter_peaks(pos_peaks):
    filter_range(pos_peaks)
    if peaks != len(pos(peaks)):
        filter_range(pos_peaks)
    med_time = np.median(pos_peaks)
    for x in pos_peaks:
        if (x < (med_time - 0.2)) or (x > (med_time + 0.2)):
            remove(x)
    peaks = np.ndarray.size(pos_peaks)
    return
    
def filter_range(pos_peaks):
    i = 1
    MIN, MAX = 0
    array = []
    while i < np.ndarray.size(pos_peaks):
        if (array == []) and ((pos_peaks[i] - pos_peaks[i-1]) <= 0.01): 
            array.append(pos_peaks[i-1])
            array.append(pos_peaks[i])
            MIN = i-1
        elif ((pos_peaks[i] - pos_peaks[i-1]) <= 0.01) and ((pos_peaks[i-1] - array[i]) <= 0.01):
                array.append(pos_peaks[i])
                MAX = i
    med_time = list.median(pos_peaks)
    med_array = find_nearest(array, med_time)
    for x in pos_peaks[MIN:MAX]:
        if x != med_array:
            pos_peaks.remove(x)
    return
    
def find_nearest(array, value):
    array = np.asarray(array)
    i = (abs(array - value)).argmin()
    return array[i]
            
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
        pos[i] == MIN1 or MAX"""