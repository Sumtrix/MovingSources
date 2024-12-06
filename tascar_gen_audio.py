import subprocess
import os 

def run_command(command):
    try:
        res = subprocess.run(command, shell=True, text=True)
        return res
    except subprocess.CalledProcessError as e:
        print(e)

tascar_dir = "C:/Users/annik/OneDrive/Desktop/Projekt/tascar"
out_dir = "C:/Users/annik/OneDrive/Desktop/Projekt/MovingSources/rendered_audio_files"
scene_dir = "C:/Users/annik/OneDrive/Desktop/Projekt/MovingSources/scenes"


# command = f"""
# cd {tascar_dir}
# tascar_renderfile -o {out_dir}/S0N0.wav -s {scene_dir}/S0N0.tsc
# """

command = """
cd C:/Users/annik/OneDrive/Desktop/Projekt/tascar
tascar_renderfile -o S0N0.wav C:/Users/annik/OneDrive/Desktop/Projekt/MovingSources/scenes/S0N0.tsc
tascar_renderfile -o S0N90.wav C:/Users/annik/OneDrive/Desktop/Projekt/MovingSources/scenes/S0N90.tsc
tascar_renderfile -o S0N0rot.wav C:/Users/annik/OneDrive/Desktop/Projekt/MovingSources/scenes/S0N0rot.tsc
tascar_renderfile -o S0N90N180Headrot90.wav C:/Users/annik/OneDrive/Desktop/Projekt/MovingSources/scenes/S0N90N180Headrot90.tsc
tascar_renderfile -o S0NrotNosci.wav C:/Users/annik/OneDrive/Desktop/Projekt/MovingSources/scenes/S0NrotNosci.tsc

"""

print(command)

subprocess.run(command, shell=True, text=True)