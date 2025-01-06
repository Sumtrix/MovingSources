import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import json

results_path = "le_modell_results\-3 dB SNR"
files_fast = sorted(glob.glob(os.path.join(results_path, "*fast*.npy")))
files_medium = sorted(glob.glob(os.path.join(results_path, "*medium*.npy")))
files = [files_fast, files_medium]
set_names = ["fast", "medium"]

fig, ax = plt.subplots(2, 1)


for idx, dataset in enumerate(files):
    set_name = set_names[idx]
    legend = []
    for file in dataset:
        print(file)
        data_list = np.load(file)  # Load data from .npy file
        scene = os.path.basename(file)
        num_values = len(data_list)
        
        ax[idx].plot(data_list)
        ax[idx].set_title(set_name)
        legend.append(scene)
    ax[idx].legend(legend)
    
        
#ax_pol.legend(legend_vec)
ax[0].set_ylim([0, 14])
ax[0].grid(linestyle=':', alpha=0.5)
ax[1].set_ylim([0, 14])
ax[1].grid(linestyle=':', alpha=0.5)
plt.show()



# old based on json
"""
#fig_po, ax_pol = plt.subplots(subplot_kw={'projection': 'polar'})
fig, ax = plt.subplots(2, 1)

legend_fast = []
legend_medium = []
for file in files:
    print(file)
    with open(file, 'r') as f:
        data_list = json.load(f)
    scene = os.path.basename(file)
    num_values = len(data_list)
    angles = np.linspace(0, 2*np.pi, num_values)
    
    if len(data_list) < 160 :
        ax[0].plot(data_list)       
        ax[0].set_title("Fast - 5 s")       
        legend_fast.append(scene)
    else:
        ax[1].plot(data_list)       
        ax[1].set_title("Medium - 10 s")        
        legend_medium.append(scene)
    #ax_pol.plot(angles, data_list)
    #ax_pol.grid(True)
    
#ax_pol.legend(legend_vec)
ax[0].legend(legend_fast)
ax[0].set_ylim([0,14])
ax[0].grid(linestyle=':', alpha=0.5)
ax[1].legend(legend_medium)
ax[1].set_ylim([0,14])
ax[1].grid(linestyle=':', alpha=0.5)
plt.show()
"""