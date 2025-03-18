import os
import constants as c
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()



#random search code commented out
# for i in range(c.NUM_SIMULATIONS):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")