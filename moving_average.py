import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, size=100)

# Define window size for moving average
window_size = 5

# Calculate moving average
moving_avg = np.convolve(y, np.ones(window_size)/window_size, mode='valid')

# Create the figure and plot
fig, ax = plt.subplots()

# Plot the original time series
ax.plot(x, y, label='Original')

# Plot the moving average
ax.plot(x[window_size-1:], moving_avg, label=f'Moving Average (window size = {window_size})')

# Set the axis labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Moving Average')

# Add a legend
ax.legend()

# Display the plot
plt.show()
