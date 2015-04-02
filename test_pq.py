from priority_queue import Priority_Queue
import pytest


@pytest.fixture(scope='function')
def m_eq(request):
    return Priority_Queue(2)


@pytest.fixture(scope='function')
def m_lbh(request):
    q = Priority_Queue(2)
    for x in range(5):
        q.insert(x, 1)
    for x in range(-1, -6, -1):
        q.insert(x, 0)
    return q


@pytest.fixture(scope='function')
def m_hbl(request):
    q = Priority_Queue(2)
    for x in range(-1, -6, -1):
        q.insert(x, 0)
    for x in range(5):
        q.insert(x, 1)
    return q


# Test creating a Priority_Queue.
def test_eq(m_eq):
    assert isinstance(m_eq, Priority_Queue)


# Test insert()
def test_insert(m_eq, m_lbh, m_hbl):
    # Onto empty Q
    q = m_eq
    q.insert('a', 0)
    q.insert('b', 1)
    assert q.p[0].head.data == 'a'
    assert q.p[1].head.data == 'b'


# Test pop()
def test_pop(m_eq, m_lbh, m_hbl):
    # pop() an empty Priority_Queue.
    with pytest.raises(IndexError):
        m_eq.pop()
    # Low before high priority and high before low enqueued should not
    # affect the order of these when popped off
    for x in range(-1, -6, -1):
        assert m_lbh.pop() == x
        assert m_hbl.pop() == x
    for x in range(5):
        assert m_lbh.pop() == x
        assert m_hbl.pop() == x

    # Only high priority items in the list.
    q = Priority_Queue(2)
    q.insert('hey', 0)
    q.insert('last', 0)
    assert q.pop() == 'hey'
    assert q.pop() == 'last'

# Test peek()
def test_peek(m_eq, m_lbh, m_hbl):
    assert isinstance(m_eq.peek(), type(None))

    assert m_lbh.peek() == -1
    assert m_hbl.peek() == -1

    # Only low priority items in the list.
    q = Priority_Queue(2)
    q.insert('eh', 1)
    assert q.peek() == 'eh'
    q.insert('again', 1)
    assert q.peek() == 'eh'
    # Does peek look at the next to be popped, or the next chronologically
    # enqueued item?
