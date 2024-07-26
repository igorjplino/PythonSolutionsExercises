from Sequence import Sequence

class Sequence_lt(Sequence):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, j):
        return self._data[j]

    def __lt__(self, other):
        for a, b in zip(self, other):
            if a != b:
                return a < b
        return len(self) < len(other)