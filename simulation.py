import pybullet as p
import sys
import pybullet_data
from world import WORLD
from robot import ROBOT
import constants as c
import pyrosim.pyrosim as pyrosim
import time


class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        # Connect to pybullet
        self.directOrGUI = directOrGUI

        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(c.GRAVITY_X, c.GRAVITY_Y, c.GRAVITY_Z)
        
        # Created world and robot instances
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

        # Prepare sim
        # pyrosim.Prepare_To_Simulate(self.robot.robotId)


    def Run(self):
        for i in range(c.NUM_STEPS):
            #print(i)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            # --- If too fast for viewing uncomment ---
            # if self.directOrGUI == "GUI":
            #     time.sleep(0.008)

        self.robot.Save_Values()

    def __del__(self):
        # End Simulation
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()