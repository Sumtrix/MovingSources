import os
import glob
import random

scenes_root = "./scenes/"
outdir = "./lists/"
#scenes_medium = sorted(glob.glob(os.path.join(scenes_root,"*medium*.tsc")))
scenes = sorted(glob.glob(os.path.join(scenes_root, "*.tsc")))

num_lists = 10

for list_idx in range(num_lists):    
    file = open(os.path.join(outdir, f'list_{list_idx}.txt'),'w')
    random.shuffle(scenes)
    for scene in scenes:
        file.write(f"./audio/{os.path.basename(scene)[:-4]}.wav\n")
    file.close

# for list_idx in range(num_lists):    
#     file = open(os.path.join(outdir, f'list_medium_{list_idx}.txt'),'w')
#     random.shuffle(scenes_medium)
#     for scene in scenes_medium:
#         file.write(f"./audio/{os.path.basename(scene)[:-4]}.wav\n")
#     file.close