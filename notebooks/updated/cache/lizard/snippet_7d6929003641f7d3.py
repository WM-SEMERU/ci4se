def doublec(self, j):
    if j < self.k0 + 1:
        return 0
    if self.b[j] != self.b[j - 1]:
        return 0
    return self.cons(j)