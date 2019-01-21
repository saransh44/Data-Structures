class Vector:

    coords = [0,0,0]

    def __init__(self, d):
        if isinstance(d, list):
            self.coords = [u for u in d]
        if isinstance(d, int):
            self.coords = [0 for u in range(d)]

    def __len__(self):
         return len(self.coords)

    def __getitem__(self, j):
         return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
         return '<' + str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(self)

    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__ (self, d):
        if isinstance(d, Vector):
            scoords = sum([a * b for a, b in zip([c for c in self.coords], [z for z in d])])
            return scoords

        if isinstance(d, int):
            newCoords = [i*d for i in self.coords]
            return newCoords

    def __rmul__(self, other):
        newCoords = [i*other for i in self.coords]
        return newCoords

    def __neg__(self):
        newCoords = [i* -1 for i in self.coords]
        return newCoords

v = Vector([0,1,3])

v1 = Vector(5)
v1[1] = 10
v1[-1] = 10
print(v1)

v2 = Vector([2, 4, 6, 8, 10])
print(v2)

u1 = v1 + v2
print(u1)

u2 = -v2
print(u2)

u3 = 3 * v2
print(u3)

u4 = v2 * 3
print(u4)

u5 = v1 * v2
print(u5)

