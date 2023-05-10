import random
import math
import matplotlib.pyplot as plt

n_samples = 1500
sep_dist = 3 
int_dist = 1.5 
rad = 5.0 

def generate_circle(center_x, center_y, radius, n_samples):
    points = []
    for i in range(n_samples):
        angle = random.uniform(0, 2*math.pi)
        x = center_x + radius*math.cos(angle)
        y = center_y + radius*math.sin(angle)
        points.append((x, y))
    return points


circle1_points = generate_circle(-sep_dist/2 - rad, 0, rad, n_samples)
circle2_points = generate_circle(sep_dist/2 + rad, 0, rad, n_samples)


int_circle1_points = generate_circle(-sep_dist/2, 0, rad, n_samples)
int_circle2_points = generate_circle(sep_dist/2, 0, rad, n_samples)


con_circle1_points = generate_circle(0, 0, rad, n_samples)
con_circle2_points = generate_circle(0, 0, rad-int_dist, n_samples)


fig, axs = plt.subplots(1, 3, figsize=(15, 5)) #pour créer le graph



axs[0].scatter([p[0] for p in circle1_points], [p[1] for p in circle1_points], c='blue', alpha=0.5) #position de chacuns
axs[0].scatter([p[0] for p in circle2_points], [p[1] for p in circle2_points], c='red', alpha=0.5)
axs[0].set_xlim(-rad*4, rad*4)#pts de départs
axs[0].set_ylim(-rad*2, rad*2)
axs[0].set_aspect('equal') #même cercles
axs[0].set_title('Cercles séparés')#mettre titre


axs[1].scatter([p[0] for p in int_circle1_points], [p[1] for p in int_circle1_points], c='blue', alpha=0.5)
axs[1].scatter([p[0] for p in int_circle2_points], [p[1] for p in int_circle2_points], c='red', alpha=0.5)
axs[1].set_xlim(-rad*2, rad*2)
axs[1].set_ylim(-rad*2, rad*2)
axs[1].set_title('Cercles intersectant')


con_circle1 = plt.Circle((0, 0), rad, facecolor='none', edgecolor='blue')
con_circle2 = plt.Circle((0, 0), rad-int_dist, facecolor='none', edgecolor='red')
axs[2].add_artist(con_circle1)
axs[2].add_artist(con_circle2)
axs[2].set_xlim(-rad*2, rad*2)
axs[2].set_ylim(-rad*2, rad*2)
axs[2].set_title('Cercles concentriques')

plt.show()


