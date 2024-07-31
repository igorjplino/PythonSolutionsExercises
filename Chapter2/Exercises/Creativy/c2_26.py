class ReversedSequenceIterator:
    def __init__(self, sequence):
        self.seq = sequence
        self.k = len(sequence)

    def __next__(self):
        self.k -= 1
        if self.k >= 0:
            return self.seq[self.k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self
    
if __name__ == "__main__":
    seq = [1, 2, 3]
    rev = ReversedSequenceIterator(seq)

    print(seq)
    for s in rev:
        print(s)