import pyrosim.pyrosim as pyrosim

# Define world and save to box.sdf
pyrosim.Start_SDF("box.sdf")

# Add a cube "Box" with pos and size
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5], size=[1,1,1])

pyrosim.End()
