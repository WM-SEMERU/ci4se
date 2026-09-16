def extract_all(self):
    longmin, longmax, latmin, latmax = self.Boundary()
    sample_min, sample_max = map(int, (self.SAMPLE_FIRST_PIXEL, self.
        SAMPLE_LAST_PIXEL))
    line_min, line_max = map(int, (self.LINE_FIRST_PIXEL, self.LINE_LAST_PIXEL)
        )
    X = np.array(map(self.long_id, range(sample_min, sample_max + 1, 1)))
    Y = np.array(map(self.lat_id, range(line_min, line_max + 1, 1)))
    for i, line in enumerate(range(int(line_min), int(line_max) + 1)):
        start = (line - 1) * int(self.SAMPLE_LAST_PIXEL) + sample_min
        chunk_size = int(sample_max - sample_min)
        Za = self.array(chunk_size, start, self.bytesize)
        if i == 0:
            Z = Za
        else:
            Z = np.vstack((Z, Za))
    X, Y = np.meshgrid(X, Y)
    return X, Y, Z