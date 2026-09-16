def main(self, c):
    phase = Sfix(0.0, 0, -17)
    abs, _, angle = self.core.main(c.real, c.imag, phase)
    self.y_abs = abs * (1.0 / 1.64676)
    self.y_angle = angle
    return self.y_abs, self.y_angle