import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from plot_style import * 

def interpolate_vector(vector):
    """
    Interpolates a vector to be twice as long using linear interpolation.
    
    Parameters:
        vector (list or np.ndarray): Input vector.
        
    Returns:
        np.ndarray: Interpolated vector with twice the length.
    """
    x_old = np.linspace(0, 1, len(vector))
    x_new = np.linspace(0, 1, 2 * len(vector) - 1)
    
    return np.interp(x_new, x_old, vector)


def getAngleVec(scene_name, numVals, numLabels=12):
    numVals += 1
    if "medium" in scene_name:
        dur = 30
    elif "slow" in scene_name:
        dur = 60
    
    xticks_positions = np.linspace(0, numVals, numLabels+1) # positions to label via xticks
    print(scene_name)
    if any(s in scene_name for s in ["S0N0_", "S0N90_", "S0N0rot_"]):
        print(["S0N0_", "S0N90_", "S0N0rot_"])
        xticks_labels = np.linspace(0, 3*360, numLabels+1)
    elif "S0N0osci60" in scene_name:
        print("S0N0osci60")
        xticks_labels = 60 * np.sin(2 * np.pi * 1 * np.linspace(0, dur, numLabels+1))
    elif "S0N180Headrot360" in scene_name:
        print("S0N180Headrot360")
        xticks_labels = np.linspace(0, 3*360, numLabels+1)
    elif "S0N90N270" in scene_name:
        print("S0N90N270Headrot90")
        xticks_labels = 90 * np.sin(np.pi * 0.2 * np.linspace(0, dur, numLabels+1))**2
    else:
        raise NameError("Scene not recognizes")
    return xticks_positions, xticks_labels

def moving_average(data, window_size):
    if window_size > len(data):
        print("Wiwndow size must not be greater than the length of the data.")
        return -1 
    if window_size < 1:
        return data
    else:
        return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


def plotConditions(scene_conditions, allInOne=False, labelAngles=True, numLabels=12):
    if allInOne:
        fig, axes = plt.subplots(1,1, figsize=(11, 8))
    else:
        fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    fig.suptitle(f'{subj_name}', fontweight="bold")
    if allInOne: condition_legend = []
    for axidx, condition in enumerate(scene_conditions):
        if allInOne:
            ax = axes
        else:
            row, col = divmod(axidx, 2) 
            ax = axes[row, col]
        if not allInOne: condition_legend = []
        for _, scene in enumerate(condition):
            name = scene.split("/")
            print(name)
            scene_name = os.path.basename(scene)
            condition_name = ' '.join(scene_name[:-4].split("_")[1:])
            with np.load(scene) as data:
                if "LEModel" in scene:
                    meas = data["data"]
                else:
                    meas = data["le"]
                smoothed_data = moving_average(meas, window_size)
                if not isinstance(smoothed_data, np.ndarray): continue
                ax.plot(smoothed_data)
                ax.set_title(condition_name)
                ax.set_ylim([0, 14])
                ax.grid(which="both", alpha=0.8, linestyle=':')
                if labelAngles:
                    numVals = len(smoothed_data)
                    if isinstance(labelAngles, str):
                        pos, labels = getAngleVec(labelAngles, numVals, numLabels)
                    else:
                        pos, labels = getAngleVec(scene_name, numVals, numLabels)
                    ax.set_xticks(pos, np.round(labels, 2).astype(np.int32))
                    ax.set_xlabel("Angle (degrees)")
                else:
                    ax.set_xlabel("Samples")
                ax.set_ylabel("Listening Effort")
                condition_legend.append(scene_name[:-4])
            #print("\n", os.path.join(run, scene), "\n", len(meas))
            ax.legend(condition_legend, ncol=2)
    fig.tight_layout(pad=1)
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


# sets plot style determined in "plot_style.py"
set_plot_style()

#subj_name = ["AB", "JR", "AH", "JRH", "LM", "LEModel"]
subj_name = "LEModel"
window_size = 25       # no smoothing if 0
modelRef = False

# ---------------------------------
# ---------------------------------


root_results = "./results"
subj_names = os.listdir(root_results)
if type(subj_name)==str:
    subj_names = [subj_name]
else:
    subj_names = subj_name
    
for subj_name in subj_names:
    subj_path = os.path.join(root_results, subj_name)
    
    scenes_med_7 = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*medium_-7*"))), dtype=object)
    scenes_med_10 = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*medium_-10*"))), dtype=object)
    scenes_slow_7 = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*slow_-7*"))), dtype=object)
    scenes_slow_10 = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*slow_-10*"))), dtype=object)
    
    if modelRef:
        scenes_med_7 = np.insert(scenes_med_7, len(scenes_med_7), glob.glob(os.path.join(root_results, "LEModel", f"*medium_-7*")))
        scenes_med_10 = np.insert(scenes_med_7, len(scenes_med_10), glob.glob(os.path.join(root_results, "LEModel", f"*medium_-10*")))
        scenes_slow_7 = np.insert(scenes_med_7, len(scenes_slow_7), glob.glob(os.path.join(root_results, "LEModel", f"*slow_-7*")))
        scenes_slow_10 = np.insert(scenes_med_7, len(scenes_slow_10), glob.glob(os.path.join(root_results, "LEModel", f"*slow_-10*")))

    #------------------------------------------------
    # all conditions and all data
    scene_conditions = [scenes_med_7, scenes_med_10, scenes_slow_7, scenes_slow_10]
    plotConditions(scene_conditions, labelAngles=False)
    
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
    plotConditions(scene_conditions, labelAngles="S0N0_")
    
    
    #------------------------------------------------
    # N0S180 rot both
    select_indices = [3]
    scene_conditions = [scenes_med_7[select_indices], 
                        scenes_med_10[select_indices]]
    plotConditions(scene_conditions, allInOne=True)
    
    scene_conditions = [scenes_slow_7[select_indices], 
                        scenes_slow_10[select_indices]]
    plotConditions(scene_conditions, allInOne=True)


    # N0S180 rot both
    # select_indices = [3]
    # scene_conditions = [scenes_med_7[select_indices], 
    #                     scenes_slow_7[select_indices]]
    # plotConditions(scene_conditions, allInOne=True)
    
    # scene_conditions = [scenes_med_10[select_indices], 
    #                     scenes_slow_10[select_indices]]
    # plotConditions(scene_conditions, allInOne=True)


    #------------------------------------------------
    # # S0N270N90 headrot
    select_indices = [4]
    scene_conditions = [scenes_med_7[select_indices], 
                        scenes_med_10[select_indices], 
                        scenes_slow_7[select_indices], 
                        scenes_slow_10[select_indices]]
    plotConditions(scene_conditions, numLabels=24)


    # select_indices = [4]
    # scene_conditions = [scenes_med_7[select_indices], 
    #                     scenes_med_10[select_indices]]
    # plotConditions(scene_conditions, allInOne=True)
    
    # scene_conditions = [scenes_slow_7[select_indices], 
    #                     scenes_slow_10[select_indices]]
    # plotConditions(scene_conditions, allInOne=True)
    

    #------------------------------------------------
    # average LE to S0Nrot
    select_indices = [2]
    scene_conditions = [scenes_slow_7[select_indices], 
                        scenes_slow_10[select_indices]]
    plotConditions(scene_conditions, allInOne=True, labelAngles="S0N0rot_")
    
    