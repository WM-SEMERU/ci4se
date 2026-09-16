def rotateZ(self, angle, axis_point=(0, 0, 0), rad=False):
    if rad:
        angle *= 57.29578
    self.RotateZ(angle)
    if self.trail:
        self.updateTrail()
    return self