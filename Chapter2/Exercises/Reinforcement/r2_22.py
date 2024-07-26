from Sequence import Sequence

class Sequence_eq(Sequence):
    def __len__(self):
        return len(self)

    def __getitem__(self, j):
        return self[j]

    def __eq__(self, other):
        if (len(self) != len(other)):
            return False
        return self == other