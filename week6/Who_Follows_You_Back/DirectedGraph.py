class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def create_node(self, node):
        self.graph[node] = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph:
            self.create_node(node_a)
        if node_b not in self.graph:
            self.create_node(node_b)
        if node_b not in self.graph[node_a]:
            self.graph[node_a].append(node_b)

    def get_neighbours_for(self, node):
        return self.graph[node]

    def path_between(self, node_a, node_b):
        if node_b in self.graph[node_a]:
            return True
        for node in self.graph[node_a]:
            return self.path_between(node, node_b)
        return False

    def print_graph(self):
        for key, value in self.graph.items():
            print(key, ":", value)