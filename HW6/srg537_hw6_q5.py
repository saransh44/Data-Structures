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

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    result2 = DoublyLinkedList()

    def merge_sublists(lnk1, lnk2, now1, now2):

        if now1.data and now2.data is not None:
            if now1.data <= now2.data:
                result2.add_last(now1.data)
                now1 = now1.next

            elif now1.data > now2.data:
                result2.add_last(now2.data)
                now2 = now2.next

        elif now1.data is not None:
            result2.add_last(now1.data)
            now1 = now1.next

        elif now2.data is not None:
            result2.add_last(now2.data)
            now2 = now2.next

        if now1.data or now2.data is not None:
            merge_sublists(lnk1, lnk2, now1, now2)
            return result2

    if srt_lnk_lst1.is_empty():
        result2 = srt_lnk_lst2
        return result2
    elif srt_lnk_lst2.is_empty():
        result2 = srt_lnk_lst1
        return result2
    else:
        return merge_sublists (srt_lnk_lst1, srt_lnk_lst2, srt_lnk_lst1.first_node(), srt_lnk_lst2.first_node())


# def merge(lnk1, lnk2, now1, now2):
#     result = DoublyLinkedList()
#     temp1 = DoublyLinkedList()
#     temp2= DoublyLinkedList()
#
#     if now1.data < now2.data:
#         temp1 = lnk1
#         temp2 = lnk2
#     else:
#         temp1 = lnk2
#         temp2 = lnk1
#
#     now1 = temp1.first_node()
#     now2 = temp2.first_node()
#     while now2.data is not None:
#         while now1.data is not None and now1.data <= now2.data:
#             result.add_last(now1.data)
#             now1 = now1.next
#         result.add_last(now2.data)
#         now2 = now2.next
#
#     return result

s = DoublyLinkedList()
s2 = DoublyLinkedList()

s.add_last(1)
s.add_last(12)
s.add_last(10)
s.add_last(6)
s.add_last(8)

s2.add_last(2)
s2.add_last(3)
s2.add_last(5)
s2.add_last(10)
s2.add_last(15)
s2.add_last(18)

print(s)
print(s2)
s3 = merge_linked_lists(s,s2)

# print(s3)


def findMax(node):
    if node.next.data is None:
        return node.data

    else:
        m = findMax(node.next)
        return max(node.data, m)


m1 = findMax(s.first_node())

print(m1)

st = "sheep"
ch = 'e'
lst1 = [0,1,2]
lst2 = ['s','h','i','t']
if ch in st:
    lst3 = lst1+lst2
print(lst3)