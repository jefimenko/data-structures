from priority_queue import Priority_Queue
import pytest


@pytest.fixture(scope='function')
def m_eq(request):
    return Priority_Queue


@pytest.fixture(scope='function')
def m_lbh(request):
    q = Priority_Queue()
    for x in range(5):
        q.insert(x, 'low')
    for x in range(-1, -6, -1):
        q.insert(x, 'high')


@pytest.fixture(scope='function')
def m_hbl(request):
    q = Priority_Queue()
    for x in range(-1, -6, -1):
        q.insert(x, 'high')
    for x in range(5):
        q.insert(x, 'low')


# Test creating a Priority_Queue.
def test_eq(m_eq):
    assert isinstance(m_eq, Priority_Queue)
    # Test that Priority_Queue is empty.
    assert m_eq.high.size() == 0
    assert m_eq.low.size() == 0


# Test insert()
def test_insert(m_eq, m_lbh, m_hbl):
    pass
    # Onto empty Q
        # Low
        # High
    # Onto non-empty Q
        # Low
        # High


# Test pop()
def test_pop(m_eq, m_lbh, m_hbl):
    pass
    # Empty Q
    # Low before high
    # High before low


# Test peek()
def test_peek(m_eq, m_lbh, m_hbl):
    pass
    # Empty Q
    # Low before high
    # High before low
        # Does peek look at the next to be popped, or the next chronologically enqueued item?
