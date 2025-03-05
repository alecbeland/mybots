
import pyrosim.pyrosim as pyrosim
import robot
import constants as c
import pybullet as p
import numpy as np

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, desiredAngle, robot):
        targetLocation = desiredAngle
        #print(f"Motor {self.jointName} at t={t}: targetLocation={targetLocation}")


        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot.robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = targetLocation,
            maxForce = c.MAX_FORCE)
       
