import pytest
from stack import Level
from stack import Stack


@pytest.fixture(scope='function')
def create_stack(request):
    a = Stack()
    for x in range(10):
        a.push(x)
    a.push('val')

    # Unbind a from stack for teardown.
    def cleanup(a):
        a = None
    request.addfinalizer(cleanup)

    # return a


# Tests for Levels object
def test_level_cons():
    # For no data passed into Level(), this should fail
    try:
        a = Level()
    except TypeError:
        assert True
    b = Level(1)
    assert b.data == 1
    c = Level('asdf')
    assert c.data == 'asdf'


def test_stack_cons():
    s = Stack()
    assert s.top is None
    assert s.size is 0

def test_push():
    a = Stack()
    a.push(1)
    assert a.top.data is 1
    a.push(2)
    assert a.top.data is 2

def test_pop():
    a = Stack()
    
    try:
        a.pop()
    except IndexError:
        assert True
