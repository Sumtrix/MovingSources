import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = "scenes/paths/S0N0osci60_slow/noise_osci.txt"
data = pd.read_csv(file).to_numpy()
print(data)
t = data[0,:]
x = data[:,1]
y = data[:,2]
    
plt.plot(x, y)
plt.xlim([-1.2, 1.2])
plt.ylim([-1.2, 1.2])
plt.show()