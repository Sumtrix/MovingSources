import numpy as np

def generate_circle_points(rotangle, radius, height, orOffset, num_points, duration, lockorientation=False):
    angle = rotangle / num_points
    angles = np.linspace(0, rotangle + angle, num_points+1, endpoint=False)
    x_coords = radius * np.cos(angles)
    y_coords = radius * np.sin(angles)
    z_coords = height
    # assuming equidistant sampling
    time_interval = duration / num_points

    points = []
    orientation = []
    for i in range(num_points+1):
        t = i * time_interval
        x, y = x_coords[i], y_coords[i]
        z = z_coords  # Since we are in 2D space
        points.append((t, x, y, z))
    if lockorientation:
        for i in range(num_points+1):
            t = i * time_interval
            orientation.append((t, (angles[i]/np.pi)*180 + orOffset, 0, 0))
        points = np.vstack((points, orientation))
    return points

def save_to_file(filename, points):
    with open(filename, 'w') as f:
        for t, x, y, z in points:
            f.write(f"{t:.2f} {x:.2f} {y:.2f} {z:.2f}\n")
    print(f"Data saved to {filename}")


# ----------------------------------------
# ----------------------------------------

radius = 3                # Radius of the circle
rotangle = 3 * (2 * np.pi)
points_per_rot = 200
num_points = points_per_rot*(rotangle/2*np.pi)          # Number of points along the circle
speed = 20                # duration of one rotation
height = 1.5

lock = True 
orOffset = -90

data = generate_circle_points(rotangle, radius, height, orOffset, num_points, speed, lock)
save_to_file("circle_path.txt", data)
