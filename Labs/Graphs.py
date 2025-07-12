class Graph:
    def __init__(self, directed=False):
        self.directed = directed

        self.adj_list= dict()

    def __repr__(self):
        str_graph = ""

        for key, value in self.adj_list.items():
            str_graph += f"{key} -> {value} "
            return str_graph

    def bfs(self):
        pass

    def dfs(self):
        pass

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists!!")

    def add_edge(self, source_node, destination_node, weighted = 1):
        if source_node not in self.adj_list:
            self.add_node(source_node)
        if destination_node not in self.adj_list:
            self.add_node(destination_node)

        if weighted is None:
            self.adj_list[source_node].add(destination_node)

            if self.directed:
                self.adj_list[destination_node].add(source_node)
        else:
            self.adj_list[source_node].add((destination_node, weighted))
            if self.directed:
                self.adj_list[destination_node].add((source_node, weighted))

    def obtain_neighbors(self, key_node):
        return self.adj_list.get(key_node, set())

    def  adj_matrix(self):
        pass

if __name__ == '__main__':
    graph_obj = Graph()

    print(graph_obj)

