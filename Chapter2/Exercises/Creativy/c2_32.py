from Progression import Progression
import math

class SqrtProgression(Progression):
    def __init__(self, start = 65536):
        super().__init__(start)

    def advance(self):
        self.current = math.sqrt(self.current)