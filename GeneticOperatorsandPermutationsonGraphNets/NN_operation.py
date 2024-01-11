import random
from crossover import CrossOver
from selection import Selection
from mutation import Mutation


class BranchFactory():
    @staticmethod
    def init_branches(branches=3):
        # creates new branches
        for _ in range(branches):
            node = Branch()
            branch_root = node.create_graph()
            NN.all_branches.append(branch_root)

class Configurations():
    def __init__(self):
        self.configs = None

class Branch():
    def __init__(self):
        self.branches = None
        self.nodes = None
        self.edges = None
        self.root = None

    def create_graph(self):
        node = Branch()
        data = random.randint(0,10)
        node.setData(data)
        self.root = node
        return self.root
    
    def setData(self,data):
        self.data = data

    def delete(self):
        pass

    def connect(self):
        pass

class NN(Branch, Configurations, Mutation, CrossOver):
    all_branches = []  # Declare all_branches as a class variable

    def __init__(self):
        super().__init__()

# Access all_branches directly through the class
BranchFactory.init_branches()
model = NN()

print(model.all_branches)
print(model.all_branches[0].data)
#print(model.all_branches[1].data)
# print(model.all_branches[2].data)

