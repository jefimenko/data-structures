import pytest
from stack import Level
from stack import Stack


@pytest.fixture(scope='function')
def create_stack(request):
    # Create a populated stack for testing.
    a = Stack()
    for x in range(10):
        a.push(x)
    a.push('val')

    # Unbind a from stack for teardown practice.
    def cleanup():
        a = None

    request.addfinalizer(cleanup)

    return a


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


# Testing a case where both pop() and push() are used.
def test_pushpop(create_stack):
    b = create_stack

    # Testing pop() on a populated stack.
    assert b.pop().data == 'val'
    # Testing push() on a populated stack.
    b.push('hello')
    assert b.top.data == 'hello'
    assert b.pop().data == 'hello'
    assert b.pop().data == 9


# Verifying proper function of size attribute.
def test_verifysize(create_stack):
    c = create_stack

    alleged_size = 11
    assert c.size == alleged_size
    while c.size > 0:
        assert c.pop()
        alleged_size -= 1
        assert c.size == alleged_size

    try:
        c.pop()
    except IndexError:
        assert True

    for d in range(5):
        alleged_size += 1
        c.push(d)
        assert c.size == alleged_size
