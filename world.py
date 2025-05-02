import pybullet as p

class WORLD:

    def __init__(self):
        # Load floor
        self.planeId = p.loadURDF("plane.urdf")

        # Load and store all block IDs
        self.block_ids = p.loadSDF("world.sdf")

        # Set friction and make blocks static
        for block_id in self.block_ids:
            p.changeDynamics(
                bodyUniqueId=block_id,
                linkIndex=-1,  # for base link
                mass=0,  # makes the object static
                lateralFriction=5.0  # high friction so robot can't just slide them
            )

        # # Load environment (world.sdf)
        # p.loadSDF("world.sdf")