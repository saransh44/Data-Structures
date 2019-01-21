# The	__init__ method	should	run	in	linear	expected	time. That	is	if	there	are	n
# words	in	the	file,	the	initialization	should	take	in	Θ(�) expected	time	(averagecase).
# 2. The	indices method	should	run	in	Θ(1) expected	time	(average-case).
import random
import re

class UnsortedArrayMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("Key Error: " + str(key))

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key

    def existsintable(self, key):
        for item in self.table:
            if key == item.key:
                return True
        return False

class ChainingHashTableMap:

    def __init__(self, N=64, p=6460101079):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n


    def __getitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key]

    def exists(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            return False
        else:
            return curr_bucket.existsintable(key)

    def __setitem__(self, key, value):
        j = self.hash_function(key)
        if self.table[j] is None:
            self.table[j] = UnsortedArrayMap()
        old_size = len(self.table[j])
        self.table[j][key] = value
        new_size = len(self.table[j])
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        del curr_bucket[key]
        self.n -= 1
        if (curr_bucket.is_empty()):
            self.table[j] = None
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                for key in curr_bucket:
                    yield key

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value


class InvertedFile:
    def __init__(self, file_name):
        self.f = open(file_name)
        self.alltext = self.f.read().lower()
        self.words = re.sub("[^\w]", " ",  self.alltext).split()
        self.ind = ChainingHashTableMap()

        for i in range(len(self.words)):
            if self.ind.exists(self.words[i]):
                self.ind[self.words[i]].append(i)
            else:
                self.ind[self.words[i]] = [i]

    def indices(self, key):
        return self.ind[key]

    def __str__(self):
        return self.f.read().lower()

    def __repr__(self):
        print(self.f.read())

    def readline(self):
        return self.f.readline()

    def toArray(self):

        result = []

        for line in self.f:
            result.append(self.readline())

        print(result)

    def readLineByLine(self):
        for line in self.f:
            print(line)

    def printwords(self):
        print(self.words)


# file = InvertedFile("test.txt")
#
#
# file.printwords()
# print(file.indices("row"))
# print(file.readline())
# s = file.f.read()

# file.toArray()
# file.readLineByLine()

