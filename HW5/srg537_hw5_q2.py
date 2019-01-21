class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
    def __str__(self):
        s = ''
        for element in self.data:
            s += str(element) + ' '
        return s


class Deque:
    def __init__(self):
        self.front = 0
        self.back = 0
        self.data = []
        self.size = 0

    def add_first(self, val):
        if self.front > self.back:
            if self.back == self.front - 1:
                self.resize()
                self.front = len(self.data) - 1
                self.data[self.front] = val
            else:
                self.front -= 1
                self.data[self.front] = val
        elif self.back > self.front:
            if self.front == 0:
                self.resize()
                self.front = len(self.data) - 1
                self.data[self.front] = val
            else:
                self.front -= 1
                self.data[self.front] = val
        else:
            self.data.append(val)
            if (len(self) == 2):
                self.front = 1
                self.back = 0

        self.size += 1

    def add_last(self, val):
        if self.front > self.back:
            if self.back == self.front - 1:
                self.resize()
                self.back += 1
                self.data[self.back] = val
            else:
                self.back += 1
                self.data[self.back] = val
        elif self.back > self.front:
            if self.back == len(self.data) - 1:
                self.resize()
                self.back += 1
                self.data[self.back] = val
            else:
                self.back += 1
                self.data[self.back] = val
        else:
            self.data.append(val)
            if (len(self) == 2):
                self.back = 1
                self.front = 0
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty("double ended queue is empty")
        number = self.data[self.front]
        self.data[self.front] = None
        self.front += 1
        if self.is_empty():
            self.front = 0
            self.back = 0
            self.data = []
        self.size -= 1
        return number

    def delete_last(self):
        if self.is_empty():
            raise Empty("double ended queue is empty")
        number = self.data[self.back]
        self.data[self.back] = None
        self.back -= 1
        if self.is_empty():
            self.front = 0
            self.back = 0
            self.data = []
        self.size -= 1
        return number

    def resize(self):
        old_data = self.data[:]
        self.data = [None] * (len(self) * 2)
        if self.front > self.back:
            first_half = old_data[self.front:]
            second_half = old_data[:self.back + 1]
            index = 0
            for elem in first_half:
                self.data[index] = elem
                index += 1
            for elem in second_half:
                self.data[index] = elem
                index += 1
            self.front = 0
            self.back = len(old_data) - 1
        elif self.back > self.front:
            index = 0
            for elem in old_data:
                self.data[index] = elem
                index += 1
            self.front = 0
            self.back = len(old_data) - 1

    def __len__(self):
        count = 0
        for elem in self.data:
            if elem is not None:
                count += 1
        return count

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return len(self) == 0

# c = Deque()
# c.add_first(1)
# c.add_first(1)
# c.add_first(1)
# c.add_first(2)
# c.add_last(2)
# c.delete_first()


# print(len(c))

class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.deque = Deque()

    def is_empty(self):
        return (self.stack.is_empty() and self.deque.is_empty())

    def __len__(self):
        return len(self.stack) + len(self.deque)

    def push(self, e):
        self.deque.add_last(e)

    def top(self):
        if self.stack.is_empty() and self.deque.is_empty():
            raise Empty("Midstack is empty")
        else:
            return self.deque.back

    def pop(self):
        if (self.stack.is_empty() and self.deque.is_empty()):
            raise Empty("Midstack is empty")
        else:
            return self.deque.delete_last()

    def mid_push(self,e):

        if len(self.deque) % 2 == 0:
            for i in range(len(self.deque) // 2):
                    self.stack.push(self.deque.delete_first())

            self.stack.push(e)
            while (not self.stack.is_empty()):
                 self.deque.add_first(self.stack.pop())

        else:
            for i in range((len(self.deque)//2) + 1):
                self.stack.push(self.deque.delete_first())

            self.stack.push(e)
            while (not self.stack.is_empty()):
                self.deque.add_first(self.stack.pop())

a = MidStack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)


print(a.pop())

a.mid_push(7)
# print(a.pop())
# print(a.pop())
# print(a.pop())





