import pyrosim.pyrosim as pyrosim

# Define world and save to box.sdf
pyrosim.Start_SDF("box.sdf")

# Add a cube "Box" with pos and size
length = 1
width = 1
height = 1
x = 0
y = 0.5
z = 0
pyrosim.Send_Cube(name="Box", pos=[x,z,y], size=[length, width, height])

# Add a second cube "Box2" with pos and size
length = 1
width = 1
height = 1
x = 1
y = 1.5
z = 0
pyrosim.Send_Cube(name="Box2", pos=[x,z,y], size=[length, width, height])

pyrosim.End()
