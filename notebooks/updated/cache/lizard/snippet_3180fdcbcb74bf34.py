def derivativeX(self, x, y):
    xShift = self.lowerBound(y)
    dfdx_out = self.func.derivativeX(x - xShift, y)
    return dfdx_out