from dll import ListItem
from dll import DoublyLinkedList
import pytest


# Test an isolated ListItem
def test_LI_cons():
    item = ListItem(5)
    assert item.data == 5
    assert item.next is None
    assert item.prev is None


# Test a ListItem linked to other ListItems
def test_LI_cnect():
    selected = ListItem('this one', ListItem('the next one'), ListItem('the previous one'))
    assert selected.data == 'this one'
    assert selected.next.data == 'the next one'
    assert selected.prev.data == 'the previous one'


def test_DLL_cons():
    # Test an empty list
    dbl = DoublyLinkedList()
    assert dbl
    assert dbl.head is None
    assert dbl.tail is None


# insert(val) at the start of the list
def test_DLL_ins():
    dbl = DoublyLinkedList()
    # First case with an empty list
    dbl.insert('insert')
    assert dbl.head.data == 'insert'
    assert dbl.tail.data == 'insert'
    assert dbl.head.next is None
    assert dbl.head.prev is None
    assert dbl.tail.next is None
    assert dbl.tail.next is None

    dbl.insert('next')
    assert dbl.head.data == 'next'
    # Test for updating of prev in in the second item
    assert dbl.head.next.prev.data == 'next'
    assert dbl.tail.data == 'insert'

    dbl.insert('final')
    assert dbl.head.data == 'final'
    assert dbl.head.next.prev.data == 'next'
    assert dbl.tail.data == 'insert'


# append(val) at the end of the list
def test_DLL_app():
    dbl = DoublyLinkedList()
    dbl.append('append')
    assert dbl.head.data == 'append'
    assert dbl.tail.data == 'append'
    assert dbl.head.next is None
    assert dbl.head.prev is None
    assert dbl.tail.next is None
    assert dbl.tail.prev is None

    dbl.append('next')
    assert dbl.head.data == 'append'
    assert dbl.tail.data == 'next'
    assert dbl.tail.prev.next.data == 'next'

    dbl.append('final')
    assert dbl.head.data == 'append'
    assert dbl.tail.data == 'final'
    assert dbl.tail.prev.next.data == 'final'


@pytest.fixture(scope='function')
def mk_dll(request):
    something = DoublyLinkedList()
    for a in range(2):
        for x in range(20):
            something.append(x)
    return something


# pop() item off the start of the list and return it's value
def test_DLL_pop(mk_dll):
    zeroth = DoublyLinkedList()
    with pytest.raises(IndexError):
        zeroth.pop()
    populated = mk_dll
    for x in range(20):
        assert populated.pop() == x


# shift() item off the tail
def test_DLL_pop(mk_dll):
    zeroth = DoublyLinkedList()
    with pytest.raises(IndexError):
        zeroth.shift()
    populated = mk_dll
    for x in range(19, -1, -1):
        assert populated.shift() == x


# remove(val) an item with val from somewhere in the list
def test_DLL_rm(mk_dll):
    zeroth = DoublyLinkedList()
    with pytest.raises(IndexError):
        zeroth.remove(3)
    populated = mk_dll
    # Remove from the head
    assert populated.head.data == 0
    populated.remove(0)
    assert populated.head.data == 1
    # Remove from the tail
    assert populated.tail.data == 19
    populated.remove(19)
    assert populated.tail.data == 18
    # Remove from the middle
    current = populated.head
    for a in range(5):
        current = current.next
    the_nexts_value = current.next.data
    populated.remove(the_nexts_value)
    assert not the_nexts_value == current.next.data

    # Try to remove a value that isn't there
    with pytest.raises(ValueError):
        populated.remove('not there')
