from Vector import Vector

class Vector_radd(Vector):
    def __init__(self, d):
        super().__init__(d)

    def __radd__(self, other):
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result