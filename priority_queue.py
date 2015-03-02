from queue import Queue


class Priority_Queue(object):

    def __init__(self):
        self.high = Queue()
        self.low = Queue()

    def insert(self, item, priority=None):
        """
        Insert a queue first by priority, then by first-in-last-out.

        Priority_Queue does not track the absolute order that all items
        were inserted into the queue, and only provides Priority_Queue
        behavior through pop() and insert() functions.
        Priority levels are abritrarily set to only 'high' or 'low'.
        """
        if priority == "high":
            self.high.enqueue(item)
        elif priority == "low":
            self.low.enqueue(item)
        else:
            raise ValueError("Priorty must be literal 'high' or 'low'.")

    def pop(self):
        """
        Dequeue higher priority objects first, then those of lower priority.

        If the Priority_Queue is empty, the Queue underneath will raise a
        IndexError.
        """
        if self.high.size():
            return self.high.dequeue()
        else:
            return self.low.dequeue()

    def peek(self):
        """
        Returns the value of the next item to be returned from pop().

        If the queue is empty, None is returned.
        """
        if self.high.size():
            return self.high.head.data
        elif self.low.size():
            return self.low.head.data
