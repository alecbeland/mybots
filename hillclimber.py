import constants as c
import copy
from solution import SOLUTION


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()


    def Evolve(self):
        # Show the first random solution visually
        self.parent.Evaluate("GUI")

        # Now evaluate the parent blindly before evolution begins
        self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()


    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child


    def Spawn(self):
        self.child = copy.deepcopy(self.parent)


    def Print(self):
        print(f"\n\nParent fitness: {self.parent.fitness} | Child fitness: {self.child.fitness}\n")


    def Show_Best(self):
        self.parent.Evaluate("GUI")
