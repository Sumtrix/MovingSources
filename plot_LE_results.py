import numpy as np
import matplotlib.pyplot as plt
import glob
import os

# ---------------------------------
# ---------------------------------

# participant
#subj_name = "JR"
subj_name = "LE_Modell"
#subj_names = ["JR", "LE_Modell"]

# keyword/s for only plotting some scenes
plot_keyword = ["S0N0_", "S0N90_", "S0N0rot"]
plot_keyword = ["headrot360"]

# smoothing
window_size = 8        # no smoothing if 0

one_plot = False
# ---------------------------------
# ---------------------------------

def moving_average(data, window_size):
    if window_size > len(data):
        raise ValueError("Wiwndow size must not be greater than the length of the data.")
    if window_size < 1:
        return data
    else:
        return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


root_results = "./results"
if type(subj_name)==str:
    subj_names = [subj_name]
for subj_name in subj_names:
    subj_runs = sorted(glob.glob(os.path.join(root_results, subj_name, f"*{subj_name}*")))
    
    if one_plot:
        fig, ax = fig, axes = plt.subplots(1, 1)
    else:
        fig, axes = plt.subplots(3, 2)    # training, -3 medium, -7 medium, -3 fast, -7 fast , 1 empty
        
    for run_idx, run in enumerate(subj_runs):
        if one_plot:
            ax = axes
        else:
            row, col = divmod(run_idx, 2) 
            ax = axes[row, col]
        
        scenes = os.listdir(run)
        if plot_keyword:
            #scenes = [file for file in scenes if any(kw.lower() in file.lower() for kw in plot_keyword)]
            scenes = list(filter(lambda file: any(kw.lower() in file.lower() for kw in plot_keyword), scenes))


        run_name = os.path.basename(run)
        run_legend = []
        for scene in scenes:
            scene_name = os.path.basename(scene)
            run_legend.append(scene_name)
            #print("\n", os.path.join(run, scene), "\n")
            with np.load(os.path.join(run, scene)) as data:
                if "LE_Modell" in run_name:
                    meas = data["data"]
                else:
                    meas = data["le"]
                smoothed_data = moving_average(meas, window_size)
                ax.plot(smoothed_data)
                ax.set_title(run_name)
                ax.set_ylim([0, 14])
                ax.grid(which="both", alpha=0.8, linestyle=':')
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

