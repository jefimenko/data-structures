from queue import Queue


class Priority_Queue(object):

    def __init__(self):
        self.high = Queue()
        self.low = Queue()

    def insert(self, item, priority="high"):
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
        if self.high.size():
            return self.high.head.data
        elif self.low.size():
            return self.low.head.data
