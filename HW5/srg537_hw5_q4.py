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
        return str(self.data)

a = (1,2)
print(a[0])

class MaxStack:
    def __init__(self):
        self.sheep = ArrayStack()
        self.max = None

    def is_empty(self):
        return len(self.sheep) == 0

    def __len__(self):
        len(self.sheep)

    def push(self,e):
        if self.max == None:
            self.max = e
        else:
            if self.sheep.top()[1] < e:
                self.max = e

        t = (e, self.max)
        self.sheep.data.append(t)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.sheep.top()[0]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        t = self.sheep.pop()
        return t[0]

    def maxi(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        t = self.sheep.top()
        return t[1]

    def __str__(self):
        return str(self.sheep)


# maxS = MaxStack()
# maxS.push(3)
# maxS.push(1)
# maxS.push(6)
# maxS.push(4)
# print(maxS)
# print(maxS.top())
# print(maxS.maxi())
# print(maxS.pop())
# print(maxS.pop())
# maxS.push(6)
# print(maxS.maxi())
