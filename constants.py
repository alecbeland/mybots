import numpy as np

# Physics constants
GRAVITY_X = 0
GRAVITY_Y = 0
GRAVITY_Z = -9.8

# Sensor array size
SENSOR_ARRAY_SIZE = 1000

# Sinusoidal Motor Command Parameters
AMPLITUDE_BACK_LEG = np.pi / 3
FREQUENCY_BACK_LEG = 3.5
PHASE_OFFSET_BACK_LEG = 0

AMPLITUDE_FRONT_LEG = np.pi / 3
FREQUENCY_FRONT_LEG = 3.5
PHASE_OFFSET_FRONT_LEG = np.pi / 2

# blahblah
AMPLITUDE = np.pi / 3
FREQUENCY = 3.5
PHASE_OFFSET = 0
MAX_FORCE = 200

# Simulation steps
NUM_STEPS = 1000

# Number of generations
numberOfGenerations = 20

populationSize = 10

# Max force applied by motors
MAX_FORCE_BACK_LEG = 200
MAX_FORCE_FRONT_LEG = 200

motorJointRange = 0.2

# Neural Network Constants
numSensorNeurons = 4
numMotorNeurons = 8