import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import pybullet_data
import numpy as np
import random

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add Gravity
p.setGravity(0,0,-9.8)

# Add Floor
planeId = p.loadURDF("plane.urdf")

# Add Robot
robotId = p.loadURDF("body.urdf")

# Simulate "boxes"
p.loadSDF("world.sdf")

# Prep Pyrosim for Simulation
pyrosim.Prepare_To_Simulate(robotId)

# Initialize vector to store sensor vals
backLegSensorValues = np.zeros(1000)

frontLegSensorValues = np.zeros(1000)

# Create Sinusoidal Motor Command Vector
amplitude_BackLeg = np.pi/3
frequency_BackLeg = 3.5
phaseOffset_BackLeg = 0

amplitude_FrontLeg = np.pi/3
frequency_FrontLeg = 3.5
phaseOffset_FrontLeg = np.pi/2

num_steps = 1000

targetAngles_BackLeg = amplitude_BackLeg * np.sin(frequency_BackLeg * np.linspace(0, 2*np.pi, num_steps) + phaseOffset_BackLeg)
targetAngles_FrontLeg = amplitude_FrontLeg * np.sin(frequency_FrontLeg * np.linspace(0, 2*np.pi, num_steps) + phaseOffset_FrontLeg)
# np.savetxt("motor_commands_back.txt", targetAngles_BackLeg)
# np.savetxt("motor_commands_front.txt", targetAngles_FrontLeg)
# np.savetxt("motor_commands.txt", targetAngles)
# exit()

for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robotId,
		jointName = "Torso_BackLeg",
		controlMode = p.POSITION_CONTROL,
		targetPosition = targetAngles_BackLeg[i],
		maxForce = 20)
	pyrosim.Set_Motor_For_Joint(
		bodyIndex = robotId,
		jointName = "Torso_FrontLeg",
		controlMode = p.POSITION_CONTROL,
		targetPosition = targetAngles_FrontLeg[i],
		maxForce = 20)
	time.sleep(0.0166)
	print(i)
p.disconnect()

print(backLegSensorValues)
print(frontLegSensorValues)
np.save("data/backLegSensorValues", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)