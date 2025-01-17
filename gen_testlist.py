import os
import glob
import random

scenes_root = "./scenes/"
outdir = "./lists/"
scenes = sorted(glob.glob(os.path.join(scenes_root, "*.tsc")))

num_lists = 7

for list_idx in range(num_lists):    
    file = open(os.path.join(outdir, f'list_{list_idx}'),'w')
    random.shuffle(scenes)
    for scene in scenes:
        file.write(f"./audio/{os.path.basename(scene)[:-4]}.wav\n")
    file.close