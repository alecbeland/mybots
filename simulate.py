# import time
# import numpy as np
# import random
# import constants as c
from simulation import SIMULATION





# # Add Floor
# planeId = p.loadURDF("plane.urdf")

# # Add Robot
# robotId = p.loadURDF("body.urdf")

# # Simulate "boxes"
# p.loadSDF("world.sdf")


# # Initialize vector to store sensor vals
# backLegSensorValues = np.zeros(c.NUM_STEPS)

# frontLegSensorValues = np.zeros(c.NUM_STEPS)

# # Create Sinusoidal Motor Command Vector
# amplitude_BackLeg = c.AMPLITUDE_BACK_LEG
# frequency_BackLeg = c.FREQUENCY_BACK_LEG
# phaseOffset_BackLeg = c.PHASE_OFFSET_BACK_LEG

# amplitude_FrontLeg = c.AMPLITUDE_FRONT_LEG
# frequency_FrontLeg = c.FREQUENCY_FRONT_LEG
# phaseOffset_FrontLeg = c.PHASE_OFFSET_FRONT_LEG

# num_steps = c.NUM_STEPS

# targetAngles_BackLeg = amplitude_BackLeg * np.sin(frequency_BackLeg * np.linspace(0, 2*np.pi, num_steps) + phaseOffset_BackLeg)
# targetAngles_FrontLeg = amplitude_FrontLeg * np.sin(frequency_FrontLeg * np.linspace(0, 2*np.pi, num_steps) + phaseOffset_FrontLeg)
# # np.savetxt("motor_commands_back.txt", targetAngles_BackLeg)
# # np.savetxt("motor_commands_front.txt", targetAngles_FrontLeg)
# # np.savetxt("motor_commands.txt", targetAngles)
# # exit()

# for i in range(1000):
# 	p.stepSimulation()
# 	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	pyrosim.Set_Motor_For_Joint(
# 		bodyIndex = robotId,
# 		jointName = "Torso_BackLeg",
# 		controlMode = p.POSITION_CONTROL,
# 		targetPosition = targetAngles_BackLeg[i],
# 		maxForce = c.MAX_FORCE_BACK_LEG)
# 	pyrosim.Set_Motor_For_Joint(
# 		bodyIndex = robotId,
# 		jointName = "Torso_FrontLeg",
# 		controlMode = p.POSITION_CONTROL,
# 		targetPosition = targetAngles_FrontLeg[i],
# 		maxForce = c.MAX_FORCE_FRONT_LEG)
# 	time.sleep(0.0166)
# 	print(i)

# print(backLegSensorValues)
# print(frontLegSensorValues)
# np.save("data/backLegSensorValues", backLegSensorValues)
# np.save("data/frontLegSensorValues", frontLegSensorValues)

simulation = SIMULATION()
simulation.Run()