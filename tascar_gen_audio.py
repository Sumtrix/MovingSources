import subprocess
import os 
import glob
import time 

tascar_dir = "D:/Program Files (86x)/tascar-0.233.2.0-bb38f5e-windows/tascar"
scene_dir = "D:/Benutzer/Johannes/Desktop/Studium/Uni/Sem2/MovingSources/scenes"


# file management
files = glob.glob(os.path.join(scene_dir, "*.tsc"))
file_names = [os.path.basename(file) for file in files]
print("\nV V V V File that will be generated V V V V\n")
[print(file_name) for file_name in file_names]


# run commands
print("\nV V V V V V Command Output V V V VV V \n")
os.chdir(tascar_dir)
for file_name in file_names:
    command = [
        "tascar_renderfile",
        "-o", 
        f" {file_name}.wav ",
        f"{scene_dir}/{file_name}"
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)