def get_stddevs(self, mag, imt, stddev_types, num_sites):
    stddevs = []
    for stddev_type in stddev_types:
        assert stddev_type in self.DEFINED_FOR_STANDARD_DEVIATION_TYPES
        if stddev_type == const.StdDev.TOTAL:
            sigma = self._get_total_sigma(imt, mag)
            stddevs.append(sigma + np.zeros(num_sites))
    return stddevs