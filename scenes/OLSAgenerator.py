import soundfile as sf
import os 
import numpy as np
import matplotlib.pyplot as plt

olsa_dir = os.path.relpath("./scenes/sounds/OLSA_dithered")
#pause_dur = 3 #Duration of pause 
#num_sent = 3 #Number of sentences 
lens_file = 10      # s
files = os.listdir(olsa_dir)
sent_out_file_name = "sent_example_1"
noise_out_file_name = "noise_example_1"

noise_file = files[-1]
noise, fs_noise = sf.read(os.path.join(olsa_dir, noise_file))
noise_len = len(noise)

allsentences = np.empty((1, 2))
allnoise = np.empty((1, 2))

file_ind =  np.random.choice(range(0, len(files)-1), size=len(files)-1, replace=False) # random order
for idx in file_ind:
    file = files[idx]
    sentence, fs = sf.read(os.path.join(olsa_dir, file))
    sentence_len = len(sentence)
    #offset = int((noise_len - sentence_len) / 2)
    #sentence_padded = np.zeros((noise_len,2))
    #sentence_padded[offset:offset+sentence_len,:] = sentence

    allsentences = np.vstack((allsentences, sentence))
    allnoise = np.vstack((allnoise, noise[0:len(sentence)]))
    
    # stop once file is long enough for scene 
    if len(allsentences) >= int(lens_file*fs_noise):
        # cut audio to perfect length - ! possibly cuts sentence off !
        allsentences = allsentences[:int(lens_file*fs_noise)]
        allnoise = allnoise[:int(lens_file*fs_noise)]
        break

if not os.path.exists("./scenes/sounds/OlSA_gen"):
    os.makedirs("./scenes/sounds/OlSA_gen")

sf.write(f"./scenes/sounds/OlSA_gen/{sent_out_file_name}.wav", allsentences, fs)
sf.write(f"./scenes/sounds/OlSA_gen/{noise_out_file_name}.wav", allnoise, fs_noise)

data, fs = sf.read("./scenes/sounds/OlSA_gen/sent_example_1.wav")
noise, fs = sf.read("./scenes/sounds/OlSA_gen/noise_example_1.wav")

fig, ax = plt.subplots(2,1)
ax[0].plot(noise)
ax[1].plot(data[:,0])
ax[1].plot(data[:,1]+0.1)
plt.show()
