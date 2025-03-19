import random
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time

class SOLUTION:


    def __init__(self, solutionID):
        self.weights = np.random.rand(3, 2) * 2 - 1
        self.myID = solutionID

        self.solutionID = solutionID
        

    
    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        command = f"python3 simulate.py {mode} {self.myID} &"
        os.system(command)


    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f"fitness{self.myID}.txt"

        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        with open(fitnessFileName, "r") as f:
            self.fitness = float(f.read())

        print(f"Fitness of solution {self.myID}: {self.fitness}")

        os.system(f"rm {fitnessFileName}")



    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-3, 3, 0.5], size=[1, 1, 1])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[1, 0, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[2, 0, 1])
        pyrosim.End()


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # Sensor neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        # Motor neurons
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # Synapses using weights
        for currentRow in range(3):         # Sensor neurons
            for currentColumn in range(2):  # Motor neurons
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow,
                    targetNeuronName=currentColumn + 3,
                    weight=weight
                )

        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0, 2)  # choose sensor neuron
        randomColumn = random.randint(0, 1)  # choose motor neuron
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1


    def Set_ID(self, newID):
        self.myID = newID
