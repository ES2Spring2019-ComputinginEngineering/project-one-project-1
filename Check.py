import Simulation as sim
import math

x, y, z = sim.read_file(792)
pos = sim.tilt(x, y, z)
run_time = len(pos)/100
t = sim.create_list_of_times(pos)
sim.plot_p(t, pos, run_time)

x, y, z = sim.read_file(951)
pos = sim.tilt(x, y, z)
run_time = len(pos)/100
t = sim.create_list_of_times(pos)
sim.plot_p(t, pos, run_time)

x, y, z = sim.read_file(912)
pos = sim.tilt(x, y, z)
run_time = len(pos)/100
t = sim.create_list_of_times(pos)
sim.plot_p(t, pos, run_time)

g = -9.81
L = .1651

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
sim.plot_pva(list_of_times, ang_pos, ang_vel, ang_accel, run_time)