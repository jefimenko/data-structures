from dll import ListItem
from dll import DoublyLinkedList


# Test an isolated ListItem
def test_LI_cons():
    item = ListItem(5)
    assert item.data == 5
    assert item.next is None
    assert item.previous is None


# Test a ListItem linked to other ListItems
def test_LI_cnect():
    pass


def test_DLL_cons():
    pass
    # Test an empty list


# insert(val) at the start of the list
def test_DLL_ins():
    pass


# append(val) at the end of the list
def test_DLL_app():
    pass


# pop() item off the start of the list and return it's value
def test_DLL_pop():
    pass


# remove(val) an item with val from somewhere in the list
def test_DLL_rm():
    pass
