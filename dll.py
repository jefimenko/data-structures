class ListItem(object):
    """
    ListItem class to be used by DoublyLinkedList
    """
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    """
    DoublyLinkedList class using ListItem
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        """
        insert function to insert a ListItem at head/front of DoublyLinkedList
        """
        if self.head == None:
            # insert() on an empty list.
            self.head = self.tail = ListItem(val)
        else:
            # insert() on a list with items.
            self.head = ListItem(val, self.head)
            self.head.next.prev = self.head
