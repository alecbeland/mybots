import pyrosim.pyrosim as pyrosim

# Define world and save to boxes.sdf
pyrosim.Start_SDF("world.sdf")

# Base cube size
length = 1
width = 1
height = 1

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5], size=[length, width, height])

pyrosim.End()
