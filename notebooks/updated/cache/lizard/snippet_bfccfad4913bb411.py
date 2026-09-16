def get_tile_gid(self, x, y, layer):
    try:
        assert x >= 0 and y >= 0 and layer >= 0
    except AssertionError:
        raise ValueError
    try:
        return self.layers[int(layer)].data[int(y)][int(x)]
    except (IndexError, ValueError):
        msg = 'Coords: ({0},{1}) in layer {2} is invalid'
        logger.debug(msg, (x, y, layer))
        raise ValueError