class Bst(object):
    """Binary Search Tree"""
    def __init__(self, value=None):
        self.tree = {}
        self.top = None
        self._size = 0

        if not value is None:
            self.tree[value] = {'depth': 1}
            self.top = value
            self._size += 1

    def insert(self, value):
        current = self.top
        if current is None:
            self.tree[value] = {'depth': 1}
            self.top = value
            return
        depth = 2
        while not current is None:
            print current
            if current == value:
                return
            else:
                if current < value:
                    traverse = self.tree[current].get('right')
                    child = 'right'
                else:
                    traverse = self.tree[current].get('left')
                    child = 'left'
                if traverse is None:
                    #actual insert
                    self.tree[value] = {'depth': depth}
                    self.tree[current][child] = value
                    self._size += 1
                    return
                else:
                    current = traverse
            depth += 1

    def size(self):
        return self._size