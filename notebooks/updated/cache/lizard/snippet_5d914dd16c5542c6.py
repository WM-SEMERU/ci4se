def setActivations(self, value):
    Numeric.put(self.activation, Numeric.arange(len(self.activation)), value)
    self.activationSet = 1