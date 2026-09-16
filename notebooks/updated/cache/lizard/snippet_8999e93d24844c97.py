def is_same_nick(self, left, right):
    return self.normalize(left) == self.normalize(right)