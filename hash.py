class Hash(object):
    def __init__(self, buckets):
        self.heap = []
        for i in range(0, buckets):
            self.heap.append([])

    def set(self, key, val):
        """store the given val using the given key"""
        tup = (key, val)
        self.heap[self.hash(key)].append(tup)

    def hash(self, key):
        total = 0
        for letter in key:
            total += ord(letter)
        return total % len(self.heap)

    def get(self, key):
        """return the value stored with the given key"""
        bucket = self.heap[self.hash(key)]
        for element in bucket:
            if element[0] == key:
                return element[1]
