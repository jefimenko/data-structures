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
                    result.append((key, value))
        return result

    def add_node(self, n):
        """
        Add a node to the Graph
        """
        self.g[n] = []

    def add_edge(self, n1, n2):
        """
        Add an edge between two nodes

        If any of the nodes were not created then they will be created
        """
        if not self.g.has_key(n1):
            self.add_node(n1)
        if not self.g.has_key(n2):
            self.add_node(n2)
        self.g[n1].append(n2)

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
            self.g[n1].remove(n2)
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
            return self.g[n]
        except KeyError:
            raise IndexError("Node doesn't exist")

    def adjacent(self, n1, n2):
        """
        Return if an edge exist between two nodes
        """
        try:
            return n2 in self.g[n1]
        except KeyError:
            raise IndexError("One or more nodes doesn't exist")

    # def traverse(self, node, result=""):
    #     result = '{}{}'.format(result, node)
    #     if self.g[node]:
    #         for edge_node in self.g[node]:
    #             result = self.traverse(edge_node,result)
    #     return result
    #     # if len(self.g[node]) != 0:
    #     #     for edge_node in self.g[node]:
    #     #         result = '{}{}'.format(node, self.traverse(edge_node, result))
    #     # return '{}{}'.format(node, result)

    # def depth_first_traversal_helper(self, node, result):
    #     if self.g[node]:
    #         for edge_node in self.g[node]:
    #             # import pdb; pdb.set_trace()
    #             result = '{}{}'.format(result, edge_node)
    #             result = self.depth_first_traversal_helper(edge_node, result)
    #     return result

    def depth_first_traversal(self, node,result=""):
        if not str(node) in result:
            result = '{}{}'.format(result, node)
            if self.g[node]:
                for edge_node in self.g[node]:
                    result = self.depth_first_traversal(edge_node,result)
        return result

    def breadth_first_traversal_helper(self, children , result):
        for child in children:
            for grandchild in self.g[child]:
                result = '{}{}'.format(result, grandchild)

        return grandchildren, result

    def breadth_first_traversal(self, node):
        """
        Iterate over a graph and return a path as a string.
        """
        children = self.g[node]

        grandchildren, result = self.breadth_iterator(children, [], node)

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
            result = '{}{}'.format(result, child)
            grandchildren += self.g[child]

        return grandchildren, result
