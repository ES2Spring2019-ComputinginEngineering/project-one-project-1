import math
import Simulation

g = -9.81
L = 1

run_time = 20
init_ang_pos = (math.pi)/6
init_ang_vel = 0
init_ang_accel = (g/L) * math.sin(init_ang_pos)

# lists that will be appended
list_of_times = [0]
ang_pos = [init_ang_pos]
ang_vel = [init_ang_vel]
ang_accel = [init_ang_accel]

Simulation.pendulum_values(run_time, init_ang_pos, init_ang_vel, g, L,
                           list_of_times, ang_pos, ang_vel, ang_accel)
Simulation.plot_pva(list_of_times, ang_pos, ang_vel, ang_accel)