def find_bright_peaks(self, data, threshold=None, sigma=5, radius=5):
    if threshold is None:
        threshold = self.get_threshold(data, sigma=sigma)
        self.logger.debug('threshold defaults to %f (sigma=%f)' % (
            threshold, sigma))
    data_max = filters.maximum_filter(data, radius)
    maxima = data == data_max
    diff = data_max > threshold
    maxima[diff == 0] = 0
    labeled, num_objects = ndimage.label(maxima)
    slices = ndimage.find_objects(labeled)
    peaks = []
    for dy, dx in slices:
        xc = (dx.start + dx.stop - 1) / 2.0
        yc = (dy.start + dy.stop - 1) / 2.0
        peaks.append((xc, yc))
    self.logger.debug('peaks=%s' % str(peaks))
    return peaks