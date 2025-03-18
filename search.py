import os
import constants as c

for i in range(c.NUM_SIMULATIONS):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")