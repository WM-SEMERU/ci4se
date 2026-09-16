def tile_height(self, zoom):
    warnings.warn(DeprecationWarning('tile_height is deprecated'))
    validate_zoom(zoom)
    matrix_pixel = 2 ** zoom * self.tile_size * self.grid.shape.height
    tile_pixel = self.tile_size * self.metatiling
    return matrix_pixel if tile_pixel > matrix_pixel else tile_pixel