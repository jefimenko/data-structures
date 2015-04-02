class Hash(object):
    def __init__(self, buckets):
        self.h_list = []
        for i in range(0, buckets):
            self.h_list.append([])

    def set(self, key, val):
        """Store the given val using the given key.

        Replaces the value if setting with a key already in.
        """
        tup = (key, val)
        bucket = self.h_list[self.hash(key)]
        for item in bucket:
            if item[0] == key:
                bucket.remove(item)
                break
        bucket.append(tup)

    def hash(self, key):
        if not isinstance(key, (str, unicode)):
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
