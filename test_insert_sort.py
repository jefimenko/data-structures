from insert_sort import sort

def test_ordered():
    something = [x for x in range(100)]
    actual =  sort(something)
    expected = [x for x in range(100)]
    assert actual == expected


def test_reversed():
    something_else = [x for x in range(1000, 0, -1)]
    actual = sort(something_else)
    expected = [x for x in range(1, 1001)]
    assert actual == expected
