from hash import Hash
import pytest


def test_create():
    something = Hash(10)
    assert isinstance(something.heap, list)
    assert len(something.heap) == 10


def test_bad_create():
    with pytest.raises(TypeError):
        something = Hash()


def test_hash():
    something = Hash(10)
    hashed_val = something.hash('hello')
    assert hashed_val == 2


def test_set():
    something = Hash(10)
    something.set('asdf', 10)

    sum = 0
    for char in 'asdf':
        sum += ord(char)
    assert ('asdf', 10) in something.heap[sum % 10]


def test_get():
    something = Hash(10)
    something.set('asdf', 10)
    assert something.get('asdf') == 10