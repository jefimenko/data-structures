#class for list node
class list_node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#class for linked list
class linked_list(object):
    def __init__(self, *args):
        self.head = None
        #if args:
            #self.head = args[0]


