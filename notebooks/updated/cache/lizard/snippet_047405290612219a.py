def average(self, projection=None):
    length = self.size()
    if projection:
        return sum(self.map(projection)) / length
    else:
        return sum(self) / length