import soundfile as sf
import os 
import numpy as np
import matplotlib.pyplot as plt

olsa_dir = os.path.relpath("./scenes/sounds/OLSA_dithered")
pause_dur = 3 #Duration of pause 
num_sent = 3 #Number of sentences 
files = os.listdir(olsa_dir)
sent_out_file_name = "sent_example_1"
noise_out_file_name = "noise_example_1"

noise_file = files[-1]
noise, fs_noise = sf.read(os.path.join(olsa_dir, noise_file))
noise_len = len(noise)
print(files[-1])

allsentences = np.empty((1, 2))
allnoise = np.empty((1, 2))

for file in files[0:num_sent]:
    sentence, fs = sf.read(os.path.join(olsa_dir, file))
    sentence_len = len(sentence)
    offset = int((noise_len - sentence_len) / 2)
    sentence_padded = np.zeros((noise_len,2))
    sentence_padded[offset:offset+sentence_len,:] = sentence

    allsentences = np.vstack((allsentences, np.zeros((int(pause_dur*fs), 2)), sentence_padded))
    allnoise = np.vstack((allnoise, noise))

sf.write(f"./scenes/sounds/OlSA_gen/{sent_out_file_name}.wav", allsentences, fs)
sf.write(f"./scenes/sounds/OlSA_gen/{noise_out_file_name}.wav", allnoise, fs_noise)

data, fs = sf.read("./scenes/sounds/OlSA_gen/sent_example_1.wav")
noise, fs = sf.read("./scenes/sounds/OlSA_gen/noise_example_1.wav")

plt.plot(noise)
plt.plot(data)
plt.show()
