import subprocess
import os 

def run_command(command):
    try:
        subprocess.run(command, shell=True, text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(e)

tascar_dir = "/Users/johannesrolfes/Desktop/StudiumHA/Uni/Sem2/Projekt"
#tascar_dir = "path"
cd = f"cd {tascar_dir}"

# render tascar files
out_dir = "/Users/johannesrolfes/Desktop/StudiumHA/Uni/Sem2/Projekt/repo/MovingSources/rendered_audio_files"
commands = ["tascar_renderfile -o S0N0.wav -s tascar_scene.tsc "]

for command in commands:
    stdout, stderr = run_command(command)
    print("Output:", stdout)
    print("Errors:", stderr)
