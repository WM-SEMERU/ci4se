def setGamma(self, x):
    if x != self.gamma:
        self.gamma = x
        self.refresh = True