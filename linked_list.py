class List_Node(object):
    """
    List_Node class to create a node that reference another node used by
    the Linked_List class
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_List(object):
    """
    Linked_List class to have values connected to on another using List_Node
    """
    def __init__(self):
        """
        Create an empty Linked_List with a size of 0
        """
        self.head = None
        self._size = 0

    def __str__(self):
        """
        Print the Linked_List in a string when the Linked_List is called.
        """
        return self.display_prep()

    def __repr__(self):
        return self.display_prep()

    def insert(self, val):
        """
        From a given val, create a new node.

        Set .data attribute to val and rearrange the list so the head is 
        the new node with a reference to the old head.
        """
        self.head = List_Node(val, self.head)
        self._size += 1

    def pop(self):
        """
        Remove the item at the head of the linked list.
        """
        self._size -= 1
        result = self.head
        self.head = self.head.next
        return result.data

    def size(self):
        """
        Return an integer equal to the number of nodes in the list.
        """
        return self._size

    def search(self, val):
        """
        Search through the Linked_List for given value. 

        If found return the List_Node if not found return None
        """
        temp = self.head
        while temp is not None:
            if temp.data == val:
                return temp
            else:
                temp = temp.next
        return None

    def remove(self, node):
        """
        Remove a node with that has a given value, node id.

        For linked lists with multiple nodes with identical values,
        only the leftmost/most recently added occurence will be removed.
        """
        temp = self.head
        if temp.data == node.data:
            self.pop()
        else:
            while not(temp.next is None):
                if temp.next.data == node.data:
                    temp.next = temp.next.next
                    self._size -= 1
                    break
                else:
                    temp = temp.next

    def display(self):
        """
        Print the string representation of this list.
        """
        print self.display_prep()

    def display_prep(self):
        """
        Return a string representation of the list.

        The most recently added is the leftmost to appear in the console.
        """
        temp = self.head
        output = "("

        while temp:
            dummy = temp.data
            if isinstance(temp.data, str or unicode):
                dummy = "'{}'".format(dummy.encode('utf-8'))

            if temp is self.head:
                output = "{}{}".format(output, dummy)
            else:
                dummy = str(dummy)
                output = "{}, {}".format(output, dummy)
            temp = temp.next


        return output + ")"
