import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import os 
import pathGenerator as pg



durs = [30, 60]
durnames = ["medium", "slow"]

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
    rotation_angle = 1080
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
    rotation_angle = 1080
    Scene.addHeadMovement(name, type, start_angle, rotation_angle)

    print(Scene.sources.head())
    Scene.save(scene_name)
