class ArrayStack: #uses of stack, undo/redo in text editor (checking data in reverse), checking isbalanced, Post fix notation (5 1 2 + * --> (1+2) *5), lines (q)
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
    def __str__(self):
        s = ''
        for element in self.data:
            s += str(element) + ' '
        return s


def balanced_expression(string_input):
	'''
return true if the string is a balanced expression, meaning that for every ")" there is also a "(" in the corresponding position. This function checks for () [] {}

append open cases to a stack. when you come across a closed case, check if the index of that closed case is equal to the very top item in stack. If they are, continue, else, it means it is not balanced so return false. Have a check at the end if the stack is empty (which is should be). If not, some open cases are left. Could have just a single closed case or single open case.
	'''

	from collections import deque

	open_case = ('(', '[', '{')
	closed_case = (')', ']', '}')

	stack1 = []

	for c in string_input:
		if c in open_case:
			stack1.append(c)
		if c in closed_case:
			if len(stack1) > 0:
				if closed_case.index(c) == open_case.index(stack1.pop()):
					continue
				else:
					return False
			else:
				return False
	if len(stack1) > 0:
		return False
	else:
		return True

'''
print(balanced_expression('{{([])}}([])'))
print(balanced_expression('{{[(])}}'))
print(balanced_expression('([]{{[]}())}'))
print(balanced_expression('(([]{{[]}})'))
print(balanced_expression('([]{{[]}()})'))
'''


class Queue:
    def __init__(self, n=10):
        self.data = [None] * n
        self.front = 0
        #self.nextInsert = 0
        self.count = 0

    def resize(self, cap):
        old = self.data
        self.data = [None]*cap
        for i in range(self.count):
            self.data = old[(i+self.front)%len(old)]
        self.front=0

    def enqueue(self, val):
        if(self.count >= len(self.data)):
            self.resize(len(self.data) * 2)
        back = (self.front+self.count) % len(self.data)
        self.data[back] = val
        self.count += 1

    def dequeue(self):
        if(self.count==0):
            raise Empty()
        retVal = self.data[self.front]
        self.data[self.front] = None
        self.front += (self.front+1)%len(self.data)
        self.count -= 1
        return retVal

    def __len__(self):
        return len(self.data)

    def __str__(self):
        lst = []
        for i in range(len(self.data)):
            lst.append(self.data[i])
        return(str(lst))

class double_ended_queue:
	'''
	Elements can be inserted/removed at front and back of queue. Standard operations still run in O(1) amortized runtime.
	'''
	def __init__(self):
		self.front = 0
		self.rear = 0
		self.data = []

	def add_first(self, val):
		if self.front > self.rear:				#if front looped around before rear
			if self.rear == self.front-1:		#check if space available before
				self.resize()
				self.front = len(self.data)-1	#make first equal to last index
				self.data[self.front] = val
			else:								#space available to add at front-1
				self.front -= 1
				self.data[self.front] = val
		elif self.rear > self.front:			#front has no looped around yet
			if self.front == 0:					#check if spaces before 0 are available
				self.resize()
				self.front = len(self.data)-1	#make front point to last index
				self.data[self.front] = val
			else:								#space available, not at beginning
				self.front -= 1
				self.data[self.front] = val
		else:
			self.data.append(val)
			if (len(self) == 2):
				self.front = 1
				self.rear = 0

	def add_last(self, val):
		if self.front > self.rear:			#front loop around before rear
			if self.rear == self.front-1:	#no space available to add at rear
				self.resize()
				self.rear += 1
				self.data[self.rear] = val
			else:							#space available, insert at end
				self.rear += 1
				self.data[self.rear] = val
		elif self.rear > self.front:
			if self.rear == len(self.data)-1:	#at the last index
				self.resize()
				self.rear += 1
				self.data[self.rear] = val
			else:							#not at last index, space available at end
				self.rear += 1
				self.data[self.rear] = val
		else:
			self.data.append(val)
			if (len(self) == 2):
				self.rear = 1
				self.front = 0

	def delete_first(self):
		if self.is_Empty():
			raise IndexException('empty double_ended_queue')
		number = self.data[self.front]
		self.data[self.front] = None
		self.front += 1
		if self.is_Empty():					#reset back to everything when empty
			self.front = 0
			self.rear = 0
			self.data = []
		return number

	def delete_last(self):
		if self.is_Empty():
			raise IndexException('empty double_ended_queue')
		number = self.data[self.rear]
		self.data[self.rear] = None
		self.rear -= 1
		if self.is_Empty():					#reset back to everything when empty
			self.front = 0
			self.rear = 0
			self.data = []
		return number

	def resize(self):								#sort numbers in front to last order. double space.
		old_data = self.data[:]
		self.data = [None] * (len(self) * 2)
		if self.front > self.rear:					#front numbers are at end
			first_half = old_data[self.front:]
			second_half = old_data[:self.rear+1]
			index = 0
			for elem in first_half:
				self.data[index] = elem
				index += 1
			for elem in second_half:
				self.data[index] = elem
				index += 1
			self.front = 0							#front is zero and rear is pointing to last index
			self.rear = len(old_data)-1
		elif self.rear > self.front:				#in inserted order, that needs more space.
			index = 0
			for elem in old_data:
				self.data[index] = elem
				index += 1
			self.front = 0
			self.rear = len(old_data)-1

	def __len__(self):
		count = 0
		for elem in self.data:
			if elem is not None:
				count += 1
		return count

	def __str__(self):
		return str(self.data)

	def is_Empty(self):
		return len(self) == 0
