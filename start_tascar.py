import subprocess
import os 

def run_command(command):
    try:
        subprocess.run(command, shell=True, text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(e)

tascar_dir = "/Users/johannesrolfes/Desktop/StudiumHA/Uni/Sem2/Projekt/tascar"
cd = f"cd {tascar_dir}"
print(f"Running: {cd}")
run_command(cd)

# render tascar files
run = f"tascar_renderfile -o S0N0.wav -s tascar_scene.tsc "
print(f"Running: {run}")
run_command(run)
