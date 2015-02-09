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
        # For the first case with an empty queue
        if not self._size:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail = Node(val, self.tail)
        self._size += 1

    def dequeue(self):
        temp = self.head
        self.head = self.head.next
        self._size -= 1
        return temp.data

    def size(self):
        return self._size
