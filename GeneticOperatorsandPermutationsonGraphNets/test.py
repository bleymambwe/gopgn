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
            NN().all_branches[branch_root] = node

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
        node = self.root
        return node

    def delete(self):
        pass

    def connect(self):
        pass

class NN(Branch, Configurations, Mutation, CrossOver):
    def __init__(self):
        super().__init__()
        self.all_branches = []
        self.init_nodes()

    def init_nodes(self, num_nodes=3):
        # Create three nodes and append their branch_roots to all_branches
        for _ in range(num_nodes):
            node = Branch()
            branch_root = node.create_graph()
            self.all_branches.append(branch_root)

BranchFactory.init_branches()
model = NN()

print(model.all_branches)
