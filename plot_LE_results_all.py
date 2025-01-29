import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from plot_style import * 

def getAngleVec(scene_name, numVals):
    numVals += 1
    if "medium" in scene_name:
        dur = 30
    elif "slow" in scene_name:
        dur = 60
    
    numLabels = 12
    xticks_positions = np.linspace(0, numVals, numLabels) # positions to label via xticks
    if any in ["S0N0", "S0N90", "S0N90rot"] in scene_name:
        print(["S0N0", "S0N90", "S0N90rot"])
        angles = np.linspace(0, 3*360, numVals)
        xticks_labels = np.linspace(0, 3*360, numLabels)
    elif "S0N0osci60" in scene_name:
        print("S0N0osci60")
        angles = 60 * np.sin(2 * np.pi * 1 * np.linspace(0, dur, numVals))
        xticks_labels = 60 * np.sin(2 * np.pi * 1 * np.linspace(0, dur, numLabels))
    elif "S0N180Headrot360" in scene_name:
        print("S0N180Headrot360")
        angles = np.linspace(0, 3*360, numVals)
        xticks_labels = np.linspace(0, 3*360, numLabels)
    else:# "S0N90N270Headrot90" in scene_name:
        angles = 90 * np.sin(np.pi * 0.2 * np.linspace(0, dur, numVals))**2
        xticks_labels = 90 * np.sin(np.pi * 0.2 * np.linspace(0, dur, numLabels))**2
    # plt.plot(xticks_labels)
    # plt.show()
    return xticks_positions, np.round(xticks_labels, 2)

def moving_average(data, window_size):
    if window_size > len(data):
        print("Wiwndow size must not be greater than the length of the data.")
        return -1 
    if window_size < 1:
        return data
    else:
        return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


def plotConditions(scene_conditions, allInOne=False):
    if allInOne:
        _, axes = plt.subplots(1,1)
    else:
        _, axes = plt.subplots(2, 2)
    if allInOne: condition_legend = []
    for axidx, condition in enumerate(scene_conditions):
        if allInOne:
            ax = axes
        else:
            row, col = divmod(axidx, 2) 
            ax = axes[row, col]
        if not allInOne: condition_legend = []
        for _, scene in enumerate(condition):
            scene_name = os.path.basename(scene)
            condition = ' '.join(scene_name[:-4].split("_")[1:])
            with np.load(scene) as data:
                if "LE_Modell" in scene_name:
                    meas = data["data"]
                else:
                    meas = data["le"]
                smoothed_data = moving_average(meas, window_size)
                if not isinstance(smoothed_data, np.ndarray): continue
                ax.plot(smoothed_data)
                #numVals = len(smoothed_data)
                #pos, labels = getAngleVec(scene_name, numVals)
                #ax.set_xticks(pos, labels)
                ax.set_title(condition)
                ax.set_ylim([0, 14])
                ax.grid(which="both", alpha=0.8, linestyle=':')
                condition_legend.append(scene_name[:-4])
            #print("\n", os.path.join(run, scene), "\n", len(meas))
            ax.legend(condition_legend, ncol=2)
    plt.show()


# ---------------------------------
# ---------------------------------

# PLOT VARIABLES NEEDED
# per SNR 
# angle vector for every situation
# plot of every situation singular
# all situtaions per subj (for one in particular) in one (overall range)
# compare S0N0 S0N90 S0Nrot
# compare S0N0 osci
# var area plot 
# pro kondition in einem plot medium vs slow + modell + variance area
    # most interesting: 
    # > S0N0rot 
    # > S0N180 headturn

set_plot_style()

subj_name = "JR"
window_size = 30        # no smoothing if 0
one_plot = False

# ---------------------------------
# ---------------------------------


root_results = "./results"
subj_names = os.listdir(root_results)
if type(subj_name)==str:
    subj_names = [subj_name]
    
for subj_name in subj_names:
    subj_path = os.path.join(root_results, subj_name)
    
    scenes_med_7 = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*medium_-7*"))))
    scenes_med_10 = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*medium_-10*"))))
    scenes_slow_7 = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*slow_-7*"))))
    scenes_slow_10 = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*slow_-10*"))))
    
    #------------------------------------------------
    # all conditions and all data
    scene_conditions = [scenes_med_7, scenes_med_10, scenes_slow_7, scenes_slow_10]
    plotConditions(scene_conditions)
    
    #------------------------------------------------
    # plot comparison S0N0 S0N90 S0Nrot
    select_indices = [0, 2, -1]
    scene_conditions = [scenes_med_7[select_indices], 
                        scenes_med_10[select_indices], 
                        scenes_slow_7[select_indices], 
                        scenes_slow_10[select_indices]]
    plotConditions(scene_conditions)


    #------------------------------------------------
    # plot comparison S0N0 S0N90 S0Nrot
    select_indices = [0, 1]
    scene_conditions = [scenes_med_7[select_indices], 
                        scenes_med_10[select_indices], 
                        scenes_slow_7[select_indices], 
                        scenes_slow_10[select_indices]]
    plotConditions(scene_conditions)
    
    
    #------------------------------------------------
    # N0S180 rot both
    select_indices = [3]
    scene_conditions = [scenes_med_7[select_indices], 
                        scenes_med_10[select_indices]]
    plotConditions(scene_conditions, allInOne=True)
    
    scene_conditions = [scenes_slow_7[select_indices], 
                        scenes_slow_10[select_indices]]
    plotConditions(scene_conditions, allInOne=True)







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

