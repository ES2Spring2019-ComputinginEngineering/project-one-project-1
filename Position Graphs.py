import math
import Simulation as sim

g = -9.81
L = 1

run_time = 5
init_ang_pos = (math.pi)/6
init_ang_vel = 0
init_ang_accel = (g/L) * math.sin(init_ang_pos)

# lists that will be appended
list_of_times = [0]
ang_pos = [init_ang_pos]
ang_vel = [init_ang_vel]
ang_accel = [init_ang_accel]

m = input("What run trial would you like to use? ")

sim.pendulum_values(run_time, init_ang_pos, init_ang_vel, g, L,
                           list_of_times, ang_pos, ang_vel, ang_accel)

x, y, z = sim.read_file(m)
run_time = (len(x)/1000)

pos = sim.tilt(x, y, z)

ang_pos_filt = sim.apply_filter(ang_pos)
pos_filt = sim.apply_filter(pos)

ang_pos_peaks = sim.find_peaks(ang_pos_filt)
pos_peaks = sim.find_peaks(pos)
ang_pos_filt_peaks = sim.find_peaks(ang_pos_filt)
pos_filt_peaks = sim.find_peaks(pos_filt)

sim.plot_filtered(list_of_times, ang_pos, pos, ang_pos_filt, pos_filt,
                  ang_pos_peaks, pos_peaks, ang_pos_filt_peaks, pos_filt_peaks, run_time)