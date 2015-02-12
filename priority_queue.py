from queue import Queue


class Priority_Queue(object):

    def __init__(self):
        self.high = Queue()
        self.low = Queue()

    def insert(item, priority="high"):
        if priority == "high":
            self.high.enqueue(item)
        elif priority == "low":
            self.low.enqueue(item)
        else:
            raise ValueError("Priorty must be literal 'high' or 'low'.")

    def pop():
        """
        Dequeue higher priority objects first, then those of lower priority.

        If the Priority_Queue is empty, the Queue underneath will raise a
        IndexError.
        """
        if self.high.size():
            return self.high.dequeue()
        else:
            return self.low.dequeue()

    def peek():
        if self.high.size():
            return self.high.head.data
        else:
            return self.low.head.data
