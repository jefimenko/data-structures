from dll import ListItem
from dll import DoublyLinkedList


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
    dbl.insert('insert')
    assert dbl.head.data == 'insert'
    assert dbl.tail.data == 'insert'
    dbl.insert('next')
    assert dbl.head.data == 'next'
    assert dbl.tail.data == 'insert'
    dbl.insert('final')
    assert dbl.head.data == 'final'
    assert dbl.tail.data == 'insert'


# append(val) at the end of the list
def test_DLL_app():
    dbl = DoublyLinkedList()
    dbl.append('append')
    assert dbl.head.data == 'append'
    assert dbl.tail.data == 'append'
    dbl.append('next')
    assert dbl.head.data == 'append'
    assert dbl.tail.data == 'next'
    dbl.append('final')
    assert dbl.head.data == 'append'
    assert dbl.tail.data == 'final'


# pop() item off the start of the list and return it's value
def test_DLL_pop():
    pass


# remove(val) an item with val from somewhere in the list
def test_DLL_rm():
    pass
