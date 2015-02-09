class Node(object):
    """
    Node class to be used by Queue class
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue(object):
    """
    Queue class that makes an empty queue
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def enqueue(self, val):
        """
        Add a value at the back/tail of queue
        """
        # For the first case with an empty queue
        if not self._size:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail = Node(val, self.tail)
        self._size += 1

    def dequeue(self):
        """
        Return a value that is at the front/head of the queue
        """
        if not self._size:
            raise IndexError('Cannot dequeue an item from an empty Queue.')
        temp = self.head
        self.head = self.head.next
        self._size -= 1
        return temp.data

    def size(self):
        """
        Return the size of the queue
        """
        return self._size
