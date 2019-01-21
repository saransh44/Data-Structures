class LinkedStack: #uses of stack, undo/redo in text editor (checking data in reverse), checking isbalanced, Post fix notation (5 1 2 + * --> (1+2) *5), lines (q)
    def __init__(self):
        self.data = []
    def push(self,val):
        self.data.append(val)
    def pop(self):
        if self.is_empty():
            raise Exception("Trying to pop from an empty list")
        return self.data.pop()
    def top(self):
        return self.data[-1]
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0