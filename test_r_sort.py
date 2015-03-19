from r_sort import r_sort_delta
from r_sort import r_sort


def test_r_one():
    a = [4, 3, 2, 5, 7, 1, 6]
    a = r_sort(a)
    assert a == [1, 2, 3, 4, 5, 6, 7]


def test_r_two():
    a = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    a = r_sort(a)
    assert a == [5, 5, 5, 5, 5, 5, 5, 5, 5]


def test_r_mixed():
    a = [1, 2, 5, 4, 4, 6, 7, 9, 8, 0, 0]
    a = r_sort(a)
    assert a == [0, 0, 1, 2, 4, 4, 5, 6, 7, 8, 9]


def test_r_delta():
    a = [4, 3, 2, 5, 7, 1, 6]
    a = r_sort_d(a)
    assert a == [1, 2, 3, 4, 5, 6, 7]


def test_r_delta_neg():
    a = [-1, -3, -6, -7, -8, -10, -50]
    a = r_sort_delta(a)
    assert a == [-50, -10, -8, -7, -6, -3, -1]


def test_r_delta_posneg():
    a = [1, -3, -6, 7, -8, 10, -50]
    a = r_sort_delta(a)
    assert a == [-50, -8, -6, -3, 1, 7, 10]