from Chapter2.Vector import Vector

class Vector_mul(Vector):
    def __init__(self, d):
        super().__init__(d)

    def __mul__(self, val):
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] * val
        return result