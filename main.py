import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the labels and the number of variables
labels=np.array(['Innovation', 'Quality', 'Price', 'Sustainability'])

# Create a dataset with your values
stats = np.array([
    [4, 4, 3, 2],  # L'Oreal
    [3, 3, 4, 4],  # La Roche Posay
    [4, 3, 3, 4],  # Yves Rocher
    [3, 2, 4, 5]   # The Purest Solutions
])

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is circular, so we need to "complete the loop" and append the start to the end.
stats = np.concatenate((stats, stats[:,[0]]), axis=1)
angles += angles[:1]

# Initialize the spider plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw one axe per variable and add labels
plt.xticks(angles[:-1], labels)

# Draw ylabels
ax.set_rlabel_position(30)
plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=12)
plt.ylim(0,5)

# Plot data
ax.plot(angles, stats[0], color='blue', linewidth=2, linestyle='solid', label="L'Oreal")
ax.fill(angles, stats[0], color='blue', alpha=0.25)

ax.plot(angles, stats[1], color='red', linewidth=2, linestyle='solid', label="La Roche Posay")
ax.fill(angles, stats[1], color='red', alpha=0.25)

ax.plot(angles, stats[2], color='green', linewidth=2, linestyle='solid', label="Yves Rocher")
ax.fill(angles, stats[2], color='green', alpha=0.25)

ax.plot(angles, stats[3], color='purple', linewidth=2, linestyle='solid', label="The Purest Solutions")
ax.fill(angles, stats[3], color='purple', alpha=0.25)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Show the plot
plt.show()
