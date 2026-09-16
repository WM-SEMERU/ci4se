def normnorm(self):
    n = self.norm()
    return V2(-self.y / n, self.x / n)