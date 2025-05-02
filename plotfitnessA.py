import numpy as np
import matplotlib.pyplot as plt

# Load all 4 runs of Variant B
runs = [np.load(f"npyfitnessMatrix_A_run{r}.npy") for r in range(5)]

# Compute mean fitness across population for each generation
averages = [run.mean(axis=0) for run in runs]

# Convert to numpy array for easier math
averages = np.array(averages)

# Mean and std across runs (shape: [generations])
mean_curve = averages.mean(axis=0)
std_curve = averages.std(axis=0)

# Plotting
generations = range(len(mean_curve))
plt.plot(generations, mean_curve, label='Variant A (mean)', linewidth=2)
plt.fill_between(generations, mean_curve - std_curve, mean_curve + std_curve, alpha=0.3, label='±1 std. dev.')

plt.title("Average Fitness Over Generations (Variant B)")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
