def _get_stddevs(self, C, stddev_types, num_sites):
    assert all(stddev_type in self.DEFINED_FOR_STANDARD_DEVIATION_TYPES for
        stddev_type in stddev_types)
    stddevs = [0.26 / np.log10(np.e) + np.zeros(num_sites)]
    return stddevs