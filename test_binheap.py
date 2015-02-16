import pytest
from binheap import Binheap


# Create an empty heap
def test_create_empty():
    bh = Binheap()
    assert isinstance(bh, Binheap)

# Push onto a heap
def test_push():
    ebh = Binheap()
    assert isinstance(ebh, Binheap)
    # onto an empty heap
    ebh.push(5)
    assert ebh.values[0] == 5

    ebh.push(1)
    assert ebh.values[1] == 1
    ebh.push(5)
    assert ebh.values[2] == 5


    ebh.push(2)
    assert ebh.values[1] == 2
    assert ebh.values[3] == 1
    ebh.push(3)
    assert ebh.values[4] == 2
    assert ebh.values[1] == 3

    ebh.push(7)
    assert ebh.values[0] == 7
    assert ebh.values[2] == 5
    assert ebh.values[5] == 5
    ebh.push(6)
    assert ebh.values[0] == 7
    assert ebh.values[2] == 6
    assert ebh.values[5] == 5
    assert ebh.values[6] == 5


# Create a populated heap
def test_create_populated():

    with pytest.raises(TypeError):
        other = Binheap(1)

    # one item
    pbh = Binheap([1])
    assert pbh.values[0] == 1
    # two or more parents unbalanced
    abh = Binheap([1, 2, 3, 4, 5, 6])
    assert abh.values[0] == 6
    assert abh.values[1] == 4
    assert abh.values[2] == 5
    assert abh.values[3] == 1
    assert abh.values[4] == 3
    assert abh.values[5] == 2


# Pop off a heap
def test_pop():
    abh = Binheap([1, 2, 3, 4, 5, 6])

    for x in range(6, 0, -1):
        assert abh.pop() == x

    # onto an empty heap
    print abh.values
    with pytest.raises(IndexError):
        abh.pop()
