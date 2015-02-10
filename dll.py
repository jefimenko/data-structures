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
            self.head = self.tail = ListItem(val)
        else:
            self.head = ListItem(val, self.head)
