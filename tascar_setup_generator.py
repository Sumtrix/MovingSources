import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os 
import pathGenerator as pg

###############################################################
###############################################################

# rotating y/n
# start angle
# total rotation angle
# scene duration
# source file (?)
# > file name 

# other aspect -----------
# rotation ortientation
# num points per rotation

###############################################################
###############################################################


Scene = pg.PathGenerator(dur=10, point_per_rot=300, height=1.8)

name = "speaker"
type = "static"
start_angle = 0
radius = 1
duration = 10
Scene.addSource(name, type, start_angle, radius)

name = "noise_rot"
type = "rot"
start_angle = 0
rotation_angle = 360
radius = 1
Scene.addSource(name, type, start_angle, radius, rotation_angle)

name = "noise_osci"
type = "osci"
start_angle = 0
radius = 1
rotation_angle = 360
angle_range = 60        # +- 30°
osci_type = "lin"       # "cos", "lin", ...
freq = 5
Scene.addSource(name, type, start_angle, radius, rotation_angle, angle_range, osci_type, freq)

print(Scene.sources.head())

scene_name = "S0NrotNosci"
Scene.save(scene_name)


