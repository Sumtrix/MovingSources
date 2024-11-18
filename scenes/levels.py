import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt


def rms(signal):
    return np.sqrt(np.mean(signal**2))

def getLevel(signal):
    return round(10 * np.log10(rms(signal)), 2)

def genWNoise(level, len, ch=1):
    noise = np.random.normal(0, 1, (len, ch))
    target_rms = 10**(level / 10)
    noise = noise * (target_rms / rms(noise))
    return noise


signal, fs = sf.read("./scenes/sounds/jazzclub-piano1.wav")
level = getLevel(signal)
print(level)

noise = genWNoise(level, fs)
nlevel = getLevel(noise)
print(nlevel)

sf.write("./scenes/sounds/gen_white_noise.wav", noise, fs)
