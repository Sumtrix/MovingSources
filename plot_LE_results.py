import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# ---------------------------------
# ---------------------------------
# 15.1.2025 - All measurements are plottet. Figure per Person, subplot per run

#subj_name = "JR"
subj_name = "LE_Modell"
#subj_names = ["JR", "LE_Modell"]

# ---------------------------------
# ---------------------------------

def moving_average(data, window_size):
    if window_size < 1:
        print(("Window size must be at least 1."))
        return data
        #raise ValueError("Window size must be at least 1.")
    if window_size > len(data):
        print("Window size must not be greater than the length of the data.")
        return data
        #raise ValueError("Wiwndow size must not be greater than the length of the data.")
    else:
        return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


root_results = "./results"
if type(subj_name)==str:
    subj_names = [subj_name]
for subj_name in subj_names:
    subj_runs = sorted(glob.glob(os.path.join(root_results, subj_name, f"*{subj_name}*")))
    fig, axes = plt.subplots(3, 2)    # training, -3 medium, -7 medium, -3 fast, -7 fast , 1 empty
    for run_idx, run in enumerate(subj_runs):
        row, col = divmod(run_idx, 2) 
        ax = axes[row, col]
        
        scenes = os.listdir(run)
        run_name = os.path.basename(run)
        run_legend = []
        for scene in scenes:
            scene_name = os.path.basename(scene)
            run_legend.append(scene_name)
            print("\n", os.path.join(run, scene), "\n")
            with np.load(os.path.join(run, scene)) as data:
                print(data)
                if "LE_Modell" in run_name:
                    meas = data["data"]
                else:
                    meas = data["le"]
                
                # window_size = 10
                # smoothed_data = moving_average(meas, window_size)
                
                ax.plot(meas)
                ax.set_title(run_name)
                ax.set_ylim([0, 14])
        ax.legend(run_legend)
    plt.show()










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

