def get_y(self, var, coords=None):
    coords = coords or self.ds.coords
    coord = self.get_variable_by_axis(var, 'y', coords)
    if coord is not None:
        return coord
    return coords.get(self.get_yname(var))