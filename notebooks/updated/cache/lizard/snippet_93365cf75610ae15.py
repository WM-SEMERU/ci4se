def rotate(self, angle, direction='z', axis=None):
    state = Polygon.verify
    Polygon.verify = False
    if axis is None:
        axis = self.get_centroid()
    elif len(axis) == 2:
        axis = np.array([axis[0], axis[1], 0])
    map_ = self.get_map()[1] - axis
    c = np.cos(angle)
    s = np.sin(angle)
    if direction == 'z':
        R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    elif direction == 'y':
        R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    elif direction == 'x':
        R = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    rotated_ = np.dot(R, map_.T).T
    map_ = rotated_ + axis
    space = self.map2pyny(map_)
    Polygon.verify = state
    return space