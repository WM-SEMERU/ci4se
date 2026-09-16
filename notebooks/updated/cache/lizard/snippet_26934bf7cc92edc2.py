def similarity(self, other):
    if self.magnitude == 0 or other.magnitude == 0:
        return 0
    return self.dot(other) / self.magnitude