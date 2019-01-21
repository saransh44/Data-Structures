class Empty(Exception):
	pass
	
class Deque:
	
	def __init__(self):
		self.front = 0
		self.rear = 0
		self.data = []
	
	def add_first(self, val):
		if self.front > self.rear:
			if self.rear == self.front-1:
				self.resize()
				self.front = len(self.data)-1
				self.data[self.front] = val	
			else:
				self.front -= 1
				self.data[self.front] = val
		elif self.rear > self.front:
			if self.front == 0:
				self.resize()				
				self.front = len(self.data)-1
				self.data[self.front] = val
			else:
				self.front -= 1
				self.data[self.front] = val	
		else:
			self.data.append(val)
			if (len(self) == 2):
				self.front = 1
				self.rear = 0
	
	def add_last(self, val):
		if self.front > self.rear:
			if self.rear == self.front-1:
				self.resize()
				self.rear += 1
				self.data[self.rear] = val
			else:
				self.rear += 1
				self.data[self.rear] = val
		elif self.rear > self.front:
			if self.rear == len(self.data)-1:
				self.resize()
				self.rear += 1
				self.data[self.rear] = val
			else:
				self.rear += 1
				self.data[self.rear] = val
		else:
			self.data.append(val)
			if (len(self) == 2):
				self.rear = 1
				self.front = 0
	
	def delete_first(self):
		if self.is_empty():
			raise Empty("double ended queue is empty")
		number = self.data[self.front]
		self.data[self.front] = None
		self.front += 1
		if self.is_empty():
			self.front = 0
			self.rear = 0
			self.data = []
		return number
	
	def delete_last(self):
		if self.is_empty():
			raise Exception("double ended queue is empty")
		number = self.data[self.rear]
		self.data[self.rear] = None
		self.rear -= 1	
		if self.is_empty():
			self.front = 0
			self.rear = 0
			self.data = []			
		return number
	
	def resize(self):
		old_data = self.data[:]
		self.data = [None] * (len(self) * 2)
		if self.front > self.rear:
			first_half = old_data[self.front:]
			second_half = old_data[:self.rear+1]
			index = 0
			for elem in first_half:
				self.data[index] = elem
				index += 1
			for elem in second_half:
				self.data[index] = elem
				index += 1
			self.front = 0
			self.rear = len(old_data)-1
		elif self.rear > self.front:
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
	
	def is_empty(self):
		return len(self) == 0

