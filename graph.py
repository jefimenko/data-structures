class Graph(object):
    def __init__(self):
        self.g = {}

    def nodes(self):
        pass

    def edges(self):
        pass

    def add_node(self, n):
        self.g[n] = []

    def add_edge(self, n1, n2):
        if not self.g.has_key(n1):
            self.add_node(n1)
        elif not self.g.has_key(n2):
            self.add_node(n2)
        self.g[n1].append(n2)


    def del_node(self, n):
        pass

    def del_edge(self, n1, n2):
        pass

    def has_node(self, n):
        pass

    def neighbors(self, n):
        pass

    def adjacent(self, n1, n2):
        pass
