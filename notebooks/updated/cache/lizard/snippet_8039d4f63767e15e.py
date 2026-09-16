def move(self, point, reverse=False):
    if reverse:
        point = [(-1 * i) for i in point]
    return Box(self.x + point[0], self.y + point[1], self.width, self.height)