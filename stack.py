class Level(object):
    """
    Level class to be used by Stack class
    Create a Level to reference another Level in a Stack
    """
    def __init__(self, data, under=None):
        self.data = data
        self.under = under


class Stack(object):
    """
    Stack class using the Level class for individual node
    Create an empty Stack
    """
    def __init__(self):
        self.top = None
        self.size = 0

    """
    Push top Level down then add a Level on top
    """
    def push(self, val):
        self.top = Level(val, self.top)
        self.size += 1


    """
    Pop the top and return Level and the Level under is now the top
    Raise IndexError if there is no top Level because Stack is empty
    """
    def pop(self):
        if self.size == 0:
            raise IndexError("Can't pop empty Stack")
        result = self.top
        self.top = self.top.under
        self.size -= 1
        return result
