def remove(self, dist):
    while dist.location in self.paths:
        self.paths.remove(dist.location)
        self.dirty = True
    Environment.remove(self, dist)