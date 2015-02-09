from queue import Queue
from queue import Node
import pytest

# Create an empty queue for testing.
@pytest.fixture(scope='function')
def make_empty_q():
    return Queue()


# Create a queue with entries for testing.
@pytest.fixture(scope='function')
def make_popd_q():
    q = Queue()
    for x in range(20):
        q.enqueue(x)
    q.enqueue('asdf')
    return q

def test_node_init():
    b = Node(u'a')
    assert b.data == u'a'
    c = Node(u'a', b)
    assert c.next.data == u'a'

def test_queue_init(make_empty_q):
    # Create an empty Queue.
    d = make_empty_q
    assert d
    assert d.head == None
    assert d.tail == None


def test_enqueue(make_empty_q, make_popd_q):
    q = make_empty_q
    # Test enqueue() for an empty queue.
    q.enqueue(1)
    assert q.tail.data == 1
    # Test enqueue() for a queue with something in it.
    q.enqueue(u'a')
    assert q.tail.data =='a'
    # Test enqueue() for a queue with many items in it.
    k = make_popd_q
    k.enqueue(u'hello')
    assert k.tail.data == u'hello'


def test_dequeue(make_empty_q, make_popd_q):
    # Test dequeue() for an empty queue.
    q = make_empty_q
    with pytest.raises(IndexError):
        q.dequeue()
    # Test dequeue() for a queue containing items.
    k = make_popd_q
    assert make_popd_q.dequeue() == 0


def test_size(make_empty_q, make_popd_q):
    q = make_empty_q
    # Test for size() returning 0 for an empty queue.
    assert q.size() == 0
    # Test for size() changing according to number of items in queue.
    for a in range(1, 6):
        q.enqueue(a)
        assert q.size() == a
    q.dequeue()
    assert q.size() == 4

    k = make_popd_q
    # Test for size() for a queue already containing more items.
    assert k.size() == 21
    k.dequeue()
    assert k.size() == 20
    k.enqueue(u'A')
    assert k.size() == 21
