import matplotlib.pyplot as plt
import numpy as np
import glob

# Load all Variant A and B npy files
# variant_a_files = sorted(glob.glob("npyfitnessMatrix_A_run*.npy"))
# variant_b_files = sorted(glob.glob("npyfitnessMatrix_B_run*.npy"))

variant_a_files = sorted(glob.glob("p10g75npyfitnessMatrix_A_run*.npy"))
variant_b_files = sorted(glob.glob("p10g75npyfitnessMatrix_B_run*.npy"))

# Assume all matrices are shape (p, g)
fig, ax = plt.subplots(figsize=(10, 6))

# Plot all individual curves from Variant A (thin lines)
for file in variant_a_files:
    matrix = np.load(file)
    for row in matrix:
        ax.plot(row, color='tab:blue', alpha=0.3, linewidth=1)

# Plot all individual curves from Variant B (thick lines)
for file in variant_b_files:
    matrix = np.load(file)
    for row in matrix:
        ax.plot(row, color='tab:orange', alpha=0.2, linewidth=1)

ax.set_title("All Individual Fitness Curves (A thin, B thick)")
ax.set_xlabel("Generation")
ax.set_ylabel("Fitness")
plt.tight_layout()
plt.grid(True)
plt.show()
