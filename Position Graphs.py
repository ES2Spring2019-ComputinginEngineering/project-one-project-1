import math
import Simulation as sim

g = -9.81
L = .2413


# lists that will be appended
g = -9.81

m = input("What file number would you like to use? ")
L = sim.length(5)

run_time = 5
init_ang_pos = (math.pi)/6
init_ang_vel = 0
init_ang_accel = (g/L) * math.sin(init_ang_pos)

# lists that will be appended
list_of_times = [0]
ang_pos = [init_ang_pos]
ang_vel = [init_ang_vel]
ang_accel = [init_ang_accel]

sim.pendulum_values(run_time, init_ang_pos, init_ang_vel, g, L,
                           list_of_times, ang_pos, ang_vel, ang_accel)

x, y, z = sim.read_file(m)

pos = sim.tilt(x, y, z)
# pos = pos[:17]

# gets length of pos equal to length of list_of_times/3
"""pos.pop()
pos.pop()
pos.pop()"""

list_of_times1 = sim.create_list_of_times(pos)
# sim.plot_p(list_of_times[0::10], pos, run_time)

ang_pos_filt = sim.apply_filter(ang_pos)
pos_filt = sim.apply_filter(pos)

ang_pos_peaks = sim.find_peaks(ang_pos_filt)
pos_peaks = sim.find_peaks(pos)
ang_pos_filt_peaks = sim.find_peaks(ang_pos_filt)
pos_filt_peaks = sim.find_peaks(pos_filt)

sim.plot_filtered(list_of_times, list_of_times1, ang_pos, pos, ang_pos_filt, pos_filt,
                  ang_pos_peaks, pos_peaks, ang_pos_filt_peaks, pos_filt_peaks, run_time)

# print(sim.find_period(pos))