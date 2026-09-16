def fit(self, bbox, max_zoom=MAX_ZOOM, force_zoom=None):
    BUFFER_FACTOR = 1.1
    if force_zoom is not None:
        self.zoom = force_zoom
    else:
        for zoom in range(max_zoom, MIN_ZOOM - 1, -1):
            self.zoom = zoom
            left, top = self.lonlat_to_screen([bbox.west], [bbox.north])
            right, bottom = self.lonlat_to_screen([bbox.east], [bbox.south])
            if (top - bottom < SCREEN_H * BUFFER_FACTOR and right - left < 
                SCREEN_W * BUFFER_FACTOR):
                break
    west_tile, north_tile = self.deg2num(bbox.north, bbox.west, self.zoom)
    east_tile, south_tile = self.deg2num(bbox.south, bbox.east, self.zoom)
    self.xtile = west_tile - self.tiles_horizontally / 2.0 + (east_tile -
        west_tile) / 2
    self.ytile = north_tile - self.tiles_vertically / 2.0 + (south_tile -
        north_tile) / 2
    self.calculate_viewport_size()