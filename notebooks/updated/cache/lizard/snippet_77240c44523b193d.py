def glb(self, other):
    return self.__class__([min(self.lower, other.lower), min(self.upper,
        other.upper)], lower_inc=self.lower_inc if self < other else other.
        lower_inc, upper_inc=self.upper_inc if self > other else other.
        upper_inc)