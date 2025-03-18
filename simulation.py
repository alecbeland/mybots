import pybullet as p
import pybullet_data
from world import WORLD
from robot import ROBOT
import constants as c
import pyrosim.pyrosim as pyrosim
import time


class SIMULATION:

    def __init__(self):
        # Connect to pybullet
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Set Gravity
        p.setGravity(c.GRAVITY_X, c.GRAVITY_Y, c.GRAVITY_Z)
        
        # Created world and robot instances
        self.world = WORLD()
        self.robot = ROBOT()

        # Prepare sim
        # pyrosim.Prepare_To_Simulate(self.robot.robotId)


    def Run(self):
        for i in range(c.NUM_STEPS):
            #print(i)
            p.stepSimulation()
            time.sleep(0.0166)
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

        self.robot.Save_Values()

    def __del__(self):
        # End Simulation
        p.disconnect()
