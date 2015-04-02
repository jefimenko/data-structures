from q_sort import get_pivot, q_sort


def test_get_pivot_f():
    a = [2, 1, 3]
    assert get_pivot(a) == [2]
    b = [2, 3, 1]
    assert get_pivot(b) == [2]


def test_get_pivot_l():
    a = [1, 3, 2]
    assert get_pivot(a) == [2]
    b = [3, 1, 2]
    assert get_pivot(b) == [2]


def test_get_pivot_m():
    a = [1, 5, 5, 2, 1, 1, 3]
    assert get_pivot(a) == [2]
    b = [3, 2, 1]
    assert get_pivot(b) == [2]


def test_q_one():
    a = [4, 3, 2, 5, 7, 1, 6]
    a = q_sort(a)
    assert a == sorted(a)


def test_q_two():
    a = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    a = q_sort(a)
    assert a == sorted(a)


def test_q_mixed():
    a = [1, 2, 5, 4, 4, 6, 7, 9, 8, 0, 0]
    a = q_sort(a)
    assert a == sorted(a)


def test_q_mixed():
    a = [1, 2, 5, 10, 10]
    a = q_sort(a)
    assert a == sorted(a)
