Git repository from the Fortgeschrittenen-Projekt Hörtechnik und Audiologie 
WiSE 2024/25 investigating the influence of moving sources on the listening effort.

Date: 26.4.2025
Authors:
Johannes Rolfes, johannes.rolfes@uni-oldenburg.de
Annika Beyer, annika.beyer@uni-oldenburg.de

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------


Files of interest
-----------------

# Plots from the poster: 
plot_LE_results_cond.py
plot_LE_results_across_subj.py

# Render audio files 
tascar_gen_audio.py

# Generate source paths
tascar_setup_generator.py
(pathGenerator.py)

Usage
-----
Setup sources and their movement in `tascar_setup_generator.py` just like the 
examples in the script. The outputs are .txt files containing the time stamps
and coordinates for the paths generated. Currently these must be implemented 
into the .tsc files manually at the top of the files based on the directory they
are in. 

