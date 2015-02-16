from graph import Graph


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
