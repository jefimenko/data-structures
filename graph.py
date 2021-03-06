class Graph(object):
    """
    Create the graph class and initialize an empty dictionary
    """
    def __init__(self):
        self.g = {}

    def nodes(self):
        """
        returns a list of nodes
        """
        return self.g.keys()

    def edges(self):
        """
        returns a list of tuples the corresponds to the edges
        """
        result = []
        for key, values in self.g.iteritems():
            for value in values:
                if value:
                    result.append((key, value[0]))
        return result

    def add_node(self, n):
        """
        Add a node to the Graph
        """
        self.g[n] = []

    def add_edge(self, n1, n2, w=0):
        """
        Add an edge between two nodes

        If any of the nodes were not created then they will be created
        """
        if not self.g.has_key(n1):
            self.add_node(n1)
        if not self.g.has_key(n2):
            self.add_node(n2)
        self.g[n1].append((n2, w))

    def del_node(self, n):
        """
        Delete an existing node from the Graph
        """
        try:
            del self.g[n]
            for node in self.g.iterkeys():
                if n in self.g[node]:
                    self.g[node].remove(n)
        except KeyError:
            raise IndexError("Node doesn't exist")

    def del_edge(self, n1, n2):
        """
        Delete an edge from the Graph. If an edge doesn't exist pass
        """
        try:
            for num in range(len(self.g[n1])):
                if self.g[n1][num][0] == n2:
                    self.g[n1].remove(self.g[n1][num])
                    break
        except ValueError:
            pass
        except KeyError:
            raise IndexError("First node doesn't exist")

    def has_node(self, n):
        """
        Return if Graph has a node
        """
        return self.g.has_key(n)

    def neighbors(self, n):
        """
        Return the edges for a node in a list
        """
        try:
            edges = [node[0] for node in self.g[n]]
            return edges
        except KeyError:
            raise IndexError("Node doesn't exist")

    def adjacent(self, n1, n2):
        """
        Return if an edge exist between two nodes
        """
        try:
            return n2 in self.neighbors(n1)
        except KeyError:
            raise IndexError("One or more nodes doesn't exist")

    def depth_first_traversal(self, node,result=""):
        if not str(node) in result:
            result = '{}{}'.format(result, node)
            if self.g[node]:
                for edge_node, weight in self.g[node]:
                    result = self.depth_first_traversal(edge_node,result)
        return result

    def breadth_first_traversal(self, node):
        """
        Iterate over a graph and return a path as a string.
        """
        children = [pair[0] for pair in self.g[node]]

        grandchildren, result = self.breadth_iterator(children, [], str(node))

        while grandchildren:
            children = grandchildren

            grandchildren, result = self.breadth_iterator(children, [], result)

        return result

    def breadth_iterator(self, children, grandchildren, result):
        """
        Traverse a graph by generations.

        Simultaneously grow a result string from list of current generations
        and create a list of the next generation.
        """
        for child in children:
            if str(child) not in result:
                result = '{}{}'.format(result, child)
                grandchildren += [pair[0] for pair in self.g[child]]

        return grandchildren, result

    def dijkstra(self, start, end):
        """
        Find a path always using smallest weight and return the path and weight
        """
        # set a temp current value to start
        current = start
        path = [start]
        path_weight = 0

        while not current == end:
            # Set weight to infinity for first case
            weight = float('inf')
            skinniest = None
            for child in self.g[current]:
                if child[1] < weight and child[0] not in path:
                    skinniest = child[0]
                    weight = child[1]
            path.append(skinniest)
            path_weight += weight
            current = skinniest

        return path, path_weight

    def find_paths(self, start, end, result=[], path=[]):
        """
        Find all paths possible with a start and an end nodes

        and return a list with possibles path inside 
        """
        if start is end:
            path.append(end)
            result.append(path[:])
            path.pop()

        elif start not in path:
            if self.g[start]:
                path.append(start)
                for edge_node, weight in self.g[start]:
                    self.find_paths(edge_node, end, result, path)
                path.pop()

        return result

    def get_path_weight(self, path):
        """
        Return the weight of a path when giving the path as a list
        """
        weight = 0
        for num in range(len(path) - 1):
            n1 = path[num]
            n2 = path[num + 1]
            for node in self.g[n1]:
                if node[0] == n2:
                    weight += node[1]
                    break
        return weight

    def find_shortest_path(self, start, end):
        """
        Return the shortest path to two nodes and the weight of the path
        """
        paths = self.find_paths(start, end, [], [])
        weight = float('inf')
        shortest_path = []
        for path in paths:
            sum = self.get_path_weight(path)
            if sum < weight:
                weight = sum
                shortest_path = path
        return shortest_path, weight
