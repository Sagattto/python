import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create a figure with subplots arranged in a grid
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot the first subplot (line plot)
axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('sin(x)')
axs[0, 0].set_title('Sine')

# Plot the second subplot (line plot)
axs[0, 1].plot(x, y2, color='red')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('cos(x)')
axs[0, 1].set_title('Cosine')

# Plot the third subplot (line plot)
axs[1, 0].plot(x, y3, color='green')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('tan(x)')
axs[1, 0].set_title('Tangent')

# Hide the fourth subplot
axs[1, 1].axis('off')

# Adjust spacing between subplots
fig.tight_layout()

# Display the figure
plt.show()

