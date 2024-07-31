from Range import Range

class Range_Contains(Range):
    def __init__(self, start, stop = None, step = 1):
        super().__init__(start, stop, step)

    def __contains__(self, k):
        quotient, remainder = divmod((k - self.start), self.step)
        
        if remainder == 0: 
            return 0 <= quotient  < len(self) # Check if factor is within valid range
        
        return False