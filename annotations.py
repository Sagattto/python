import matplotlib.pyplot as plt

# Prepare the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the graph
plt.plot(x, y, marker='o')

# Add annotations
plt.annotate('Max Value', xy=(5, 10), xytext=(4, 8),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
             
# Add text
plt.text(2, 4, 'Important Point', ha='center', va='bottom')

# Set the axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set the graph title
plt.title('Line Plot with Annotations')

# Display the graph
plt.show()

