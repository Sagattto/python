import matplotlib.pyplot as plt

# Prepare the data
x = ['A', 'B', 'C', 'D', 'E']
y = [25, 18, 30, 15, 22]

# Create the bar chart
plt.bar(x, y)

# Set the axis labels
plt.xlabel('Category')
plt.ylabel('Value')

# Set the chart title
plt.title('Bar Chart')

# Display the chart
plt.show()
