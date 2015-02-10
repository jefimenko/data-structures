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
        if self.head is None:
            # insert() on an empty list.
            self.head = self.tail = ListItem(val)
        else:
            # insert() on a list with items.
            self.head = ListItem(val, self.head)
            self.head.next.prev = self.head

    def append(self, val):
        """
        Append a ListItem with at the tail/end of a DoublyLinkedList.
        """
        if self.head is None:
            self.tail = self.head = ListItem(val)
        else:
            self.tail = ListItem(val, prev=self.tail)
            self.tail.prev.next = self.tail

    def pop(self):
        """
        Remove the very first ListItem from the list
        """
        # Empty list
        try:
            temp = self.head.data
        except AttributeError:
            raise IndexError

        # List of one
        if self.head is self.tail:
            self.head = self.tail = None
        # List of more than one
        else:
            self.head = self.head.next
            self.head.prev = None
        return temp

    def shift(self):
        """
        Remove the very last ListItem from the list
        """
        # Empty list
        try:
            temp = self.tail.data
        except AttributeError:
            raise IndexError
        # List of one
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return temp

    def remove(self, val):
        """
        Remove the ListItem with data the same as val
        """
        temp = self.head
        try:
            if self.head.data == val:
                # At the head
                self.pop()
            elif self.tail.data == val:
                # At the tail
                self.shift()
            else:
                while temp.next:
                    # Begin looking for val
                    if temp.next.data == val:
                        temp.next = temp.next.next
                        temp.next.prev = temp
                        break
                    else:
                        temp = temp.next
                else:
                    # Go through the whole list without finding val
                    raise ValueError
        # If the list is empty
        except AttributeError:
            raise IndexError
