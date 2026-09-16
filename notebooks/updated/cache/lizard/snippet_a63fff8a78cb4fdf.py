def center(self):
    bounds = self.bounds
    x = (bounds[1] + bounds[0]) / 2
    y = (bounds[3] + bounds[2]) / 2
    z = (bounds[5] + bounds[4]) / 2
    return [x, y, z]