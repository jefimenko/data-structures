import bst
import pytest


def test_Bst():
    """Constructing a bst tree"""
    tree = bst.Bst()
    assert tree.tree == {}
    tree = bst.Bst(5)
    assert tree.tree == {5: {}}


def test_insert(empty_tree):
    """Test insert into a tree"""
    tree = empty_tree
    tree.insert(20)
    assert tree.tree == {20: {}}
    tree.insert(30)
    expect = {20: {'right': 30},
              30: {'parent': 20}}
    assert tree.tree == expect
    tree.insert(40)
    expect = {20: {'right': 30},
              30: {'right': 40,
                   'parent': 20},
              40: {'parent': 30}}
    assert tree.tree == expect
    tree.insert(10)
    expect = {20: {'left': 10,
                   'right': 30},
              30: {'right': 40,
                   'parent': 20},
              40: {'parent': 30},
              10: {'parent': 20}}
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


def test_balance_subtree(empty_tree, filled_tree_2):
    t = filled_tree_2
    # list of subtrees and expected balances
    expected = [(1, 0), (2, -1), (3, 0), (4, -1), (5, 0), (6, -1),
                (7, -1), (8, 0), (9, 0), (10, 0), (11, 0), (12, 1),
                (13, 0)]
    for i, j in expected:
        assert t.balance(i) == j


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


def test_swap(filled_tree_2):
    tree = filled_tree_2
    tree._swap_nodes(7, 5)
    assert tree.top == 5

    assert tree.parent(5) is None
    assert tree.left(5) == 4
    assert tree.right(5) == 11

    assert tree.parent(7) == 6
    assert tree.left(7) is None
    assert tree.right(7) is None


def test_swap_parentchild(filled_tree_2):
    tree = filled_tree_2
    tree._swap_nodes(7, 4)
    assert tree.top == 4

    assert tree.parent(4) is None
    assert tree.left(4) == 7
    assert tree.right(4) == 11

    assert tree.parent(7) == 4
    assert tree.left(7) is 2
    assert tree.right(7) is 6


def test_deletion_easy_case(filled_tree_2):
    """Delete retainging balance"""
    tree = filled_tree_2
    assert tree.right(0) == 1
    tree.delete(1)
    assert tree.right(0) is None
    assert tree.contains(1) is False


def test_deletion_two_childrens(filled_tree_2):
    tree = filled_tree_2
    assert tree.parent(9) == 11
    assert tree.left(9) == 8
    assert tree.right(9) == 10
    tree.delete(9)
    assert tree.left(11) == 8
    assert tree.right(11) == 12

    assert tree.parent(8) == 11
    assert tree.left(8) is None
    assert tree.right(8) == 10
    assert tree.parent(10) == 8

    assert tree.contains(9) is False


def test_deletion_one_right_child_lesser(filled_tree_2):
    tree = filled_tree_2
    assert tree.parent(0) == 2
    assert tree.left(0) is None
    assert tree.right(0) == 1
    tree.delete(0)

    assert tree.left(2) == 1
    assert tree.right(2) == 3

    assert tree.parent(1) == 2
    assert tree.left(1) is None
    assert tree.right(1) is None

    assert tree.contains(0) is False


def test_node_depth(filled_tree_2):
    expected = [(1, 5), (4, 2), (7, 1), (13, 4)]
    for i, j in expected:
        assert filled_tree_2.node_depth(i) == j



def test_rightmost(filled_tree_2):
    expected = [(0, 1), (4, 6), (6, 6), (7, 13)]
    for i, j in expected:
        assert filled_tree_2._rightmost(i) == j


def test_r_rotate_moves_right_child_of_left_to_left_child_of_right(l_tree):
    """Test r rotation on a tree with 3 nodes on l and 1 on right"""
    tree = l_tree
    tree._r_rotate(4)

    # generate inorder list from tree.
    gen = tree.in_order()
    node_list = []
    try:
        for i in gen:
            node_list.append(i)
    except(StopIteration):
        pass
    # see if it's in the right order
    expected = [1, 2, 3, 4, 5]
    for i, j in enumerate(expected):
        assert j == node_list[i]
    assert tree.top == 2


def test_r_rotate():
    tree = bst.Bst()
    tree.insert(2)
    tree.insert(1)
    assert tree.top == 2
    tree._r_rotate(2)

    # Verify correct rotation
    assert tree.right(1) == 2
    assert tree.left(1) is None
    assert tree.parent(1) is None

    assert tree.right(2) is None
    assert tree.left(2) is None
    assert tree.parent(2) == 1

    assert tree.top == 1


def test_r_rotate_on_ll_tree():
    tree = bst.Bst()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    assert tree.top == 3
    tree._r_rotate(3)

    # Verify correct rotation
    assert tree.right(1) is None
    assert tree.left(1) is None
    assert tree.parent(1) == 2

    assert tree.right(2) == 3
    assert tree.left(2) == 1
    assert tree.parent(2) is None

    assert tree.right(3) is None
    assert tree.left(3) is None
    assert tree.parent(3) == 2

    assert tree.top == 2


