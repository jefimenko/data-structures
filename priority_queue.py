from queue import Queue


class Priority_Queue(object):

    def __init__(self, size):
        self.p = [Queue() for i in xrange(size)]
        self.size = size


    def insert(self, item, priority=None):
        """
        Insert a queue first by priority, then by first-in-last-out.

        Priority_Queue does not track the absolute order that all items
        were inserted into the queue, and only provides Priority_Queue
        behavior through pop() and insert() functions.
        Priority levels are abritrarily set to only 'high' or 'low'.
        """
        try:
            self.p[priority].enqueue(item)
        except ValueError:
            return "the priority value must be in the range 0 to " + str(self.size)

    def pop(self):
        """
        Dequeue higher priority objects first, then those of lower priority.

        If the Priority_Queue is empty, the Queue underneath will raise a
        IndexError.
        """
        current = 0
        while current < self.size:
            if self.p[current].size() == 0:
                current += 1
            else:
                return self.p[current].dequeue()
        raise IndexError('The Priority_Queue is empty')


    def peek(self):
        """
        Returns the value of the next item to be returned from pop().

        If the queue is empty, None is returned.
        """
        current = 0
        while current < self.size:
            if self.p[current].size() == 0:
                current += 1
            else:
                return self.p[current].head.data
        return None
