def long_id(self, sample):
    if self.grid == 'WAC':
        lon = self.CENTER_LONGITUDE + (sample - self.
            SAMPLE_PROJECTION_OFFSET - 1) * self.MAP_SCALE * 0.001 / (self.
            A_AXIS_RADIUS * np.cos(self.CENTER_LATITUDE * np.pi / 180.0))
        return lon * 180 / np.pi
    else:
        lon = float(self.CENTER_LONGITUDE) + (sample - float(self.
            SAMPLE_PROJECTION_OFFSET) - 1) / float(self.MAP_RESOLUTION)
        return lon