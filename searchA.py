import os
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER


for run in range(10):
    phc = PARALLEL_HILL_CLIMBER(runID=run, variant="A")
    phc.Evolve()

# phc.Show_Best()



#random search code commented out
# for i in range(c.NUM_SIMULATIONS):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")