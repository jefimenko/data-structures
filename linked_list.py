# class for list node
class list_node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# class for linked list
class linked_list(object):
    def __init__(self, *args):
        self.head = None
        self._size = 0
        # if args:
        #    self.head = args[0]

    def insert(self, val):
        """
        From a given val, create a new node with .data attribute set to val
        and rearrange the list so the head is the new node with a reference
        to the old head.
        """
        new_node = list_node(val, self.head)
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
        return self._size

    def search(self, val):
        temp = self.head
        while temp is not None:
            if temp.data == val:
                return temp
            else:
                temp = temp.next
        return None


a = linked_list()
a.insert('a')
a.insert('b')
a.insert('c')
a.insert('d')
a.size()

