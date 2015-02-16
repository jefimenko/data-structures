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
        if not self.g.has_key(n2):
            self.add_node(n2)
        self.g[n1].append(n2)

    def del_node(self, n):
        try:
            del self.g[n]
        except KeyError:
            raise IndexError("Node doesn't exist")

    def del_edge(self, n1, n2):
        try:
            self.g[n1].remove(n2)
        except ValueError:
            pass
        except KeyError:
            raise IndexError("First node doesn't exist")

    def has_node(self, n):
        return self.g.has_key(n)

    def neighbors(self, n):
        return self.g[n]

    def adjacent(self, n1, n2):
        return n2 in self.g[n1] or n1 in self.g[n2]
