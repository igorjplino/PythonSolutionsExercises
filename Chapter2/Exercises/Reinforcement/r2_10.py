from Chapter2.Vector import Vector

class Vector_neg(Vector):
    def __init__(self, d):
        super().__init__(d)

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result