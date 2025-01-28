import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add Gravity
p.setGravity(0,0,-9.8)

# Add Floor
planeId = p.loadURDF("plane.urdf")

# Simulate "box"
p.loadSDF("box.sdf")

for i in range(1000):
	p.stepSimulation()
	time.sleep(0.0166)
	print(i)
p.disconnect()
