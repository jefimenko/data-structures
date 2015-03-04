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
              30: {'depth': 2}}
    assert tree.tree == expect
    tree.insert(40) 
    expect = {20: {'depth': 1,
                   'right': 30},
              30: {'depth': 2,
                   'right': 40},
              40: {'depth': 3}}
    assert tree.tree == expect
    tree.insert(10)
    expect = {20: {'depth': 1,
                   'left': 10,
                   'right': 30},
              30: {'depth': 2,
                   'right': 40},
              40: {'depth': 3},
              10: {'depth': 2}}
    assert tree.tree == expect


def test_size_emptree():
    t = bst.Bst()
    assert t.size() == 0


@pytest.fixture(scope='function')
def empty_tree():
    tree = bst.Bst()
    return tree
