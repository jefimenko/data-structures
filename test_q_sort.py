from q_sort import get_pivot, q_sort


def test_get_pivot_f():
    a = [2, 1, 3]
    assert get_pivot(a) == 2
    b = [2, 3, 1]
    assert get_pivot(b) == 2


def test_get_pivot_l():
    a = [1, 3, 2]
    assert get_pivot(a) == 2
    b = [3, 1, 2]
    assert get_pivot(b) == 2


def test_get_pivot_m():
    a = [1, 5, 5, 2, 1, 1, 3]
    assert get_pivot(a) == 2
    b = [3, 2, 1]
    assert get_pivot(b) == 2


def test_q_one():
    a = [4, 3, 2, 5, 7, 1, 6]
    a = q_sort(a)
    assert a == [1, 2, 3, 4, 5, 6, 7]
