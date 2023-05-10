import matplotlib.pyplot as plt
import math
import random

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
rad = 5.0 
sep_dist = 3 
n_samples = 1500

def generate_circle(center_x, center_y, radius, n_samples):
    points = []
    for i in range(n_samples):
        angle = random.uniform(0, 2*math.pi)
        x = center_x + radius*math.cos(angle)
        y = center_y + radius*math.sin(angle)
        points.append((x, y))
    return points


circle1_points = generate_circle(-sep_dist/2 - rad, 0, rad, n_samples)


axs[0].scatter([p[0] for p in circle1_points], [p[1] for p in circle1_points], c='blue', alpha=0.5)
axs[0].set_xlim(-rad*4, rad*4)
axs[0].set_ylim(-rad*2, rad*2)

angle = random.uniform(0, 2*math.pi)
angle

