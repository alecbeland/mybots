import pyrosim.pyrosim as pyrosim

# Define world and save to boxes.sdf
pyrosim.Start_SDF("boxes.sdf")

# Base cube size
base_length = 1
base_width = 1
base_height = 1

# Grid size (5x5)
grid_size = 5
tower_height = 10

# Loop through rows
for i in range(5):    
    
    # Loop through columns
    for j in range(5):
        x = i
        y = j
        z = 0.5
        length = base_length
        width = base_width
        height = base_height

        # Stack block tower at location
        for k in range(10):
            pyrosim.Send_Cube(name=f"Box({i},{j},{k})", pos=[x,y,z], size=[length, width, height])
            z += height
            length *= 0.9
            width *= 0.9
            height *= 0.9

pyrosim.End()