def test_l_rotate():
    tree = bst.Bst()
    tree.insert(1)
    tree.insert(2)
    assert tree.top == 1
    tree._l_rotate(1)

    # Verify correct rotation
    assert tree.right(1) is None
    assert tree.left(1) is None
    assert tree.parent(1) == 2

    assert tree.right(2) is None
    assert tree.left(2) == 1
    assert tree.parent(2) is None

    assert tree.top == 2

def test_l_rotate_on_rr_tree():
    tree = bst.Bst()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    assert tree.top == 1
    tree._l_rotate(1)

    # Verify correct rotation
    assert tree.right(1) is None
    assert tree.left(1) is None
    assert tree.parent(1) == 2

    assert tree.right(2) == 3
    assert tree.left(2) == 1
    assert tree.parent(2) is None

    assert tree.right(3) is None
    assert tree.left(3) is None
    assert tree.parent(3) is 2

    assert tree.top == 2


def test_b_insert_rr(filled_tree_2):
    """tests inserting into at a rr place"""
    tree = filled_tree_2
    tree.b_insert(1.5)

    # make sure 0, 1, 1.5 pointers are ok.
    assert tree.parent(1.5) == 1
    assert tree.right(1.5) is None
    assert tree.left(1.5) is None

    assert tree.parent(1) == 2
    assert tree.right(1) == 1.5
    assert tree.left(1) == 0

    assert tree.parent(0) == 1
    assert tree.right(0) is None
    assert tree.left(0) is None


def test_b_insert_rl(filled_tree_2):
    """tests inserting into at a rl place"""
    tree = filled_tree_2
    tree.b_insert(12.5)

    # make sure 12, 12.5, 13 pointers are ok.
    assert tree.parent(12.5) == 11
    assert tree.right(12.5) is 13
    assert tree.left(12.5) is 12

    assert tree.parent(12) == 12.5
    assert tree.right(12) is None
    assert tree.left(12) is None

    assert tree.parent(13) == 12.5
    assert tree.right(13) is None
    assert tree.left(13) is None


def test_b_insert_ll(filled_tree_2):
    """tests inserting into at a ll place"""
    tree = filled_tree_2
    tree.b_insert(4.5)

    # make sure 4.5, 5, 6 pointers are ok.
    assert tree.parent(5) == 4
    assert tree.right(5) == 4.5
    assert tree.left(5) == 6

    assert tree.parent(4.5) == 5
    assert tree.right(4.5) is None
    assert tree.left(4.5) is None

    assert tree.parent(6) == 5
    assert tree.right(6) is None
    assert tree.left(6) is None


def test_b_insert_lr(filled_tree_2):
    """tests inserting into at a lr place"""
    tree = filled_tree_2
    tree.b_insert(5.5)

    # make sure 5, 5.5, 6 pointers are ok.
    assert tree.parent(5.5) == 4
    assert tree.right(5.5) == 5
    assert tree.left(5.5) == 6

    assert tree.parent(4) == 5.5
    assert tree.right(4) is None
    assert tree.left(4) is None

    assert tree.parent(6) == 5.5
    assert tree.right(6) is None
    assert tree.left(6) is None


def test_delete_lr(filled_tree_2):
    tree = filled_tree_2
    tree.delete(3)

    # make sure 5, 5.5, 6 pointers are ok.
    assert tree.parent(1) == 4
    assert tree.right(1) == 2
    assert tree.left(1) == 0

    assert tree.parent(0) == 1
    assert tree.right(0) is None
    assert tree.left(0) is None

    assert tree.parent(2) == 1
    assert tree.right(2) is None
    assert tree.left(2) is None  


def test_delete_ll(filled_tree_2):
    tree = filled_tree_2
    tree.insert(-1)
    tree.delete(1)

    # delete the node that unbalances the tree
    tree.delete(3)

    # make sure -1, 0, 2 pointers are ok.
    assert tree.parent(0) == 4
    assert tree.right(0) == 2
    assert tree.left(0) == -1

    assert tree.parent(-1) == 0
    assert tree.right(-1) is None
    assert tree.left(-1) is None

    assert tree.parent(2) == 0
    assert tree.right(2) is None
    assert tree.left(2) is None

@pytest.fixture(scope='function')
def l_tree():
    """ Tree with 3 nodes (same depth) on the left and one on the right"""
    tree = bst.Bst()
    for i in [4, 5, 2, 1, 3]:
        tree.insert(i)
    return tree


def test_llr_rightright_top():
    tree = bst.Bst()


def test_llr_rightright():
    tree = bst.Bst()


def test_llr_rightleft_top():
    tree = bst.Bst()


def test_llr_rightleft():
    tree = bst.Bst()


def test_rrl_leftleft_top():
    tree = bst.Bst()


def test_rrl_leftleft():
    tree = bst.Bst()


def test_rrl_leftright_top():
    tree = bst.Bst()


def test_rrl_leftright():
    tree = bst.Bst()


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
