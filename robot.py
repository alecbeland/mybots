import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR
import numpy as np
import constants as c
import os

class ROBOT:

    def __init__(self, solutionID):
        # Load the robot URDF
        self.robotId = p.loadURDF("body.urdf")
        self.solutionID = solutionID
        
        # Neural Network nndf
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        
        # Prepare simulation
        pyrosim.Prepare_To_Simulate(self.robotId)
        
        # Prepare sensors
        self.Prepare_To_Sense()

        # Prepare motors
        self.Prepare_To_Act()

        os.system(f"rm brain{solutionID}.nndf")


    def Prepare_To_Sense(self):
        # Attach a sensor to every link in the robot
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
            
    
    def Prepare_To_Act(self):
        self.motors = {}
        
        # Attach motors to every joint
        for jointName in pyrosim.jointNamesToIndices:
            # print(jointName)
            self.motors[jointName] = MOTOR(jointName)
            # initialize random weight
            self.sinVals = np.linspace(0, (2 * np.pi), c.NUM_STEPS)


    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self, t)
                print(jointName, desiredAngle)



    def Think(self):
        self.nn.Update()
        # self.nn.Print()


    def Save_Values(self):
        for sensor in self.sensors.values():
            sensor.Save_Values()
        for motor in self.motors.values():
            motor.Save_Values()


    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        with open(f"tmp{self.solutionID}.txt", "w") as f:
            f.write(str(xCoordinateOfLinkZero))

        os.system(f"mv tmp{self.solutionID}.txt fitness{self.solutionID}.txt")