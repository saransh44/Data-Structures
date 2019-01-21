import copy

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

class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

    def __str__(self):
        lst = []
        for i in range(len(self.data)):
            lst.append(self.data[i])
        return(str(lst))

def permutations(lst):
    stack = ArrayStack()
    q = ArrayQueue()
    current = None
    temp = []
    temp_changed = []
    result = []
    if (len(lst) == 0):
        return None
    else:
        for i in range(len(lst)):
            stack.push(lst[i])
        q.enqueue([stack.pop()])

        while (not stack.is_empty()):
            temp = []
            result = []
            final = []
            current = stack.pop()
            while (not q.is_empty()):
                temp = q.dequeue()
                # print(temp)
                for i in range(len(temp)+1):
                    temp_changed = copy.deepcopy(temp)
                    temp_changed.insert(i,current)
                    result.append(temp_changed)
                    # print(result)

            for element in result:
                q.enqueue(element)

        for element in q.data:
            if element is not None:
                stack.push(q.dequeue())
                print(element)
        return stack

print(permutations([1,2,3,4]))