# For Period/Length Analysis

import matplotlib.pyplot as plt

length_sim = [.2413, .3556, .2794, .3429, .1651]
# estimated from graphs since function not working
period_simulation = [1, 1.25, 1.125, 1.167, .8]
length_data = [.2413, .3556, .2794, .1651]
period_data = [.6, 1.25, 1.5, 1.125]

# graph for SIMULATION
plt.subplot(3, 1, 1)
plt.plot(length_sim, period_simulation, 'g-')
plt.xlabel("Length of Pendulum (m)")
plt.ylabel("Period of Simulation (s)")
plt.title("Relationship of Length vs Simulation Period")
plt.xscale('log')
plt.yscale('log')
plt.xlim(0, period_simulation)
plt.grid()

# graph for DATA
plt.subplot(3, 1, 3)
plt.plot(length_data, period_data, 'r-')
plt.xlabel("Length of Pendulum (m)")
plt.ylabel("Period of Data (s)")
plt.title("Relationship of Length vs Data Period")
plt.xscale('log')
plt.yscale('log')
plt.xlim(0, period_data)
plt.grid()