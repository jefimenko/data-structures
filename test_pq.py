from priority_queue import Priority_Queue
import pytest


@pytest.fixture(scope='function')
def m_eq(request):
    return Priority_Queue()


@pytest.fixture(scope='function')
def m_lbh(request):
    q = Priority_Queue()
    for x in range(5):
        q.insert(x, 'low')
    for x in range(-1, -6, -1):
        q.insert(x, 'high')
    return q


@pytest.fixture(scope='function')
def m_hbl(request):
    q = Priority_Queue()
    for x in range(-1, -6, -1):
        q.insert(x, 'high')
    for x in range(5):
        q.insert(x, 'low')
    return q


# Test creating a Priority_Queue.
def test_eq(m_eq):
    assert isinstance(m_eq, Priority_Queue)
    # Test that Priority_Queue is empty.
    assert m_eq.high.size() == 0
    assert m_eq.low.size() == 0


# Test insert()
def test_insert(m_eq, m_lbh, m_hbl):
    # Onto empty Q
    q = m_eq
    q.insert('a', 'high')
    q.insert('b', 'low')
    assert q.high.head.data == 'a'
    assert q.low.head.data == 'b'


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
    q = Priority_Queue()
    q.insert('hey', 'high')
    q.insert('last', 'high')
    assert q.pop() == 'hey'
    assert q.pop() == 'last'

# Test peek()
def test_peek(m_eq, m_lbh, m_hbl):
    assert isinstance(m_eq.peek(), type(None))

    assert m_lbh.peek() == -1
    assert m_hbl.peek() == -1

    # Only low priority items in the list.
    q = Priority_Queue()
    q.insert('eh', 'low')
    assert q.peek() == 'eh'
    q.insert('again', 'low')
    assert q.peek() == 'eh'
    # Does peek look at the next to be popped, or the next chronologically
    # enqueued item?
