import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.NUM_STEPS)  # Initialize sensor values array


    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if t == len(self.values) - 1:
            # Print the full sensor vector at the last time step
            #print(self.values)
            pass

    
    def Save_Values(self):
        np.save(f"data/{self.linkName}_sensorValues.npy", self.values)