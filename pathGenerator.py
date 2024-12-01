import numpy as np
import pandas as pd
import os 

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
        match osci_type:
            case "sin":
                num_points = int(self.pprot * (rotation_angle / 360))
                time_interval = self.duration / self.pprot
                times = np.linspace(0, self.duration, num_points + 1)
                oscillation = (angle_range/2) * np.sin(2 * np.pi * freq * times)
                angles = np.radians(start_angle) + np.radians(oscillation) + \
                         np.linspace(0, np.radians(rotation_angle), num_points + 1)
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









    # def gen_circ_path(self):
    #     num_points = int(round(self.pprot*(self.rotation_angle/2*np.pi), 0))
    #     angles = np.linspace(self.start_angle, self.start_angle + self.rotation_angle, num_points+1, endpoint=False)
    #     x_coords = self.radius * np.cos(angles)
    #     y_coords = self.radius * np.sin(angles)
    #     time_interval = self.duration / self.pprot
    #     points = []
    #     for i in range(num_points+1):
    #         t = i * time_interval
    #         x, y = x_coords[i], y_coords[i]
    #         z = self.height  # circle on xy plane only
    #         points.append((t, x, y, z))
    #     return points


    # def save_to_file(self, filename, points):
    #     with open(filename, 'w') as f:
    #         print(len(points))
    #         if len(points) == 4:
    #             t, x, y, z = points
    #             f.write(f"{t:.2f} {x:.2f} {y:.2f} {z:.2f}\n")
    #         else:
    #             for t, x, y, z in points:
    #                 f.write(f"{t:.2f} {x:.2f} {y:.2f} {z:.2f}\n")
    #     print(f"Data saved to {filename}")


    # def genRotPath(self, start_angle, rotation_angle, radius):
    #     self.type = "rot"
    #     self.start_angle = start_angle
    #     self.radius = radius
    #     self.rotation_angle = rotation_angle
    #     self.filename = f"{self.type}_{self.start_angle}_{self.rotation_angle}_{self.duration}_{self.pprot}.wav"
    #     self.path = self.gen_circ_path()


    # def genStaticPath(self, start_angle):
    #     self.type = "static"
    #     self.start_angle = start_angle
    #     self.filename = f"{self.type}_{self.start_angle}_{self.rotation_angle}_{self.duration}_{self.pprot}.wav"


    # def genOsciPath(self, start_angle, range, osci_type, freq):
    #     self.type = "osci"
    #     self.start_angle = start_angle
    #     self.range = range
    #     self.osci_type = osci_type
    #     self.freq = freq
    #     self.filename = f"{self.type}_{self.start_angle}_{self.range}_{self.osci_type}_{self.freq}_{self.duration}_{self.pprot}.wav"

