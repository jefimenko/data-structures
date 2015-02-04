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

    def remove(self, node_id):
        """
        Remove a node with that has a given value, node id.
        """
        temp = self.head
        if temp.data == node_id:
            self.head = temp.next
        else:
            while not(temp.next is None):
                if temp.next.data == node_id:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next


b = list_node(500000000)
print b

a = linked_list()
a.insert('a')
a.insert('b')
a.insert('c')
a.insert('d')
print a.size()

a.remove('a')
a.remove('d')
a.remove('c')
print a.head.data
