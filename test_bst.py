import bst
import pytest


def test_Bst():
    """Constructing a bst tree"""
    tree = bst.Bst()
    assert tree.tree == {}
    tree = bst.Bst(5)
    assert tree.tree == {5: {'depth': 1}}


def test_insert(empty_tree):
    """Test insert into a tree"""
    tree = empty_tree
    tree.insert(20)
    assert tree.tree == {20: {'depth': 1}}
    tree.insert(30)
    expect = {20: {'depth': 1,
                   'right': 30},
              30: {'depth': 2,
                   'parent': 20}}
    assert tree.tree == expect
    tree.insert(40) 
    expect = {20: {'depth': 1,
                   'right': 30},
              30: {'depth': 2,
                   'right': 40,
                   'parent': 20},
              40: {'depth': 3,
                   'parent': 30}}
    assert tree.tree == expect
    tree.insert(10)
    expect = {20: {'depth': 1,
                   'left': 10,
                   'right': 30},
              30: {'depth': 2,
                   'right': 40,
                   'parent': 20},
              40: {'depth': 3,
                   'parent': 30},
              10: {'depth': 2,
                   'parent': 20}}
    assert tree.tree == expect


def test_size_emptree(empty_tree):
    t = empty_tree
    assert t.size() == 0


def test_size_tree(filled_tree):
    t = filled_tree
    assert t.size() == 14


def test_depth_emptree(empty_tree):
    t = empty_tree
    assert t.depth() == 0


def test_depth_tree(filled_tree):
    t = filled_tree
    assert t.depth() == 10


def test_balance(empty_tree, filled_tree):
    t = empty_tree
    assert t.balance() == 0
    t.insert(3)
    assert t.balance() == 0
    t = filled_tree
    assert t.balance() == -5


def test_contains(filled_tree):
    t = filled_tree
    for num in reversed(range(10)):
        assert t.contains(num) is True
    for num in range(10, 14):
        assert t.contains(num) is True
    for num in range(20, 25):
        assert t.contains(num) is False


def test_in_order(filled_tree):
    tree = filled_tree
    gen = tree.in_order()
    expected_order = range(0, 14)
    for i in expected_order:
        j = gen.next()
        print str(i) + '=' + str(j)
        assert i == j
    with pytest.raises(StopIteration):
        gen.next()


def test_pre_order(filled_tree):
    tree = filled_tree
    gen = tree.pre_order()
    expected_order = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 11, 12, 13]
    for i in expected_order:
        j = gen.next()
        print str(i) + '=' + str(j)
        assert i == j
    with pytest.raises(StopIteration):
        gen.next()

def test_post_order(filled_tree):
    tree = filled_tree
    gen = tree.post_order()
    expected_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 13, 12, 11, 10, 9]
    for i in expected_order:
        j = gen.next()
        print str(i) + '=' + str(j)
        assert i == j
    with pytest.raises(StopIteration):
        gen.next()


def test_breadth_first_order(filled_tree):
    tree = filled_tree
    expected_order = [9, 8, 10, 7, 11, 6, 12, 5, 13, 4, 3, 2, 1, 0]
    for place, item in enumerate(tree.breadth_first()):
        assert expected_order[place] == item


def test_deletion_easy_case(filled_tree_2):
    tree = filled_tree_2
    assert tree.left(6) == 5
    tree.delete(5)
    assert tree.left(6) is None


@pytest.fixture(scope='function')
def filled_tree():
    """Upside down V Shaped Tree"""
    tree = bst.Bst()
    for num in reversed(range(10)):
        tree.insert(num)
    for num in range(10, 14):
        tree.insert(num)
    return tree


@pytest.fixture(scope='function')
def filled_tree_2():
    """Tree with lots of branches"""
    inserts = [7, 4, 11, 2, 9, 6, 12, 5, 13, 0, 10, 8, 3, 1]
    tree = bst.Bst()
    for val in inserts:
        tree.insert(val)
    return tree


@pytest.fixture(scope='function')
def empty_tree():
    tree = bst.Bst()
    return tree
