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
    y_pks.astype(int)
    return y_pks

def plot_filtered(list_of_times, list_of_times1, y, y_noisy, y_filt, y_noisy_filt,
                  y_pks, y_noisy_pks, y_filt_pks, y_noisy_filt_pks, run_time):
    plt.figure(figsize=(12, 12))
    
    plt.subplot(2, 2, 1)
    for x in y_pks:
        plt.plot(list_of_times, y, 'r-', list_of_times[x], y[x], 'b.')
    plt.title("Original")
    plt.xlim(0, run_time)

    plt.subplot(2, 2, 2)
    for x in y_noisy_pks:
        plt.plot(list_of_times1, y_noisy, 'r-', list_of_times1[x],
                 y_noisy[x], 'b.')
    plt.title("Noisy")
    plt.xlim(0, run_time)

    plt.subplot(2, 2, 3)
    for x in y_filt_pks:
        plt.plot(list_of_times, y_filt, 'r-', list_of_times[x], y_filt[x], 'b.')
    plt.title("Original Median Filtered")
    plt.xlim(0, run_time)

    plt.subplot(2, 2, 4)
    for x in y_noisy_filt_pks:
        plt.plot(list_of_times1, y_noisy_filt, 'r-',
                 list_of_times1[x], y_noisy_filt[x], 'b.')
    plt.title("Noisy Filtered")
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
    pos_peaks = list(sig.find_peaks(pos))
    pos = list(filter_peaks(pos_peaks))
    while i < len(pos_peaks):
        MAX.append((pos[i])-(pos[i-1]))
        i += 1
    period = sum(MAX)/len(MAX)
    return period

def filter_peaks(pos_peaks):
    position_peaks = list(pos_peaks)
    # filter_range(pos_peaks)
    med_time = np.median(pos_peaks)
    for x in pos_peaks:
        if (x < (med_time - 0.2)) or (x > (med_time + 0.2)):
            position_peaks.remove(x)
    return position_peaks
    
def filter_range(pos_peaks):
    i = 1
    MIN = 0
    MAX = 0
    array = []
    position_peaks = list(pos_peaks)
    while i < len(position_peaks):
        if (array == []) and ((position_peaks[i] - position_peaks[i-1]) <= 0.01): 
            array.append(pos_peaks[i-1])
            array.append(pos_peaks[i])
            MIN = i-1
        elif ((position_peaks[i] - position_peaks[i-1]) <= 0.01) and ((position_peaks[i-1] - array[i]) <= 0.01):
            array.append(pos_peaks[i])
            MAX = i
        else:
            array.append(0)
        i += 1
    n = 0
    j = 0
    for j in array:
        if j == n:
            array.remove(j)
    med_time = np.median(pos_peaks)
    med_time = np.asarray(med_time)
    med_array = find_nearest(array, med_time)
    for x in position_peaks[MIN:MAX]:
        if x != med_array:
            pos_peaks.remove(x)
    return pos_peaks
    
def find_nearest(arraya, value):
    arrayb = (np.asarray(arraya) - value)
    j = np.argmin(arrayb)
    i = list(j)
    return i

def create_list_of_times(pos):
    i = 0
    n = []
    while i < len(pos):
        n.append(i/3)
        i += 1
    return n

def length(m):
    length = 0
    if m == 1:
        length = 0.241
    elif m == 2:
        length = 0.356
    elif m == 3:
        length = 0.279
    elif m == 4:
        length = 0.343
    elif m == 5:
        length = 0.165
    else:
        print("not valid input")
    # print(m, length)
    return length