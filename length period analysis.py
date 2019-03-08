# For Period/Length Analysis

import matplotlib as plt

length = ["""lengths for each trial"""]
period_simulation = ["""periods corresponding to each length from the trials"""]
period_data = ["""periods corresponding to each length from the trials"""]

# graph for SIMULATION
plt.subplot(3, 1, 1)
plt.plot(length, period_simulation, 'g-')
plt.xlabel("Length of Pendulum (m)")
plt.ylabel("Period of Simulation (s)")
plt.title("Relationship of Length vs Simulation Period")
plt.xscale('log')
plt.yscale('log')
plt.xlim(0, period_data)
plt.grid()

# graph for DATA
plt.subplot(3, 1, 3)
plt.plot(length, period_data, 'r-')
plt.xlabel("Length of Pendulum (m)")
plt.ylabel("Period of Data (s)")
plt.title("Relationship of Length vs Data Period")
plt.xscale('log')
plt.yscale('log')
plt.xlim(0, period_data)
plt.grid()