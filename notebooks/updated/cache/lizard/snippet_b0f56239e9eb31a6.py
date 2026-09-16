def multiplyC(self, alpha):
    self.C *= alpha
    if self.dC is not self.C:
        self.dC *= alpha
    self.D *= alpha ** 0.5