from merge_sort import merge_sort
import random

def test_ordered():
    something = [x for x in range(100)]
    actual =  merge_sort(something)
    expected = [x for x in range(100)]
    assert actual == expected


def test_reversed():
    something_else = [x for x in range(1000, 0, -1)]
    actual = merge_sort(something_else)
    expected = [x for x in range(1, 1001)]
    assert actual == expected

def test_random():
    something_else = [x for x in range(1000)]
    random.shuffle(something_else)
    actual = merge_sort(something_else)
    expected = [x for x in range(0, 1000)]
    assert actual == expected