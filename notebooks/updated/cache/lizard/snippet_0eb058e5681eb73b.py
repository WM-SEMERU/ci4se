def between(self, left, right):
    crit = lambda x: left <= x < right
    return self.select(crit)