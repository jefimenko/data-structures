#!/usr/bin/env python
import random
import subprocess
from collections import deque


class Bst(object):
    """Binary Search Tree using a dictionary"""
    def __init__(self, value=None):
        self.tree = {}
        self.top = None
        self._size = 0
        self._depth = 0

        if value is not None:
            self.tree[value] = {}
            self.top = value
            self._size += 1
            self._depth += 1

    def left(self, current):
        return self.tree[current].get('left')

    def right(self, current):
        return self.tree[current].get('right')

    def parent(self, current):
        return self.tree[current].get('parent')

    def insert(self, value):
        """Insert a node with value in order.

        In value is already present, it is ignored."""
        current = self.top
        if current is None:
            self.tree[value] = {}
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
                traverse = self.right(current)
                child = 'right'
            else:
                traverse = self.left(current)
                child = 'left'
            if traverse is None:
                #actual insert
                self.tree[value] = {}

                self.tree[current][child] = value
                self.tree[value]['parent'] = current
                self._size += 1
                if depth > self._depth:
                    self._depth = depth
                return
            current = traverse

    def delete(self, val):
        if self.contains(val):
            left_child = self.left(val)
            right_child = self.right(val)
            parent = self.parent(val)
            if left_child is None and right_child is None:
            # Delete a node with not children
                if parent is not None:
                # For a node with a parent...
                    if self.left(parent) == val:
                        del self.tree[parent]['left']
                    else:
                        del self.tree[parent]['right']
                else:
                    # For deleting a node that is the root with no children
                    self.top = None
                del self.tree[val]
            elif left_child is not None:
                biggest_child = self._rightmost(left_child)
                self._swap_nodes(val, biggest_child)
                self.delete(val)
            else:
                if parent is not None:
                    if self.left(parent) == val:
                        self.tree[parent]['left'] = right_child
                    else:
                        self.tree[parent]['right'] = right_child
                    self.tree[right_child]['parent'] = parent
                else:
                    self.top = right_child
                del self.tree[val]


    def _swap_nodes(self, current, target):
        """
        Swap two nodes.

        Additionally, update all information on related nodes, as in, children
        and parent nodes.
        """
        cur_parent = self.parent(current)
        targ_parent = self.parent(target)

        children = []

        children.append(self.left(current))
        children.append(self.right(current))
        children.append(self.left(target))
        children.append(self.right(target))

        for child in children:
            # If a node children, update it's childrens' information
            # for 'swapping'
            if child and self.parent(child) == current:
                self.tree[child]['parent'] = target
            elif child:
                self.tree[child]['parent'] = current

        # Swapping information in the parent nodes relative to the nodes being 'swapped'
        if current != self.top:
            if current == self.tree.get(cur_parent).get('left'):
                self.tree[cur_parent]['left'] = target
            else:
                self.tree[cur_parent]['right'] = target

        if target == self.tree.get(targ_parent).get('left'):
            self.tree[targ_parent]['left'] = current
        else:
            self.tree[targ_parent]['right'] = current

        # Swap current and target's left, right, and parent information
        self.tree[current], self.tree[target] = self.tree[target], self.tree[current]

        if current == self.top:
            self.top = target


    def _rightmost(self, start):
        """Returns None if start is empty tree"""
        while start is not None:
            if self.right(start) is None:
                return start
            start = self.right(start)



        # left_of_parent = self.left(self.parent(current))
        # right_of_parent = self.right(self.parent(current))

        # if current == val:
        #     if current == left_of_parent:
        #         del self.tree[self.parent(current)]['left']
        #     else:
        #         del self.tree[self.parent(current)]['right']

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
                if left_deep < self.node_depth(node):
                    left_deep = self.node_depth(node)
            elif self.top < node:
                if right_deep < self.node_depth(node):
                    right_deep = self.node_depth(node)
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

    def node_depth(self, current):
        """Returns the depth of a node in the tree."""
        depth = 0
        while current is not None:
            current = self.parent(current)
            depth +=1
        return depth

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
        parent = self.tree[current].get('parent')
        if parent is not None:
            yield "\t%s -> %s;" % (current, parent)

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
        Generator that traverses the binary tree in order.
        """
        if current == 'start':
            current = self.top
        if current is not None:
            for node in self.in_order(self.left(current)):
                yield node
            yield current
            for node in self.in_order(self.right(current)):
                yield node


    def pre_order(self, current='dutch'):
        """Generator that traverses the binary tree pre order."""
        if current == 'dutch':
            current = self.top
        if current is not None:
            yield current
            for node in self.pre_order(self.left(current)):
                yield node
            for node in self.pre_order(self.right(current)):
                yield node

    def post_order(self, current='dutch'):
        """Generator that traverses the binary tree post order."""
        if current == 'dutch':
            current = self.top
        if current is not None:
            for node in self.post_order(self.left(current)):
                yield node
            for node in self.post_order(self.right(current)):
                yield node
            yield current

    def breadth_first(self):
        """Generator that traverses the binary tree in breadth first order."""
        q1 = deque()
        q1.appendleft(self.top)
        current = self.top
        while q1:
            current = q1.pop()
            if self.left(current) is not None:
                q1.appendleft(self.left(current))
            if self.right(current) is not None:
                q1.appendleft(self.right(current))
            yield current


def main():
    """Best case and worst case are the same."""
    tree = Bst()
    inserts = [7, 4, 11, 2, 9, 6, 12, 5, 13, 0, 10, 8, 3, 1]
    for i in inserts:
        tree.insert(i)

    tree._swap_nodes(6, 4)
    print tree.tree
    # for num in enumerate(tree.pre_order()):
    #     print num
    dot_graph = tree.get_dot()
    t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    t.communicate(dot_graph)


if __name__ == '__main__':
    main()
