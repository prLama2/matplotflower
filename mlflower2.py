import numpy as np
import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

#create figure and axis
fig, ax = plt.subplots()
ax.axis('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

#flower's initial line
flower_line, = plt.plot([], [], lw=2)

#generate flower coordinates
def generate_flower(theta, petals=6, radius=2):
    r = radius*np.cos(petals*theta)
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x,y

#intilize function for animation
def init():
    flower_line.set_data([], [])
    return flower_line,

#animation update function
def update_with_bloom(frame):
    theta = np.linspace(0, 2 * np.pi, 1000)
    radius = frame/50
    x, y = generate_flower(theta, petals=8, radius=1+0.2 *np.sin(frame*0.1))
    color = cm.viridis(frame/100)
    flower_line.set_data(x, y)
    flower_line.set_color(color)
    return flower_line,

#create animation
ani_bloom = FuncAnimation(fig, update_with_bloom, frames=np.arange(1,101), init_func=init, blit=True)

plt.show()

#saving gif
blooming_flower_path = "/mnt/data/blooming_flower.gif"
ani_bloom.save(blooming_flower_path, writer="imageagick", fps=30)

blooming_flower_path

