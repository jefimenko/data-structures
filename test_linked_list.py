# test constructor
from linked_list import List_Node
from linked_list import Linked_List


def test_constructor_ln():
    # Test constructing a node with no reference to another node.
    a = List_Node('asdf')
    assert a
    assert not a.next


def test_node_attributes():
    a = List_Node(5, List_Node(3))
    assert a.data == 5
    # Test value for .next attribute.
    assert a.next
    assert a.next.data == 3


def test_Linked_List_cons():
    # Verify that an empty linked list is created.
    a = Linked_List()
    assert isinstance(a, Linked_List)
    assert a.head is None


# Test insert(val) and pop()
def test_insert_pop():
    b = Linked_List()
    b.insert(5)
    assert b.head.data is 5
    b.pop()
    assert b.head is None


# size()
def test_size():
    s = Linked_List()
    assert s.size() is 0
    for something in range(100):
        s.insert(something)
    assert s.size() is 100
    s.pop()
    assert s.size() is 99
    s.insert(0)
    assert s.size() is 100
    s.remove(0)
    assert s.size is 99

# search(val)
def test_search():
    a = Linked_List()
    a.insert('a')
    a.insert(1)
    assert a.search(1).data is 1
    assert a.search('a').data is 'a'


# remove(node)
def test_remove():
    a = Linked_List()
    a.insert('val')
    assert a.head
    a.remove('val')
    assert not a.head
    for something in range(100):
        a.insert(something)
    a.remove(99)
    assert a.head.data is 98    
    a.remove(0)
    temp = a.head
    while temp.next:
        temp = temp.next
    assert temp.data is 1

# display()
def test_display():
    a = Linked_List()
    a.display()
    a.insert('a')
    a.insert(1)
    a.display()


# test __str__
def test_str():
    a = Linked_List()
    print a
    a.insert('b')
    a.insert(2)
    print a
