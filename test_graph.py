from graph import Graph

def test_graph_cons():
    # Test an empty Graph
    g = Graph()
    assert g.g == {}

def test_add_node():
    g = Graph()
    g.add_node('a')
    assert g.g.has_key('a')

def test_add_edge():
    g = Graph()
    g.add_node('a')
    g.add_edge('a', 'b')
    assert g.g['a'] == ['b']
