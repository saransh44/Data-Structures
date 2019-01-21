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

def copy_linked_list(lnk_lst):
    result = DoublyLinkedList()
    for element in lnk_lst:
        result.add_last(element)
    return result

def deep_copy_linked_list(lnk_lst):
    result = DoublyLinkedList()

    now = lnk_lst.first_node()

    while now.data is not None:
        if (isinstance(now.data, int)):
            result.add_last(now.data)
            now = now.next
        elif (isinstance(now.data, DoublyLinkedList)):
            result.add_last(deep_copy_linked_list(now.data))
            now = now.next

    return result

lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
lnk_lst1.add_last(elem1)
elem2 = 6
lnk_lst1.add_last(elem2)
lnk_lst1.add_last(elem1)

print(lnk_lst1)
lnk_lst2 = deep_copy_linked_list(lnk_lst1)
print(lnk_lst2)
# # print(elem1.first_node().next.next.data)
# lnk_lst2 = copy_linked_list(lnk_lst1)
# print("lnk1", lnk_lst1)
# print(elem1)
# # lnk_lst2 = deep2(lnk_lst1)
# print("lnk2", lnk_lst2)