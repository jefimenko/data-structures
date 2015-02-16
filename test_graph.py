from graph import Graph
import pytest

def test_graph_cons():
    # Test an empty Graph
    g = Graph()
    assert g.g == {}


def test_add_node():
    g = Graph()
    g.add_node('a')
    assert g.g.has_key('a')


# Adding edges.
def test_add_to():
    g = Graph()
    g.add_node('a')
    g.add_edge('a', 'b')
    assert g.g['a'] == ['b']
    # B should have no references to other nodes.
    assert not g.g['b']


def test_add_from():
    g = Graph()
    g.add_node('b')
    g.add_edge('a', 'b')
    assert g.g['a'] == ['b']
    # B should still have no references.
    assert not g.g['b']


def test_add_out():
    g = Graph()
    g.add_edge('a', 'b')
    assert g.g['a'] == ['b']


def test_del_node():
    g = Graph()
    with pytest.raises(IndexError): 
        g.del_node('a') # empty
    g.add_node('a')
    assert g.g.has_key('a')
    g.del_node('a')
    assert not g.g.has_key('a')


def test_multi_node():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    g.del_node(1)
    assert not g.g.has_key(1)
    assert g.g.has_key(2)


def test_del_edge():
    g = Graph()
    for x in range(10):
        g.add_node(x)
    for x in range(1, 10):
        g.add_edge(0, x)

    assert g.g[0][8] == 9
    g.del_edge(0, 9)
    for x in range(1, 9):
        # Node 0 has all connections to all nodes except to 9.
        assert g.g[0][x-1] == x
    assert g.g[0][7] == 8
    # Removing an edge doesn't affect other edges.
    with pytest.raises(IndexError):
        g.g[0][8]


def test_has_node():
    g = Graph()
    assert not g.has_node(1)
    g.add_node(1)
    assert g.has_node(1)


def test_neighbors():
    g = Graph()
    with pytest.raises(IndexError):
        g.neighbors(1)
    g.add_node('asdf')
    g.add_edge('asdf', 2)
    g.add_node(3)
    assert g.neighbors('asdf') == [2]
    assert g.neighbors(2) == []
    assert g.neighbors(3) == []


def test_adjacent():
    g = Graph()
    with pytest.raises(IndexError):
        g.adjacent(1, 'not here')
    g.add_node(1)
    with pytest.raises(IndexError):
        g.adjacent(1, 'still note here')
    with pytest.raises(IndexError):
        g.adjacent('dne', 1)

def test_nodes():
    g = Graph()
    assert g.nodes() == []
    for x in range(0, 10):
        g.add_node(x)
    assert g.nodes() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_edges():
    g = Graph()
    g.add_node(9)
    for x in range(0, 5):
        g.add_edge(9, x)
    for y in g.edges():
        assert y in [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4)]
