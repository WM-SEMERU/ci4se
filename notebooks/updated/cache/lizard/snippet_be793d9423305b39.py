def control_force(self, c):
    g = self.g
    s = self.s
    return g * (2 / π) * arctan(s / g * c)