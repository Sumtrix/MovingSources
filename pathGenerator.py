import numpy as np
import pandas as pd
import os 
from scipy import signal
import matplotlib.pyplot as plt


class PathGenerator():
    def __init__(self, dur=10, point_per_rot=200, height=1.8):
        self.duration = dur
        self.pprot = point_per_rot
        self.height = 1.8
        self.sources = pd.DataFrame(columns=['name','path','type','stats'])


    def addSource(self, name, type, start_angle=None, radius=None, 
                  rotation_angle=None, angle_range=None, osci_type=None, freq=None):
        match type:
            case "static":
                if not name and not type and not start_angle and not radius:
                    print("Static: check arguments")
                    quit()
                else:
                    path = self.genStaticCoords(start_angle, radius)
                    stats = [start_angle, radius]
                    entry = {'name':name, 'path':path, 'type':type, 'stats':stats}
                    self.sources.loc[len(self.sources)+1] = entry

            case "rot":
                if not name and not type and not start_angle and not radius and not rotation_angle:
                    print("Rotation: check arguments")
                    quit()
                else:
                    path = self.genCircleCoords(start_angle, radius, rotation_angle)
                    stats = [start_angle, radius, rotation_angle]
                    entry = {'name':name, 'path':path, 'type':type, 'stats':stats}
                    self.sources.loc[len(self.sources)+1] = entry
            
            case "osci":
                if not name and not type and not start_angle and not radius\
                    and not rotation_angle and not angle_range and not osci_type and not freq:
                    print("Osci: check arguments")
                    quit()
                else:
                    path = self.genOscillatingCoords(start_angle, radius,rotation_angle, angle_range, osci_type, freq)
                    stats = [start_angle, radius, rotation_angle, angle_range, osci_type, freq]
                    entry = {'name':name, 'path':path, 'type':type, 'stats':stats}
                    self.sources.loc[len(self.sources)+1] = entry
            case _:
                print("Error: Determine type of source")


    def addHeadMovement(self, name, type, start_angle=None, rotation_angle=None, 
                        angle_range=None, osci_type=None, freq=None):
        match type:
            # case "rot":
            #     if not name and not type and not start_angle and not radius and not rotation_angle:
            #         print("Rotation: check arguments")
            #         quit()
            #     else:
            #         path = self.genCircleOrientation(start_angle, radius, rotation_angle)
            #         stats = [start_angle, radius, rotation_angle]
            #         entry = {'name':name, 'path':path, 'type':type, 'stats':stats}
            #         self.sources.loc[len(self.sources)+1] = entry
            
            case "osci":
                if not name and not type and not start_angle\
                    and not rotation_angle and not angle_range and not osci_type and not freq:
                    print("Osci: check arguments")
                    quit()
                else:
                    path = self.genOsciOrientation(start_angle,rotation_angle, angle_range, osci_type, freq)
                    stats = [start_angle, rotation_angle, angle_range, osci_type, freq]
                    entry = {'name':name, 'path':path, 'type':type, 'stats':stats}
                    self.sources.loc[len(self.sources)+1] = entry
            case _:
                print("Error: Determine type of source")


    def genStaticCoords(self, start_angle, radius):
        x_coords = radius * np.cos(start_angle)
        y_coords = radius * np.sin(start_angle)
        return 0, x_coords, y_coords, self.height


    def genCircleCoords(self, start_angle, radius, rotation_angle):
        num_points = int(round(self.pprot*(rotation_angle/360), 0))
        angles = np.radians(np.linspace(start_angle, start_angle + rotation_angle, num_points+1, endpoint=False))
        x_coords = radius * np.cos(angles)
        y_coords = radius * np.sin(angles)
        time_interval = self.duration / self.pprot
        points = []
        for i in range(num_points+1):
            t = i * time_interval
            x, y = x_coords[i], y_coords[i]
            z = self.height  # circle on xy plane only
            points.append((t, x, y, z))
        return points

    def genOscillatingCoords(self, start_angle, radius, rotation_angle, angle_range, osci_type, freq):
        self.checkNyquist(angle_range, freq)
        match osci_type:
            case "sin":
                num_points = int(self.pprot * (rotation_angle / 360))
                time_interval = self.duration / self.pprot
                times = np.linspace(0, self.duration, num_points + 1)
                oscillation = (angle_range/2) * np.sin(2 * np.pi * freq * times)
                angles = np.radians(start_angle) + np.radians(oscillation) + \
                         np.linspace(0, np.radians(rotation_angle), num_points + 1)
            case "lin":
                num_points = int(self.pprot * (rotation_angle / 360))
                time_interval = self.duration / self.pprot
                times = np.linspace(0, self.duration, num_points + 1)
                oscillation = (angle_range/2) * signal.sawtooth(2 * np.pi * freq * times, 0.5)
                angles = np.radians(start_angle) + np.radians(oscillation) + \
                         np.linspace(0, np.radians(rotation_angle), num_points + 1)
            case _ :
                print("Error: Check you osci type")
        
        # plt.plot(oscillation)
        # plt.show()
        x_coords = radius * np.cos(angles)
        y_coords = radius * np.sin(angles)
        time_interval = self.duration / self.pprot
        points = []
        for i in range(num_points+1):
            t = i * time_interval
            x, y = x_coords[i], y_coords[i]
            z = self.height  # circle on xy plane only
            points.append((t, x, y, z))
        return points
    
    def genOsciOrientation(self, start_angle, rotation_angle, angle_range, osci_type, freq):    
        self.checkNyquist(angle_range, freq)
        if freq==0:
            raise ValueError("Freq must be >0 otherwise use rotation source.")
        match osci_type:
            case "sin2":
                num_points = int(self.pprot * ((angle_range)/360) * freq * self.duration)
                time_interval = self.duration / self.pprot
                times = np.linspace(0, self.duration, num_points + 1)
                oscillation = angle_range * np.sin(np.pi * freq * times)**2
                angles = np.radians(start_angle) + np.radians(oscillation) + \
                         np.linspace(0, np.radians(rotation_angle), num_points + 1)
            
            # case "sin":
            #     num_points = int(self.pprot * (rotation_angle / 360))
            #     time_interval = self.duration / self.pprot
            #     times = np.linspace(0, self.duration, num_points + 1)
            #     oscillation = (angle_range/2) * np.sin(2 * np.pi * freq * times)
            #     angles = np.radians(start_angle) + np.radians(oscillation) + \
            #              np.linspace(0, np.radians(rotation_angle), num_points + 1)
            # case "lin":
            #     num_points = int(self.pprot * (rotation_angle / 360))
            #     time_interval = self.duration / self.pprot
            #     times = np.linspace(0, self.duration, num_points + 1)
            #     oscillation = (angle_range/2) * signal.sawtooth(2 * np.pi * freq * times, 0.5)
            #     angles = np.radians(start_angle) + np.radians(oscillation) + \
            #              np.linspace(0, np.radians(rotation_angle), num_points + 1)
            case _ :
                print("Error: Check you osci type")
        
        # plt.plot(angles)
        # plt.show()
        time_interval = self.duration / self.pprot
        points = []
        for i in range(num_points+1):
            t = i * time_interval
            ry, rx = 0, 0
            rz = angles[i]
            # [t_1 Rz_1 Ry_1 Rx_1]
            points.append((t, rz, ry, rx))
        return points
    

    def save(self, name, root="./scenes/paths"):
        scene_folder = os.path.join(root, name)
        if not os.path.exists(scene_folder):
            os.makedirs(scene_folder)
        
        for _, row in self.sources.iterrows():
            source_name = row['name']
            path = row['path']
            stats_str = f"{'_'.join(map(str, row['stats']))}"
            file = os.path.join(scene_folder, f"{source_name}.txt") # f"{source_name}_{stats_str}.txt"
            print(file)
            with open(file, 'w') as f:
                if len(path) == 4:
                    t, x, y, z = path
                    f.write(f"{t:.2f} {x:.2f} {y:.2f} {z:.2f}\n")
                else:
                    for t, x, y, z in path:
                        f.write(f"{t:.2f} {x:.2f} {y:.2f} {z:.2f}\n")

    def checkNyquist(self, angle_range, freq):
        num_points = round(self.pprot * ((angle_range)/360) * freq * self.duration)
        self.fs =  num_points / self.duration
        print(self.fs/2)
        print(freq)
        if freq >= (self.fs/2):
            raise ValueError(f"Oscillation freq {freq}>= Nyquist of {self.fs/2}")
        else:
            pass
