class Hash(object):
    def __init__(self, buckets):
        self.h_list = []
        for i in range(0, buckets):
            self.h_list.append([])

    def set(self, key, val):
        """store the given val using the given key"""
        tup = (key, val)
        self.h_list[self.hash(key)].append(tup)

    def hash(self, key):
        if not isinstance(key, str):
            type_ = type(key)
            raise TypeError('Cannot hash something of type {}'.format(type_))
        total = 0
        for letter in key:
            total += ord(letter)
        return total % len(self.h_list)

    def get(self, key):
        """return the value stored with the given key"""
        bucket = self.h_list[self.hash(key)]
        for element in bucket:
            if element[0] == key:
                return element[1]
