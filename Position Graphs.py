import Simulation as sim

g = -9.81
L = .2413


# lists that will be appended
list_of_times = [0]

m = input("What file number would you like to use? ")

x, y, z = sim.read_file(m)
run_time = (len(x)/1000)

pos = sim.tilt(x, y, z)

sim.plot_p(run_time, pos, run_time)

"""ang_pos_filt = sim.apply_filter(ang_pos)
pos_filt = sim.apply_filter(pos)

ang_pos_peaks = sim.find_peaks(ang_pos_filt)
pos_peaks = sim.find_peaks(pos)
ang_pos_filt_peaks = sim.find_peaks(ang_pos_filt)
pos_filt_peaks = sim.filter_peaks(sim.find_peaks(pos_filt))

sim.plot_filtered(list_of_times, ang_pos, pos, ang_pos_filt, pos_filt,
                  ang_pos_peaks, pos_peaks, ang_pos_filt_peaks, pos_filt_peaks, run_time)"""