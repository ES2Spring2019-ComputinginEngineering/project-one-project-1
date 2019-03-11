import Simulation as sim

x, y, z = sim.read_file(656)

pos = sim.tilt(x, y, z)

run_time = len(pos)/100

t = sim.create_list_of_times(pos)

sim.plot_p(t, pos, run_time)

x, y, z = sim.read_file(302)

pos = sim.tilt(x, y, z)

run_time = len(pos)/100

t = sim.create_list_of_times(pos)

sim.plot_p(t, pos, run_time)
