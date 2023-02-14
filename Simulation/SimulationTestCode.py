import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()

n = 100

# Set the axis limits
ax.set_xlim(0, n)
ax.set_ylim(0, n)

# Create an array of 100 random points
points = np.random.rand(100, 2)

# Create a scatter plot of the points
scatter = ax.scatter(points[:, 0], points[:, 1])

# Define an update function for the animation
def update(num):
    # Move the points by a small random amount
    points[:, 0] += np.random.randn(100) * 0.01
    points[:, 1] += np.random.randn(100) * 0.01
    
    # Update the scatter plot
    scatter.set_offsets(points)

# Create an animation
ani = FuncAnimation(fig, update, frames=range(100), repeat=True)

# Display the animation
plt.show()
