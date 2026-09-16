def resolution(self):
    geo_coords = self.to_geographic()
    resolution = abs(_initialresolution * math.cos(geo_coords.lat * _pi_180
        ) / 2 ** self.zoom)
    return resolution