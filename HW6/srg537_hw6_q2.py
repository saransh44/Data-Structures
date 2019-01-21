class Empty(Exception):
    pass

class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if(self.is_empty()):
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)

class Integer:
    def __init__(self, num_str):
        self.i = DoublyLinkedList()
        self.num = num_str
        if (len(num_str)>0):
            for char in  num_str:
                self.i.add_last(int(char))

    def __add__(self, other):
        temp1 = Integer(self.num)
        temp2 = Integer(other.num)
        dTotal = 0
        carry = 0
        toReturn = Integer('')

        if len(other) < len(self):
            for i in range(len(other)):
                dTotal = temp2.i.delete(temp2.i.last_node()) + temp1.i.delete(temp1.i.last_node())+carry
                toReturn.i.add_first(dTotal % 10)
                carry = dTotal // 10
            for i in range(len(temp1)):
                dTotal = temp1.i.delete(temp1.i.last_node())+carry
                toReturn.i.add_first(dTotal % 10)
                carry = dTotal//10

        else:
            for i in range(len(self)):
                dTotal = temp2.i.delete(temp2.i.last_node()) + temp1.i.delete(temp1.i.last_node()) + carry
                toReturn.i.add_first(dTotal % 10)
                carry = dTotal // 10
            for i in range(len(temp2)):
                toReturn.i.add_first(temp2.i.delete(temp2.i.last_node()))

        if (toReturn.i.first_node().data == 0 and carry > 0):
            toReturn.i.add_first(carry)

        return toReturn

    def __str__(self):
        return ''.join([str(elem) for elem in self.i])


    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.i)
