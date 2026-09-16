def _set_scale(self, value):
    sx, sxy, syx, sy, ox, oy = self.transformation
    sx, sy = value
    self.transformation = sx, sxy, syx, sy, ox, oy