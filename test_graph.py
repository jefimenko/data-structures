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
    pass

def test_has_node():
    pass

def test_neighbors():
    pass

def test_adjacent():
    pass
