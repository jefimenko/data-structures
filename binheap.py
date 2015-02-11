class Binheap(object):

    def __init__(self, values=None):
        """
        Create a Binheap that stores values in a list.

        If creating a populated Binheap, values must be an iterable
        """
        self.values = list()
        if values:
            # When you pass a string, the string will be taken apart as a list of characters
            # to populate a heap if passed as values
            try:
                for val in values:
                    self.push(val)
            except TypeError:
                raise TypeError('Binheap constructor values must be one iterable object.')


    def push(self, val):
        self.values.append(val)
        position = len(self.values) - 1
        while position != 0:
            parent_position = (position - 1) / 2
            if self.values[parent_position] < self.values[position]:
                self.values[parent_position], self.values[position] = self.values[position], self.values[parent_position]
                position = parent_position
            else:
                position = 0

    def pop(self, val):
        pass
