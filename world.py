import pybullet as p

class WORLD:

    def __init__(self):
        # Load floor
        self.planeId = p.loadURDF("plane.urdf")

        # Load environment (world.sdf)
        p.loadSDF("world.sdf")