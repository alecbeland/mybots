import pyrosim.pyrosim as pyrosim

# Define world and save to boxes.sdf

# Base cube size
length = 1
width = 1
height = 1

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], size=[length, width, height])
    pyrosim.End()

def Create_Robot():
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

if __name__ == '__main__':
    Create_World()
    Create_Robot()