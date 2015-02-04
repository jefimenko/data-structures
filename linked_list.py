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
        print the Linked_List in a string when the Linked_List is called
        """
        return self.display_prep()

    def insert(self, val):
        """
        From a given val, create a new node with .data attribute set to val
        and rearrange the list so the head is the new node with a reference
        to the old head.
        """
        new_node = List_Node(val, self.head)
        self.head = new_node
        self._size += 1

    def pop(self):
        """
        Remove the item at the head of the linked list, and rearrange
        accordingly.
        """
        self.head = self.head.next
        self._size -= 1

    def size(self):
        """
        Return an integer equal to the number of nodes in the list.
        """
        return self._size

    def search(self, val):
        temp = self.head
        while temp is not None:
            if temp.data == val:
                return temp
            else:
                temp = temp.next
        return None

    def remove(self, node_id):
        """
        Remove a node with that has a given value, node id.
        """
        temp = self.head
        if temp.data == node_id:
            self.head = temp.next
            self._size -= 1
        else:
            while not(temp.next is None):
                if temp.next.data == node_id:
                    temp.next = temp.next.next
                    self._size -= 1
                    break
                else:
                    temp = temp.next

    def display(self):
        """
        using the display_prep method print the string representation of this 
        list
        """
        print self.display_prep()

    def display_prep(self):
        """
        return a string representation of the list, where the most recently
        added is the leftmost to appear in the console.
        """
        output = "("
        temp = self.head
        while temp is not None:
            dummy = temp.data
            if isinstance(dummy, str):
                dummy = "'" + dummy + "'"
            dummy = str(dummy)
            if temp.next:
                output += dummy + ", "
            else:
                output += dummy + ')'
            temp = temp.next
        return output
