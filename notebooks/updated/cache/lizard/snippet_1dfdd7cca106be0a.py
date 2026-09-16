def mirror(self, axes='x', inplace=False):
    state = Polygon.verify
    Polygon.verify = False
    mirror = np.ones(3)
    if 'x' in axes:
        mirror *= np.array([-1, 1, 1])
    if 'y' in axes:
        mirror *= np.array([1, -1, 1])
    if 'z' in axes:
        mirror *= np.array([1, 1, -1])
    map_ = self.get_map()[1] * mirror
    space = self.map2pyny(map_)
    Polygon.verify = state
    if inplace:
        self.add_spaces(space)
        return None
    else:
        return space