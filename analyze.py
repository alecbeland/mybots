import numpy as np
import matplotlib.pyplot as plt

# Load motor data
back_leg_data = np.loadtxt("motor_commands_back.txt")
front_leg_data = np.loadtxt("motor_commands_front.txt")

# Plot the data
plt.plot(back_leg_data, label="Back Leg", color="blue")
plt.plot(front_leg_data, label="Front Leg", color="red", linestyle="dashed")
plt.legend()
plt.title("Motor Command Sinusoidal Pattern")
plt.xlabel("Time Step")
plt.ylabel("Target Angle (radians)")
plt.show()



# backLegSensorValues = np.load("data/backLegSensorValues.npy")
# frontLegSensorValues = np.load("data/frontLegSensorValues.npy")

# print(backLegSensorValues)
# print(frontLegSensorValues)

# plt.plot(backLegSensorValues, label="Back Leg", linewidth=3)
# plt.plot(frontLegSensorValues, label="Front Leg")
# plt.legend()
# plt.show()
