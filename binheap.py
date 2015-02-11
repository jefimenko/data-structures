class Binheap(object):
    def ___init___(self, vals=None):
        self.list = List(vals)

    def push(self, val):
        self.list.append(val)
        position = len(self.list) - 1
        while position != 0:
            parent_position = (position - 1) / 2
            if self.list[parent_position] < self.list[position]:
                self.list[parent_position], self.list[position] = self.list[position], self.list[parent_position]
                position = parent_position
            else:
                position = 0

    def pop(self, val):
