import numpy as np


def generate_orientations(rotStart, rotangle, num_points, duration, orOffset=0):
    angle = rotangle / num_points
    angles = np.linspace(rotStart, rotStart + rotangle + angle, num_points+1, endpoint=False)
    # assuming equidistant sampling
    time_interval = duration / num_points

    orientation = []
    for i in range(num_points+1):
        t = i * time_interval
        orientation.append((t, (angles[i]/np.pi)*180 + orOffset, 0, 0))
    return orientation


def generate_circle_points(rotStart, rotangle, radius, height, num_points, duration):
    angle = rotangle / num_points
    angles = np.linspace(rotStart, rotStart + rotangle + angle, num_points+1, endpoint=False)
    x_coords = radius * np.cos(angles)
    y_coords = radius * np.sin(angles)
    z_coords = height
    # assuming equidistant sampling
    time_interval = duration / num_points

    points = []
    for i in range(num_points+1):
        t = i * time_interval
        x, y = x_coords[i], y_coords[i]
        z = z_coords  # Since we are in 2D space
        points.append((t, x, y, z))
    return points

def save_to_file(filename, points):
    with open(filename, 'w') as f:
        print(len(points))
        if len(points) == 4:
            t, x, y, z = points
            f.write(f"{t:.2f} {x:.2f} {y:.2f} {z:.2f}\n")
        else:
            for t, x, y, z in points:
                f.write(f"{t:.2f} {x:.2f} {y:.2f} {z:.2f}\n")
    print(f"Data saved to {filename}")


# ----------------------------------------
# ----------------------------------------


radius = 1                # Radius of the circle
num_rotations = 1
rotangle = num_rotations * (2 * np.pi)
points_per_rot = 200
num_points = int(round(points_per_rot*(rotangle/2*np.pi), 0))          # Number of points along the circle
duration = 20                # duration of one rotation
height = 1.6
lockOr = False 
#orOffset = -90
#saveStart = True
#fileName = "test"


# 0 rot in 20 s
saveStart = True
fileName = "0rot"
rotStart = 0
points_speech = generate_circle_points(rotStart, rotangle, radius, height, num_points, duration)
save_to_file(f"./scenes/paths/{fileName}_{num_rotations}_{duration}_p.txt", points_speech)
if saveStart:
    save_to_file(f"./scenes/paths/{rotStart}_{num_rotations}_{duration}_p_start.txt", points_speech[0])

# 0 rot in 20 s
saveStart = True
fileName = "90rot"
rotStart = 90
points_speech = generate_circle_points(rotStart, rotangle, radius, height, num_points, duration)
save_to_file(f"./scenes/paths/{fileName}_{num_rotations}_{duration}_p.txt", points_speech)
if saveStart:
    save_to_file(f"./scenes/paths/{rotStart}_{num_rotations}_{duration}_p_start.txt", points_speech[0])


# 180 rot in 20 s
saveStart = True
fileName = "180rot"
points_noise = generate_circle_points(rotStart, rotangle, radius, height, num_points, duration)
save_to_file(f"./scenes/paths/{fileName}_{num_rotations}_{duration}_p.txt", points_noise)
if saveStart:
    save_to_file(f"./scenes/paths/{rotStart}_{num_rotations}_{duration}_p_start.txt", points_speech[0])


if lockOr:
    orientations = generate_orientations(rotStart, rotangle, num_points, duration)
    save_to_file(f"./scenes/paths/{fileName}_{num_rotations}_{duration}_o.txt", orientations)
    if saveStart:
        save_to_file(f"./scenes/paths/{rotStart}_{num_rotations}_{duration}_o_start.txt", orientations[0])




