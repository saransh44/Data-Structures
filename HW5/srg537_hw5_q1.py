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

class Queue:
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()

    def enqueue (self, element):
        self.stack1.push(element)
        print(self.stack1)

    def dequeue (self):
        if (self.stack1.is_empty()):
            raise Empty("Stack is empty")
        else:
            while (not self.stack1.is_empty()):
                self.stack2.push(self.stack1.pop())

            temp = self.stack2.pop()

            while (not self.stack2.is_empty()):
                self.stack1.push(self.stack2.pop())

            return temp

    def __str__(self):
        s = ''
        for element in self.stack1.data:
            s += str(element) + ' '
        return s





