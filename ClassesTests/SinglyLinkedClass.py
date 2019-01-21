class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinked:
    """
    Note: need
    insert at beginning
    __str__
    __len__
    """
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def __len__(self):
        return self.length
#        counter = 0
#        curr = self.head
#        while curr is not None:
#            counter += 1
#            curr = curr.next
#        return counter
        
    def insertHead(self, value):
        self.head = Node(value, self.head)
        if self.head.next is None:
            self.tail = self.head
        self.length += 1

    def __iter__(self):
        # if(self.is_empty()):
        #     return
        cursor = self.head
        while(cursor is not None):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)
        

# if __name__ == '__main__':
#     sll = SinglyLinked()
#     print(sll)
#     sll.insertHead(17)
#
    
