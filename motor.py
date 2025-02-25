
import pyrosim.pyrosim as pyrosim
import robot
import constants as c
import pybullet as p
import numpy as np

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    
    def Prepare_To_Act(self):
        if "Torso_FrontLeg" in self.jointName:
            self.frequency = c.FREQUENCY * 0.5
        else:
            self.frequency = c.FREQUENCY

        print(f"Motor {self.jointName} frequency: {self.frequency}")

        # Set motor properties from constants
        self.amplitude = c.AMPLITUDE
        # self.frequency = c.FREQUENCY
        self.offset = c.PHASE_OFFSET
        # Initialize motor command vector
        self.motorValues = self.amplitude * np.sin(
            self.frequency * np.linspace(0, 2 * np.pi, c.NUM_STEPS) + self.offset
        )
        print(f"Motor {self.jointName} motorValues sample: {self.motorValues[:10]}")



    def Set_Value(self, t, robot):
        targetLocation = self.motorValues[t]
        print(f"Motor {self.jointName} at t={t}: targetLocation={targetLocation}")


        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot.robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = targetLocation,
            maxForce = c.MAX_FORCE)
        
    
    def Save_Values(self):
        np.save(f"data/{self.jointName}_motorValues.npy", self.motorValues)
