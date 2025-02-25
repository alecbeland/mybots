import pyrosim.pyrosim as pyrosim
import numpy as np

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(1000)  # Initialize sensor values array


    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if t == len(self.values) - 1:
            # Print the full sensor vector at the last time step
            print(self.values)

    
    def Save_Values(self):
        np.save(f"data/{self.linkName}_sensorValues.npy", self.values)