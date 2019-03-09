import Simulation as sim

x, y, z = sim.read_file(154)

pos = sim.tilt(x, y, z)

run_time = len(pos)/100

t = sim.create_list_of_times(pos)

sim.plot_p(t, pos, run_time)

x, y, z = sim.read_file()

pos = sim.tilt(x, y, z)

run_time = len(pos)/100

t = sim.create_list_of_times(pos)

sim.plot_p(t, pos, run_time)
