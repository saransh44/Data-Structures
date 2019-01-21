from Deque import Deque
from Deque import Empty
from ArrayQueue import ArrayQueue
from DoublyLinkedList import DoublyLinkedList
from SinglyLinkedClass import SinglyLinked
from SinglyLinkedClass import Node


def IsPalindrome(d):

    b = ""
    f = ""
    for i in range(len(d)):
        ch = d.delete_last()
        b = b + ch
        f = ch + f

    print(b)
    print(f)

    return (b == f)

deque = Deque()
# deque.delete_last()
deque.add_last("r")
deque.add_last("b")
deque.add_last("c")
deque.add_last("e")
deque.add_last("c")
deque.add_last("a")
deque.add_last("r")

print(IsPalindrome(deque))

sll = SinglyLinked()
[sll.insertHead(i) if i > 3 and i < 7 else sll.insertHead(4) for i in range(8)]
print(sll)

def removeNums(node, val):
    while node.next != None:
        next = node.next
        if node.data is val:
            node = None
            node.next.next = next

        else:
            node = node.next
        # if node.next.data is val:
        #     node.next = None
    # if node is val:
    #     node.data = None

def r (node, removal):
    # current = Node("Fake")
    # current.next = node
    current = node
    while current != None and current.next != None:
        if current.next.data is removal:
            current.next = current.next.next
        else:
           current = current.next


    if node.data is removal:
        node = node.next

    return node

r(sll.head, 4)
print(sll.head.data)
