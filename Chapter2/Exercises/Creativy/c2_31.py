from Progression import Progression

class AbsDiffProgression(Progression):
    def __init__(self, first = 2, second = 200):
        super().__init__(first)
        self._prev = abs(second - first)

    def advance(self):
        self._prev, self.current = self.current, abs(self.current - self._prev)