import matplotlib.pyplot as plt

data = [5887, 4689, 4839]   # The list of data
x_labels = ["round 1", "round 2", "round 3"]  # The x-axis labels

plt.plot(x_labels, data, marker='o')     # Create the line graph with custom x-axis labels
plt.axhline(y=5873, color='r', linestyle='-')  # Add a horizontal line at y=4
plt.xlabel('Rounds')         # Add a label to the x-axis
plt.ylabel('Ticks')          # Add a label to the y-axis
plt.title('Number of Ticks')   # Add a title to the graph
plt.show()                   # Display the graph