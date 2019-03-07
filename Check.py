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

sim.pendulum_values(run_time, init_ang_pos, init_ang_vel, g, L,
                           list_of_times, ang_pos, ang_vel, ang_accel)

def find_period(pos):
    i = 1
    MAX = []
    ang_pos_peaks = sim.find_peaks(ang_pos)
    while i < len(ang_pos_peaks):
        MAX.append((ang_pos_peaks[i])-(ang_pos_peaks[i-1]))
        i += 1
    period = sum(MAX)/len(MAX)
    return period

period = find_period(ang_pos)
print(period)
