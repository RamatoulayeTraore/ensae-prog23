import math

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.ancestors = dict()


    def add_edge(self, node1, node2, power_min, dist=1):
        n1, n2 = False, False
        if node1 not in self.nodes:
            n1 = True
            self.nodes.append(node1)
            self.nb_nodes += 1
            self.graph[node1] = [(node2, power_min, dist)]
        if node2 not in self.nodes:
            n2 = True
            self.nodes.append(node2)
            self.nb_nodes += 1
            self.graph[node2] = [(node1, power_min, dist)]

        if not n1:
            self.graph[node1].append((node2, power_min, dist))
        if not n2:
            self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1

    def preprocess(self):
        self.ancestors = {node: [(node, 0)] for node in self.nodes}

        max_distance = int(math.log(self.nb_nodes, 2)) + 1

        for i in range(1, max_distance):
            for node in self.nodes:
                if len(self.ancestors[node]) >= i:
                    ancestor = self.ancestors[node][i - 1][0]
                    max_power = max(self.ancestors[node][i - 1][1], self.ancestors[ancestor][i - 1][1])
                    self.ancestors[node].append((self.ancestors[ancestor][i - 1][0], max_power))

    def min_power(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            return None

        if start == end:
            return 0

        max_distance = int(math.log(self.nb_nodes, 2)) + 1

        path = [start, end]
        path_ancestors = []

        for i in range(max_distance, -1, -1):
            ancestor = self.ancestors[path[-1]][i][0]

            if ancestor == start:
                path_ancestors.append(self.ancestors[path[-1]][i])
                break

            if ancestor == path[-2]:
                path.append(self.ancestors[path[-1]][i][0])
                path_ancestors.append(self.ancestors[path[-2]][i])
            else:
                path.append(ancestor)
                path_ancestors.append(self.ancestors[path[-2]][i])
                path_ancestors.append(self.ancestors[path[-1]][i])

        min_power = float('inf')

        for i in range(len(path_ancestors) - 1, -1, -1):
            power = path_ancestors[i][1]

            if power < min_power:
                min_power = power

        return min_power
