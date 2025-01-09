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

# -------------------------------------------------------------
#durs = [10, 5]

durs = [20, 10]
durnames = ["medium", "fast"]

for i in range(len(durs)):

    dur = durs[i]
    durname = durnames[i]

    scene_name = f"S0N0osci60_{durname}"

    Scene = pg.PathGenerator(dur=dur, point_per_rot=360, height=1.8)

    name = "speaker"
    type = "static"
    start_angle = 0
    radius = 1
    Scene.addSource(name, type, start_angle, radius)

    name = "noise_osci"
    type = "osci"
    start_angle = 0
    radius = 1
    rotation_angle = 0
    angle_range = 120        # +- 30°
    osci_type = "sin"       # "cos", "lin", ...
    freq = 1
    Scene.addSource(name, type, start_angle, radius, rotation_angle, angle_range, osci_type, freq)

    print(Scene.sources.head())
    Scene.save(scene_name)

# -------------------------------------------------------------


    scene_name = f"S0N0_{durname}"

    Scene = pg.PathGenerator(dur=dur, point_per_rot=360, height=1.8)
    radius = 1

    name = "speaker"
    type = "static"
    start_angle = 0
    Scene.addSource(name, type, start_angle, radius)

    name = "noise"
    type = "static"
    start_angle = 0
    Scene.addSource(name, type, start_angle, radius)

    print(Scene.sources.head())
    Scene.save(scene_name)

    # -------------------------------------------------------------

    scene_name = f"S0N90_{durname}"

    Scene = pg.PathGenerator(dur=dur, point_per_rot=360, height=1.8)
    radius = 1

    name = "speaker"
    type = "static"
    start_angle = 0
    Scene.addSource(name, type, start_angle, radius)

    name = "noise"
    type = "static"
    start_angle = 90
    Scene.addSource(name, type, start_angle, radius)

    print(Scene.sources.head())
    Scene.save(scene_name)


    # -------------------------------------------------------------

    scene_name = f"S0N0rot_{durname}"

    Scene = pg.PathGenerator(dur=dur, point_per_rot=360, height=1.8)
    radius = 1

    name = "speaker"
    type = "static"
    start_angle = 0
    Scene.addSource(name, type, start_angle, radius)

    name = "noise"
    type = "rot"
    start_angle = 0
    rotation_angle = 720
    Scene.addSource(name, type, start_angle, radius, rotation_angle)

    print(Scene.sources.head())
    Scene.save(scene_name)


    # -------------------------------------------------------------

    scene_name = f"S0N90N270Headrot90_{durname}"

    Scene = pg.PathGenerator(dur=dur, point_per_rot=360, height=1.8)
    radius = 1

    name = "speaker"
    type = "static"
    start_angle = 0
    Scene.addSource(name, type, start_angle, radius)

    name = "noise"
    type = "static"
    start_angle = 90
    Scene.addSource(name, type, start_angle, radius)

    name = "special_noise"
    type = "static"
    start_angle = 270
    Scene.addSource(name, type, start_angle, radius)

    name = "head"
    type = "osci"
    start_angle = 0
    rotation_angle = 0
    angle_range = 90
    osci_type = "sin2"
    freq = 0.2
    Scene.addHeadMovement(name, type, start_angle, rotation_angle, angle_range, osci_type, freq)

    print(Scene.sources.head())
    Scene.save(scene_name)
    
    
    # -------------------------------------------------------------

    scene_name = f"S0N180Headrot360_{durname}"

    Scene = pg.PathGenerator(dur=dur, point_per_rot=360, height=1.8)
    radius = 1

    name = "speaker"
    type = "static"
    start_angle = 0
    Scene.addSource(name, type, start_angle, radius)

    name = "noise"
    type = "static"
    start_angle = 180
    Scene.addSource(name, type, start_angle, radius)

    name = "head"
    type = "rot"
    start_angle = 0
    rotation_angle = 720
    Scene.addHeadMovement(name, type, start_angle, rotation_angle)

    print(Scene.sources.head())
    Scene.save(scene_name)





    # -------------------------------------------------------------
    # example of all ----------------------------------------------

    # scene_name = "S0NrotNosci"

    # Scene = pg.PathGenerator(dur=10, point_per_rot=300, height=1.8)

    # name = "speaker"
    # type = "static"
    # start_angle = 0
    # radius = 1
    # duration = 10
    # Scene.addSource(name, type, start_angle, radius)

    # name = "noise_rot"
    # type = "rot"
    # start_angle = 0
    # rotation_angle = 360
    # radius = 1
    # Scene.addSource(name, type, start_angle, radius, rotation_angle)

    # name = "noise_osci"
    # type = "osci"
    # start_angle = 0
    # radius = 1
    # rotation_angle = 360
    # angle_range = 60        # +- 30°
    # osci_type = "lin"       # "cos", "lin", ...
    # freq = 5
    # Scene.addSource(name, type, start_angle, radius, rotation_angle, angle_range, osci_type, freq)

    # print(Scene.sources.head())
    # Scene.save(scene_name)