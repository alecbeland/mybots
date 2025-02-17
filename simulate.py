import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import pybullet_data
import numpy as np

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
backLegSensorValues = np.zeros(100)

frontLegSensorValues = np.zeros(100)

for i in range(100):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	time.sleep(0.0166)
	# print(i)
p.disconnect()

print(backLegSensorValues)
print(frontLegSensorValues)
np.save("data/backLegSensorValues", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)