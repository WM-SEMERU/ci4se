def dot(self, w):
    return sum([(x * y) for x, y in zip(self, w)])