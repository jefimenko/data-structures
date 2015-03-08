#!/usr/bin/env python
import random
import subprocess


class Bst(object):
    """Binary Search Tree using a dictionary"""
    def __init__(self, value=None):
        self.tree = {}
        self.top = None
        self._size = 0
        self._depth = 0

        if value is not None:
            self.tree[value] = {'depth': 1}
            self.top = value
            self._size += 1
            self._depth += 1

    def insert(self, value):
        """Insert a node with value in order.

        In value is already present, it is ignored."""
        current = self.top
        if current is None:
            self.tree[value] = {'depth': 1}
            self.top = value
            self._size += 1
            self._depth += 1
            return
        depth = 1  # starts trying to insert at depth 2
        while current is not None:
            depth += 1
            if current == value:
                return
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
                if depth > self._depth:
                    self._depth = depth
                return
            current = traverse

    def balance(self):
        """Returns the balance of the tree:

        Returns a positive representing how much deeper the tree is on the
        right site or negative if the left is longer.
        Return 0 if the tree is balanced (same depth on both sides)

        """
        left_deep = 0
        right_deep = 0
        for node, v in self.tree.items():
            if self.top > node:
                if left_deep < v['depth']:
                    left_deep = v['depth']
            elif self.top < node:
                if right_deep < v['depth']:
                    right_deep = v['depth']
        return right_deep - left_deep

    def contains(self, value):
        """Returns true if value is in the tree."""
        return value in self.tree

    def size(self):
        """Returns the number of nodes in the tree."""
        return self._size

    def depth(self):
        """Returns the depth of the tree."""
        return self._depth

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if not self.tree else (
            "\n%s\n" % (
            # "\t%s;\n%s\n" % (
                # list(self.tree),
                "\n".join(self._get_dot(self.top))
            )
        ))

    def _get_dot(self, current):
        """recursively prepare a dot graph entry for this node."""
        left = self.tree[current].get('left')
        right = self.tree[current].get('right')
        if left is not None:
            yield "\t%s -> %s;" % (current, left)
            for i in self._get_dot(left):
                yield i
        elif right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (current, r)
        if right is not None:
            yield "\t%s -> %s;" % (current, right)
            for i in self._get_dot(right):
                yield i
        elif left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (current, r)

    def in_order(self, current='start'):
        """
        Generator that traverses the binary tree.
        """
        if current == 'start':
            current = self.top
        if current is not None:
            for node in self.in_order(self.tree[current].get('left')):
                yield node
            yield current
            for node in self.in_order(self.tree[current].get('right')):
                yield node

    def pre_order(self, current='dutch'):
        """Generator that traverses the binary tree."""
        if current == 'dutch':
            current = self.top
        if current is not None:
            yield current
            for node in self.in_order(self.tree[current].get('left')):
                yield node
            for node in self.in_order(self.tree[current].get('right')):
                yield node

    def post_order(self, current='dutch'):
        """Generator that traverses the binary tree."""
        if current == 'dutch':
            current = self.top
        if current is not None:
            for node in self.in_order(self.tree[current].get('left')):
                yield node
            self.in_order(self.tree[current].get('right')).next()
            for node in self.in_order(self.tree[current].get('right')):
                yield node

    def breadth_first(self):
        """Generator that traverses the binary tree in breadth first order."""
        node_list =[]
        node_list.append(self.top)
        current = self.top
        while node_list:
            current = node_list.pop(0)
            if self.tree[current].get('left') is not None:
                node_list.append(self.tree[current].get('left'))
            if self.tree[current].get('right') is not None:
                node_list.append(self.tree[current].get('right'))
            yield current  


def main():
    """Best case and worst case are the same."""
    tree = Bst()
    for num in reversed(range(10)):
        tree.insert(num)
    for num in range(10, 15):
        tree.insert(num)
    print tree.tree
    for num in enumerate(tree.breadth_first()):
        print num
    dot_graph = tree.get_dot()
    t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    # t.communicate(dot_graph)


if __name__ == '__main__':
    main()
