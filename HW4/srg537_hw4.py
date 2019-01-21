import ctypes  # provides low-level arrays

def split_by_sign(lst,low,high):
    if low == high:
        if lst[low] < 0:
            lst.insert(0,lst.pop(low))
            return lst
        else:
            lst.append(lst.pop(low))
            return lst

    else:
        if lst[low] < 0:
            lst.insert(0,lst.pop(low))
        else:
            lst.append(lst.pop(low))

    return split_by_sign(lst, low+1, high)


print(split_by_sign([-1,2,-3,4,-5], 0,4))


def permutations(lst, low, high):
    # print(lst)
    lst1 = lst[:]
    lst2 = []
    if (low == high):
        # lst = lst.reverse()
        # print(lst)
        return [lst]
    else:
        for i in range(high+1):
            # print (i)
            if i != low:
                lst1 = lst[:]


                lst1[high-i], lst1[i] = lst1[i], lst1[high-i]
                # print("list1: ", lst1)

                lst2.append(lst1)
                # print(lst2)
        return lst2 + permutations(lst, low+1, high)

# lst = [1,2,3, 4,5]
# print(permutations(lst, 0, 4))

def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size


    def extend(self, other):
        for elem in other:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        return self.data[ind]


    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        self.data[ind] = val

    def __str__(self):
        string = ""
        for i in range(self.n - 1):
            string += str(self.data[i]) + ", "
        string += str(self.data[self.n - 1])
        return "[" + string + "]"

    def __repr__(self):
        return str(self)

    def insert(self, index, val):
        if (not (0 <= index <= self.n - 1)):
            raise IndexError('invalid index')
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = self.data[self.n -1]
        self.n += 1

        for i in range(self.n, index, -1):
            self.data[i] = self.data[i-1]

        self[index] = val


    def pop(self):
        if not self:
            raise IndexError('invalid index')
        else:
            # print (self.data[self.n])

            i = self.data[self.n-1]
            self.data[self.n-1]  = None
            self.n = self.n-1
        return i

    # PopExtraCredit
    def popExtraCredit(self, index):
        if not self:
            raise IndexError('invalid index')
        else:
            value = self.data[index]
            for i in range(index, self.n, 1):
                self.data[i] = self.data[i+1]
            self.n = self.n-1
        return value


lst = MyList()
for i  in range(5):
    lst.append(i)

print(lst.pop())
print(lst)
# lst.insert(1,30)
# print(lst)
#
# v = lst.popExtraCredit(1)
# print("lstAfterPop: ", lst)
# print(v)

def find_duplicates(lst):
    a = dict()
    temp = []
    for i in lst:
        if (a.get(i)):
            a[i] +=1
            temp.append(i)
        else:
            # d1 = {i:1}
            a[i] = 1

    return temp

print(find_duplicates([1,2,1,2,4,3,4]))

# 5B
def remove_all(lst, value):
    end = None
    for i in range(len(lst)):
        if lst[i] == value:
                end = i
        else:
            if end != None:
                lst[i], lst[end] = lst[end], lst[i]
                end += 1

    for i in range(len(lst)-1,0, -1):
        if lst[i] == value:
            lst.pop()

    return lst
print(remove_all([5,2,4,5],5))

a = [1,2,3]
b = [2,4,6]

# print([c for y in a if y in b])

