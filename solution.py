import random
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
from robot import ROBOT
import time
import constants as c

class SOLUTION:


    def __init__(self, solutionID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = solutionID
        self.solutionID = solutionID
        

    
    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        command = f"python3 simulate.py {mode} {self.myID} 2&>1 &"
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
        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        # Upper Legs
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        # Lower Legs
        # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, -0.5, -0.5], size=[0.2, 1, 0.2], orientation=[-1.57, 0, 0])
        # pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, -0.5, -0.5], size=[0.2, 1, 0.2])
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[-0.5, 0, -0.5], size=[1, 0.2, 0.2])
        # pyrosim.Send_Cube(name="RightLowerLeg", pos=[0.5, 0, -0.5], size=[1, 0.2, 0.2])
        # LOWER LEG LINKS (vertical, hanging down)

        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0.1, -0.5], size=[0.2, 0.2, 1.0])
        pyrosim.Send_Cube(name="BackLowerLeg",  pos=[0, -0.1, -0.5], size=[0.2, 0.2, 1.0])
        pyrosim.Send_Cube(name="LeftLowerLeg",  pos=[-0.1, 0, -0.5], size=[0.2, 0.2, 1.0])
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0.1, 0, -0.5], size=[0.2, 0.2, 1.0])





        # Upper Leg Joints
        pyrosim.Send_Joint(name="Torso_BackLeg", 
                           parent="Torso", 
                           child="BackLeg",
                           type="revolute", 
                           position=[0, -0.5, 1], 
                           jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_FrontLeg", 
                           parent="Torso", 
                           child="FrontLeg",
                           type="revolute", 
                           position=[0, 0.5, 1], 
                           jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_LeftLeg", 
                           parent="Torso", 
                           child="LeftLeg",
                           type="revolute", 
                           position=[-0.5, 0, 1], 
                           jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_RightLeg", 
                           parent="Torso", 
                           child="RightLeg",
                           type="revolute", 
                           position=[0.5, 0, 1], 
                           jointAxis = "1 0 0")
        #Lower Leg Joints
        # pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", 
        #                    parent="FrontLeg", 
        #                    child="FrontLowerLeg",
        #                    type="revolute", 
        #                    position=[0, 1, 0],       # full length of front leg in +y
        #                    jointAxis="1 0 0")

        # pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", 
        #                 parent="BackLeg", 
        #                 child="BackLowerLeg", 
        #                 type="revolute", 
        #                 position=[0, -1, 0],      # full length of back leg in -y
        #                 jointAxis="1 0 0")

        # pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", 
        #                 parent="LeftLeg", 
        #                 child="LeftLowerLeg",
        #                 type="revolute", 
        #                 position=[-1, 0, 0],      # full length of left leg in -x
        #                 jointAxis="0 0 1")

        # pyrosim.Send_Joint(name="RightLeg_RightLowerLeg",
        #                 parent="RightLeg",
        #                 child="RightLowerLeg",
        #                 type="revolute",
        #                 position=[1, 0, 0],       # full length of right leg in +x
        #                 jointAxis="0 0 1")
        # LOWER LEG JOINTS (connect at end of upper legs, axis to swing vertically)

        pyrosim.Send_Joint(
            name="FrontLeg_FrontLowerLeg",
            parent="FrontLeg",
            child="FrontLowerLeg",
            type="revolute",
            position=[0, 1, 0],
            jointAxis="1 0 0"
        )

        pyrosim.Send_Joint(
            name="BackLeg_BackLowerLeg",
            parent="BackLeg",
            child="BackLowerLeg",
            type="revolute",
            position=[0, -1, 0],
            jointAxis="1 0 0"
        )

        pyrosim.Send_Joint(
            name="LeftLeg_LeftLowerLeg",
            parent="LeftLeg",
            child="LeftLowerLeg",
            type="revolute",
            position=[-1, 0, 0],
            jointAxis="0 0 1"
        )

        pyrosim.Send_Joint(
            name="RightLeg_RightLowerLeg",
            parent="RightLeg",
            child="RightLowerLeg",
            type="revolute",
            position=[1, 0, 0],
            jointAxis="0 0 1"
        )

        pyrosim.End()
        


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # Sensor neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg")


        # Motor neurons
        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")

        pyrosim.Send_Motor_Neuron(name=13, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLowerLeg")


        # Synapses using weights
        for currentRow in range(c.numSensorNeurons):         # Sensor neurons
            for currentColumn in range(c.numMotorNeurons):  # Motor neurons
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow,
                    targetNeuronName=currentColumn + c.numSensorNeurons,
                    weight=weight
                )
        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)  # choose sensor neuron
        randomColumn = random.randint(0, c.numMotorNeurons - 1)  # choose motor neuron
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1


    def Set_ID(self, newID):
        self.myID = newID
