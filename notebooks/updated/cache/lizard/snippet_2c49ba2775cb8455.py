def scaleField(self, scalingFactor):
    self.B = self.B._replace(val=self.B.val * scalingFactor)