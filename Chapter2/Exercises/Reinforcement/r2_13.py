from Chapter2.Vector import Vector

class Vector_rmul(Vector):
    def __init__(self, d):
        super().__init__(d)

    def __rmul__(self, val):
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] * val
        return result