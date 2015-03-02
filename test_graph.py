from graph import Graph
import pytest

# Test Graph constructor
def test_graph_cons():
    # Test an empty Graph
    g = Graph()
    assert g.g == {}

# Test adding a node
def test_add_node():
    g = Graph()
    g.add_node('a')
    assert g.g.has_key('a')


# Test adding edges and if 2nd node is missing.
def test_add_to():
    g = Graph()
    g.add_node('a')
    g.add_edge('a', 'b')
    assert g.g['a'][0][0] == 'b'
    # B should have no references to other nodes.
    assert not g.g['b']

# Test adding edges and if 1st node is missing.
def test_add_from():
    g = Graph()
    g.add_node('b')
    g.add_edge('a', 'b')
    assert g.g['a'][0][0] == 'b'
    # B should still have no references.
    assert not g.g['b']

# Test adding edges and if both nodes is missing.
def test_add_out():
    g = Graph()
    g.add_edge('a', 'b')
    assert g.g['a'][0][0] == 'b'

# Test deleting a node
def test_del_node():
    g = Graph()
    with pytest.raises(IndexError): 
        g.del_node('a') # empty
    g.add_node('a')
    assert g.g.has_key('a')
    g.del_node('a')
    assert not g.g.has_key('a')

# Test deleting a node with an edge
def test_multi_node():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.del_node(1)
    assert not g.g.has_key(1)
    assert g.g.has_key(2)

# Test deleting an edge
def test_del_edge():
    g = Graph()
    for x in range(10):
        g.add_node(x)
    for x in range(1, 10):
        g.add_edge(0, x)

    assert g.g[0][8][0] == 9
    g.del_edge(0, 9)
    for x in range(1, 9):
        # Node 0 has all connections to all nodes except to 9.
        assert g.g[0][x-1][0] == x
    assert g.g[0][7][0] == 8
    # Removing an edge doesn't affect other edges.
    with pytest.raises(IndexError):
        g.g[0][8]

# Test if a Graph has a node
def test_has_node():
    g = Graph()
    assert not g.has_node(1)
    g.add_node(1)
    assert g.has_node(1)

# Test if edges are returns for a node
def test_neighbors():
    g = Graph()
    with pytest.raises(IndexError):
        g.neighbors(1) # Empty Graph
    g.add_node('asdf')
    g.add_edge('asdf', 2)
    g.add_node(3)
    assert g.neighbors('asdf') == [2] # Empty
    assert g.neighbors(2) == []
    assert g.neighbors(3) == []

# Test if if an edge exist between two nodes
def test_adjacent():
    g = Graph()
    with pytest.raises(IndexError):
        g.adjacent(1, 'not here')
    g.add_node(1)
    assert g.adjacent(1, 'still note here') is False
    with pytest.raises(IndexError):
        g.adjacent('dne', 1)

# Test if nodes() returns a list of nodes
def test_nodes():
    g = Graph()
    assert g.nodes() == []
    for x in range(0, 10):
        g.add_node(x)
    assert g.nodes() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Test if edges() return a list of tuples of edges
def test_edges():
    g = Graph()
    g.add_node(9)
    for x in range(0, 5):
        g.add_edge(9, x)
    for y in g.edges():
        assert y in [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4)]

# def test_traverse():
#     g = Graph()
#     g.add_node(1)
#     g.add_edge(1, 2)
#     g.add_edge(2, 4)
#     g.add_edge(1, 3)
#     print g.traverse(1)
#     assert g.traverse is '1234'


# def test_breadth(popd_graph):
#     g = popd_graph
#     assert g.breadth_first_traversal(1) == '1234756910'


# def test_breadth(popd_graph):
#     g = popd_graph
#     assert g.depth_first_traversal(1) == '1245610937'


# def test_bfloop(popd_graph):
#     g = popd_graph
#     g.add_edge(10, 7)
#     g.add_edge(9, 2)
#     g.add_edge(9, 3)
#     assert g.breadth_first_traversal(1) == '1234756910'


# def test_depthfloop(popd_graph):
#     g = popd_graph
#     g.add_edge(10, 7)
#     g.add_edge(9, 2)
#     g.add_edge(9, 3)
#     assert g.depth_first_traversal(1) == '1245610793'


@pytest.fixture(scope='function')
def popd_graph(request):
    g = Graph()
    g.add_node(1)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(1, 3)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(4, 9)
    g.add_edge(6, 10)
    g.add_edge(3, 7)
    g.add_edge(8, 6)

    return g
