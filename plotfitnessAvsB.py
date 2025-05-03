import numpy as np
import matplotlib.pyplot as plt
import glob

# Load all A and B .npy files
# a_files = sorted(glob.glob("npyfitnessMatrix_A_run*.npy"))
# b_files = sorted(glob.glob("npyfitnessMatrix_B_run*.npy"))

# a_files = sorted(glob.glob("p10g75npyfitnessMatrix_A_run*.npy"))
# b_files = sorted(glob.glob("p10g75npyfitnessMatrix_B_run*.npy"))

a_files = sorted(glob.glob("p10g200npyfitnessMatrix_A_run*.npy"))
b_files = sorted(glob.glob("p10g200npyfitnessMatrix_B_run*.npy"))

# Load matrices and convert to positive fitness if needed
a_matrices = [np.load(f) for f in a_files]
b_matrices = [np.load(f) for f in b_files]

# Compute average and std dev across runs
a_avg = np.mean(a_matrices, axis=0).mean(axis=0)
a_std = np.std(a_matrices, axis=0).mean(axis=0)

b_avg = np.mean(b_matrices, axis=0).mean(axis=0)
b_std = np.std(b_matrices, axis=0).mean(axis=0)

generations = range(len(a_avg))

# Plot
plt.figure(figsize=(10, 5))
plt.plot(generations, a_avg, label='Variant A', linewidth=2)
plt.fill_between(generations, a_avg - a_std, a_avg + a_std, alpha=0.3)

plt.plot(generations, b_avg, label='Variant B', linewidth=2)
plt.fill_between(generations, b_avg - b_std, b_avg + b_std, alpha=0.3)

plt.xlabel("Generation")
plt.ylabel("Fitness (Higher is better)")
plt.title("A/B Variant Fitness Comparison")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
