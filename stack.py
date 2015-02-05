class Level(object):
    def __init__(self, data, under=None):
        self.data = data
        self.under = under


class Stack(object):
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, val):
        self.top = Level(val, self.top)
        self._size += 1

    def pop(self):
        if self._size == 0:
            #raise error
            pass
        result = self.top
        self.top = self.top.under
        return result
