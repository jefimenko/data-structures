# class for list node
class list_node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# class for linked list
class linked_list(object):
    def __init__(self, *args):
        self.head = None
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

    def pop(self):
        """
        Remove the item at the head of the linked list, and rearrange
        accordingly.
        """
        self.head = self.head.next
