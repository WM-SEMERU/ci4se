def dist(self, other):
    dx = self.x - other.x
    dy = self.y - other.y
    return math.sqrt(dx ** 2 + dy ** 2)