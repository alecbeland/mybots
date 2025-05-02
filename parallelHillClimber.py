import constants as c
import copy
from solution import SOLUTION
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.parents[i].Create_World()
            self.nextAvailableID += 1




    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
        # # Show the first random solution visually
        # self.parent.Evaluate("GUI")

        # # Now evaluate the parent blindly before evolution begins
        # self.parent.Evaluate("DIRECT")
        

    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()


    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()


    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]


    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")

        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()



    def Print(self):
        print("\n")

        for key in self.parents:
            print(f"Parent {key} fitness: {self.parents[key].fitness} | Child {key} fitness: {self.children[key].fitness}")

        print("\n")


    def Show_Best(self):
        bestParent = None
        bestFitness = float('inf')

        for i, parent in self.parents.items():
            if parent.fitness < bestFitness:
                bestFitness = parent.fitness
                bestParent = parent
                bestID = i

        print(f"Best solution is Parent {bestID} with fitness: {bestFitness}")
        bestParent.Start_Simulation("GUI")

