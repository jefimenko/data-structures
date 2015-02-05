import pytest
from stack import Level
from stack import Stack


@pytext.fixture(scope='function')
def create_stack(request):
    a = Stack()
    for x in range(10):
        a.push(val)
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
