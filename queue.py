class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, val):
        self.tail = Node(val, self.tail)
        self._size += 1

    def dequeue(self):
        pass
