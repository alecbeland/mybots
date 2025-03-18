import pyrosim.pyrosim as pyrosim
import random

# Define world and save to boxes.sdf

# Base cube size
length = 1
width = 1
height = 1

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], size=[length, width, height])
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    # Links
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length, width, height]) # Root Link (Torso)
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length, width, height])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length, width, height])

    # Joints
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,
                        type = "revolute", position = [1,0,1])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,
                        type = "revolute", position = [2,0,1])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    sensor_neurons = [0, 1, 2]
    motor_neurons = [3, 4]

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    for sensor in sensor_neurons:
        for motor in motor_neurons:
            weight = random.uniform(-1, 1)  # assign weight to rand search
            pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=motor, weight=weight)

    pyrosim.End()

def Create_Robot():
    Generate_Body()
    Generate_Brain()
    

if __name__ == '__main__':
    Create_World()
    Create_Robot()
    