import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('FINAL DATA(Trial 1).csv')

# Extract the timepoints (first column, skipping header)
timepoints = df.iloc[1:, 0].values  # [0, 4]

# Get OD600 values for each sample at each timepoint
od_values_t0 = df.iloc[0, 1:].values  # Hour 0 values
od_values_t4 = df.iloc[1, 1:].values  # Hour 4 values
print(od_values_t0)

# Sort samples by ascending OD600 at Hour 4
sorted_indices = np.argsort(od_values_t4)
samples = np.array(['Replicate 1', 'Replicate 2', 'Puc 1', 'Puc 2'])
od_values_t0 = od_values_t0[sorted_indices]
od_values_t4 = od_values_t4[sorted_indices]

# Set up the bar positions
x = np.arange(len(samples))
width = 0.35

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create bars for each timepoint
bars1 = ax.bar(x - width/2, od_values_t0, width, label='Initial', alpha=0.8)
bars2 = ax.bar(x + width/2, od_values_t4, width, label='Final', alpha=0.8)

# Customize the plot
ax.set_xlabel('Sample', fontsize=12, fontweight='bold')
ax.set_ylabel('OD600', fontsize=12, fontweight='bold')
ax.set_title('Trial 2 OD600 Measurements', fontsize=14, fontweight='bold')
ax.set_xticks(x, samples)
#ax.set_yticks(np.arange(0, 1.6, 0.2))
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Export pdf
plt.savefig("trial1", dpi=300)
plt.close()