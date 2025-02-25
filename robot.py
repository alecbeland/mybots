import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self):
        # Load the robot URDF
        self.robotId = p.loadURDF("body.urdf")
        
        # Prepare simulation
        pyrosim.Prepare_To_Simulate(self.robotId)
        
        # Prepare sensors
        self.Prepare_To_Sense()

        # Prepare motors
        self.Prepare_To_Act()

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
            print(jointName)
            self.motors[jointName] = MOTOR(jointName)


    def Act(self, t):
        for motor in self.motors.values():
            motor.Set_Value(t, self)

    
    def Save_Values(self):
        for sensor in self.sensors.values():
            sensor.Save_Values()
        for motor in self.motors.values():
            motor.Save_Values()