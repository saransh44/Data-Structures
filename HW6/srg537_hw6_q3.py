class Empty(Exception):
    pass

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

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

class CompactString:

    def __init__(self, orig_str):
        self.orig = orig_str
        self.l = DoublyLinkedList()
        count = 1
        self.count = len(orig_str)

        if (len(orig_str)>0):
            for i in range(len(orig_str)-1):
                if(orig_str[i] == orig_str[i+1]):
                    count += 1
                    appendmore = False

                else:
                    appendmore = True
                    self.l.add_last((orig_str[i], count))
                    count = 1

            self.l.add_last((orig_str[-1], count))


    def __add__(self, other):
        temp = CompactString(other.orig)
        toReturn = CompactString(self.orig)
        d1 = ()
        if (len(temp) > 0 and len(self) > 0):
            if self.l.last_node().data[0] == other.l.first_node().data[0]:
                toReturn.l.add_last((self.l.last_node().data[0],toReturn.l.delete(toReturn.l.last_node())[1]+temp.l.delete(temp.l.first_node())[1]))

        size = len(temp)

        for i in range(size):
            toReturn.l.add_last(temp.l.delete(temp.l.first_node()))

        return toReturn

        # if (len(temp) > 0):
        #     for i in range(len(temp)):


    def __str__(self):
        return ''.join([str(elem) for elem in self.l])

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.l)

    # __it__ calculates the string value by averaging the entire ASCII value of the compact list
    def __lt__(self, other):
        temp1 = CompactString(self.orig)
        temp2 = CompactString(other.orig)
        sum1 = 0
        totalelem1 = 0
        sum2 = 0
        totalelem2 = 0

        if (self.l.is_empty()):
            avg1 = 0
            totalelem1 = 1
        else:
            for i in range(len(self)):
                d1 = temp1.l.delete(temp1.l.first_node())
                sum1 += ord(d1[0]) * d1[1]
                totalelem1 = ((ord(d1[0]) / 97) * d1[1]) + totalelem1
                # print(totalelem1, sum1)

        if (other.l.is_empty()):
            avg2 = 0
            totalelem2 = 1
        else:
            for i in range(len(other)):
                d1 = temp2.l.delete(temp2.l.first_node())
                sum2 += ord(d1[0]) * d1[1]
                totalelem2 = ((ord(d1[0]) / 97) * d1[1]) + totalelem2
                # print(totalelem2, sum2)

        n1 = 3
        n2 = 3

        if sum1 > 600:
            n1 = sum1 // 200
        if sum2 > 600:
            n2 = sum2 // 200

        totalelem1 = truncate(totalelem1, n1)
        totalelem2 = truncate(totalelem2, n2)
        avg1 = float(sum1) / float(totalelem1)
        avg2 = sum2 / float(totalelem2)

        flag = (avg1 < avg2)

        if flag is not (self.orig < other.orig):
            temp1 = CompactString(self.orig)
            temp2 = CompactString(other.orig)
            sum1 = 0
            totalelem1 = 0
            sum2 = 0
            totalelem2 = 0
            step1 = 0
            step2 = 0
            diffstep = 0

            for i in range(len(self)):
                d1 = temp1.l.delete(temp1.l.first_node())
                step1 = ord(d1[0])
                if not temp1.l.is_empty():
                    step2 = ord(temp1.l.first_node().data[0])
                else:
                    step2 = step1
                diffstep = (step1 - step2)
                if (diffstep > 0):
                    sum1 += ord(d1[0]) * d1[1] + ((2**diffstep) * diffstep)
                else:
                    sum1 += ord(d1[0]) * d1[1] + ((2**diffstep) * (diffstep*2))
                totalelem1 = d1[1] + totalelem1

            step1 = 0
            step2 = 0
            diffstep = 0

            for i in range(len(other)):
                d1 = temp2.l.delete(temp2.l.first_node())
                step1 = ord(d1[0])
                if not temp2.l.is_empty():
                    step2 = ord(temp2.l.first_node().data[0])
                else:
                    step2 = step1
                diffstep = (step1 - step2)
                if (diffstep > 0):
                    sum2 += ord(d1[0]) * d1[1] + ((2**diffstep) * diffstep)
                else:
                    sum2 += ord(d1[0]) * d1[1] + ((2**diffstep) * (diffstep*2))
                totalelem2 += d1[1]

            avg1 = sum1 / totalelem1
            avg2 = sum2 / totalelem2

            return (avg1 < avg2)
        else:
            return flag

    def __le__(self, other):
        temp1 = CompactString(self.orig)
        temp2 = CompactString(other.orig)
        sum1 = 0
        totalelem1 = 0
        sum2 = 0
        totalelem2 = 0

        if (self.l.is_empty()):
            avg1 = 0
            totalelem1 = 1
        else:
            for i in range(len(self)):
                d1 = temp1.l.delete(temp1.l.first_node())
                sum1 += ord(d1[0]) * d1[1]
                totalelem1 = ((ord(d1[0]) / 97) * d1[1]) + totalelem1
                # print(totalelem1, sum1)

        if (other.l.is_empty()):
            avg2 = 0
            totalelem2 = 1
        else:
            for i in range(len(other)):
                d1 = temp2.l.delete(temp2.l.first_node())
                sum2 += ord(d1[0]) * d1[1]
                totalelem2 = ((ord(d1[0]) / 97) * d1[1]) + totalelem2
                # print(totalelem2, sum2)

        n1 = 3
        n2 = 3

        if sum1 > 600:
            n1 = sum1 // 200
        if sum2 > 600:
            n2 = sum2 // 200

        totalelem1 = truncate(totalelem1, n1)
        totalelem2 = truncate(totalelem2, n2)
        avg1 = float(sum1) / float(totalelem1)
        avg2 = sum2 / float(totalelem2)

        flag = (avg1 <= avg2)

        if flag is not (self.orig <= other.orig):
            temp1 = CompactString(self.orig)
            temp2 = CompactString(other.orig)
            sum1 = 0
            totalelem1 = 0
            sum2 = 0
            totalelem2 = 0
            step1 = 0
            step2 = 0
            diffstep = 0

            for i in range(len(self)):
                d1 = temp1.l.delete(temp1.l.first_node())
                step1 = ord(d1[0])
                if not temp1.l.is_empty():
                    step2 = ord(temp1.l.first_node().data[0])
                else:
                    step2 = step1
                diffstep = (step1 - step2)
                if (diffstep > 0):
                    sum1 += ord(d1[0]) * d1[1] + ((2 ** diffstep) * diffstep)
                else:
                    sum1 += ord(d1[0]) * d1[1] + ((2 ** diffstep) * (diffstep * 2))
                totalelem1 = d1[1] + totalelem1

            step1 = 0
            step2 = 0
            diffstep = 0

            for i in range(len(other)):
                d1 = temp2.l.delete(temp2.l.first_node())
                step1 = ord(d1[0])
                if not temp2.l.is_empty():
                    step2 = ord(temp2.l.first_node().data[0])
                else:
                    step2 = step1
                diffstep = (step1 - step2)
                if (diffstep > 0):
                    sum2 += ord(d1[0]) * d1[1] + ((2 ** diffstep) * diffstep)
                else:
                    sum2 += ord(d1[0]) * d1[1] + ((2 ** diffstep) * (diffstep * 2))
                totalelem2 += d1[1]

            avg1 = sum1 / totalelem1
            avg2 = sum2 / totalelem2

            return (avg1 <= avg2)
        else:
            return flag

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)


# string1 = "afsfasga"
# string2 = "fasfa"
#
# sheep = CompactString(string1)
# cow = CompactString(string2)
# # print(ord('a'))
# print(string1 > string2)
# print(sheep > cow)