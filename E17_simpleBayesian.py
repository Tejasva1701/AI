# Write a program to construct sample bayesian network

class Node:
    def __init__(self, name, parents, cpt):
        self.name = name
        self.parents = parents
        self.cpt = cpt


class BayesianNetwork:
    def __init__(self, nodes):
        self.nodes = nodes

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

    def get_probability(self, node, values):
        if not node.parents:
            return node.cpt[0] if values[node.name] else node.cpt[1]
        parent_values = [values[parent] for parent in node.parents]
        index = int("".join(str(int(i)) for i in parent_values), 2)
        return node.cpt[index] if values[node.name] else 1 - node.cpt[index]


# Example usage
burglary = Node("Burglary", [], [0.001, 0.999])
earthquake = Node("Earthquake", [], [0.002, 0.998])
alarm = Node(
    "Alarm",
    ["Burglary", "Earthquake"],
    [0.95, 0.05, 0.94, 0.06, 0.29, 0.71, 0.001, 0.999],
)
network = BayesianNetwork([burglary, earthquake, alarm])
print(
    network.get_probability(
        alarm, {"Burglary": True, "Earthquake": False, "Alarm": True}
    )
)

# sample Output:
# 0.94
