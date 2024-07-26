from FibonacciProgression import FibonacciProgression

class FibonacciProgression_FindPosition:
    def __init__(self):
        self.fibonacci = FibonacciProgression(2, 2)

    def find_value_position(self, p):
        self.fibonacci.print_progression(p)