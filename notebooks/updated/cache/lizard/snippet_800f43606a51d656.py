def angle2d(self):
    if self.x == 0:
        if self.y < 0:
            return math.pi / 2.0 * 3
        elif self.y > 0:
            return math.pi / 2.0
        else:
            return 0
    elif self.y == 0:
        if self.x < 0:
            return math.pi
        else:
            return 0
    ans = math.atan(self.y / self.x)
    if self.x > 0:
        if self.y > 0:
            return ans
        else:
            return ans + math.pi * 2.0
    else:
        return ans + math.pi