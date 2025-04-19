import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from plot_style import * 
import pandas as pd
import scipy.stats as st


def elongate_vector(original_vector, new_length):
    """
    Elongates a given vector to the new length using linear interpolation.
    
    :param original_vector: The original vector (1D array or list).
    :param new_length: The desired length of the new vector.
    :return: A new vector with the specified length.
    """
    # Create an index for the original vector and the new vector
    original_index = np.linspace(0, len(original_vector) - 1, len(original_vector))
    new_index = np.linspace(0, len(original_vector) - 1, new_length)
    
    # Use numpy.interp to interpolate the values for the new length
    new_vector = np.interp(new_index, original_index, original_vector)
    
    return new_vector


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


def loadLEToDf(scene, df, window_size=False):
    with np.load(scene) as data:
        if "LEModel" in scene:
            LE = moving_average(data["data"], window_size)
            entry = {'name':scene, 'le':LE}
            df.loc[len(df)+1] = entry
        else:
            LE = moving_average(data["le"], window_size)
            entry = {'name':scene, 'le':LE}
            df.loc[len(df)+1] = entry
    return df


################################################################################
################################################################################
################################################################################

scenes = ["S0N90N270Headrot90_medium_-10", 
            "S0N180Headrot360_medium_-10",
            "S0N0rot_medium_-10",
            "S0N0osci60_medium_-10",
            "S0N0_medium_-10",
            "S0N90_medium_-10"]

# sets plot style determined in "plot_style.py"
set_plot_style()

#subj_names = ["AB", "JR", "AH", "JRH", "LM", "LEModel"]
subj_names = ["JRH", "LEModel"]
window_size = 25       # no smoothing if 0
modelRef = False


fig, axes = plt.subplots(2, 3, figsize=(14, 7))
fig.suptitle(f"Subject 1 at -10 dB SNR, Medium", fontweight="bold")
axes_flat = axes.flatten()

# all data to one dataframe
df = pd.DataFrame(columns=['name', 'le'])
root_results = "./results"    
for subj_name in subj_names:
    subj_path = os.path.join(root_results, subj_name)
    subj_scenes = np.array(sorted(glob.glob(os.path.join(root_results, subj_name, f"*.npz"))), dtype=object)    
    for scene in subj_scenes:
        df = loadLEToDf(scene, df, window_size)
print(df)

#condKeyword = "S0N180Headrot360_medium_-10"
for idx, condKeyword in enumerate(sorted(scenes)):
    
    # filter dataframe 
    lemodel_df = df[df["name"].str.contains(f"LEModel/{condKeyword}")]
    filtered_df = df[~df.index.isin(lemodel_df.index) & df["name"].str.contains(condKeyword)]

    lemodel_data = lemodel_df["le"].tolist()[0]
    interp_lemodel = elongate_vector(lemodel_data, len(filtered_df["le"].tolist()[0]))

    # mean_LE = pd.DataFrame(filtered_df["le"].tolist()).mean().to_numpy()
    # std_LE = pd.DataFrame(filtered_df["le"].tolist()).std().to_numpy()
    # x = np.arange(len(mean_LE))
    
    subj_le = filtered_df["le"].tolist()[0]
    
    
    # numVals = len(subj_le)
    # if isinstance(labelAngles, str):
    #     pos, labels = getAngleVec(labelAngles, numVals, numLabels)
    # else:
    #     pos, labels = getAngleVec(scene_name, numVals, numLabels)
    # ax.set_xticks(pos, np.round(labels, 2).astype(np.int32))
    # ax.set_xlabel("Angle (degrees)")

    # plot stuff
    axes_flat[idx].plot(subj_le, label="Subject 1")
    axes_flat[idx].plot(interp_lemodel, "k:", label="LE Model")
    axes_flat[idx].set_ylim([0, 14])
    axes_flat[idx].set_title(condKeyword)
    axes_flat[idx].legend()

plt.show()
fig.savefig('/Users/johannesrolfes/Desktop/StudiumHA/Uni/Sem2/Projekt/Subject1_res_-10medium.eps', format='eps')

