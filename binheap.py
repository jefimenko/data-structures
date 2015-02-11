class Binheap(object):

    def __init__(self, values=None):
        """
        Create a Binheap that stores values in a list.

        If creating a populated Binheap, values must be an iterable.
        Binheap is a maxheap.
        """
        self.values = list()
        self.populate(values)


    def populate(self, values):
        if values:
            # For reuse in pop(), reset values to an empty list
            self.values = list()
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

    def pop(self):
        """
        Remove and return the largest value from the heap.
        """

        value = self.values[0]
        if len(self.values) == 1:
            self.values = []
        else:
            self.populate(self.values[1:])
        return value
