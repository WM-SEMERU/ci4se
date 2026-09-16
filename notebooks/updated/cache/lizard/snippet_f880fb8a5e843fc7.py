def get_children(self):
    next_zoom = self.zoom + 1
    return [self.tile_pyramid.tile(next_zoom, self.row * 2 + row_offset, 
        self.col * 2 + col_offset) for row_offset, col_offset in [(0, 0), (
        0, 1), (1, 1), (1, 0)] if all([self.row * 2 + row_offset < self.tp.
        matrix_height(next_zoom), self.col * 2 + col_offset < self.tp.
        matrix_width(next_zoom)])]