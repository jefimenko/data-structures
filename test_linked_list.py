# test constructor
from linked_list import list_node


def test_constructor_ln():
    # Test constructing a node with no reference to another node.
    a = list_node('asdf')
    assert a
    assert not list_node.next


def test_node_attributes():
    a = list_node(5, list_node(3))
    assert a.data == 5
    # Test value for .next attribute.
    assert a.next
    assert a.next.data == 3

# insert(val)

# pop()

# size()

# search(val)

# remove(node)

# print()
