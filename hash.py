

class Heap(object):
    def __init__(self, bins):
        self.heap = []
        for i in range(0, bins):
            self.heap.append([])

    def set(self, key, val):
        """store the given val using the given key"""
        tup = (key, val)
        self.heap[self.hash(key)].apppend(tup)

    def hash(self, key):
        sum = 0
        for letter in key:
            sum += ord(letter)
        return sum % len(self.heap)

    def get(self, key):
        """return the value stored with the given key"""
        bucket = self.heap[self.hash(key)]
        for element in bucket:
            if element[0] == key:
                return element[1]
