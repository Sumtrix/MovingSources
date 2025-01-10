import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import json

# ---------------------------------
# ---------------------------------

subj_name = "JR"

# ---------------------------------
# ---------------------------------

root_results = "./results_examples"
subj_runs = sorted(glob.glob(os.path.join(root_results, subj_name, f"*{subj_name}*")))
fig, ax = plt.subplots(3, 2)    # training, -3 medium, -7 medium, -3 fast, -7 fast , 1 empty

for run_idx, run in enumerate(subj_runs):
    meas_files = os.listdir(run)
    for meas_file in meas_files:
        meas_name = os.path.basename(meas_file)
        LE_data = np.load(meas_file)
        
        ax[run_idx].plot()










# #results_path = "./le_modell_results/-3 dB SNR"
# results_path = "C:/Users/annik/OneDrive/Desktop/Projekt/real-time-assessment-listening-effort/measurement/Results/JR Test"
# #files = sorted(glob.glob(os.path.join(results_path, "*medium*.npy")))
# files = os.listdir(results_path)


# fig, ax = plt.subplots(2, 1)
# legend = []
# print(files)
# for file in files:
#     print(file)
#     data_list = np.load(file)  # Load data from .npy file
#     scene = os.path.basename(file)
#     num_values = len(data_list)
#     ax[0].plot(data_list)
#     legend.append(scene)
# ax[0].legend(legend)

        
# #ax_pol.legend(legend_vec)
# ax[0].set_ylim([0, 14])
# ax[0].grid(linestyle=':', alpha=0.5)
# plt.show()

