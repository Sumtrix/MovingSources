import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

data, fs = sf.read("C:/Users/annik/OneDrive/Desktop/Projekt/tascar/S0N0rot.wav")

print(data.shape)

plt.plot(data)
plt.show()