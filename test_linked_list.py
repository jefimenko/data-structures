# test constructor
from linked_list import list_node
from linked_list import linked_list


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


def test_linked_list_cons():
    # Verify that an empty linked list is created.
    a = linked_list()
    assert isinstance(a, linked_list)
    assert a.head is None

# Test creating a populated linked list.


# Test insert(val) and pop()
def test_insert_pop():
    b = linked_list()
    b.insert(5)
    assert b.head.data is 5
    b.pop()
    assert b.head is None


# size()
def test_size():
    s = linked_list()
    assert s.size() is 0
    for something in range(100):
        s.insert(something)
    assert s.size() is 100


# search(val)
def test_search():
    a = linked_list()
    a.insert('a')
    a.insert(1)
    assert a.search(1) is 1
    assert a.search('a') is 'a'


# remove(node)
def test_remove():
    pass


# print()
def test_print():
    pass


# test __str__
def test_str():
    pass
