def _get_stddevs(self, C, stddev_types, num_sites):
    stddevs = []
    for stddev_type in stddev_types:
        assert stddev_type in self.DEFINED_FOR_STANDARD_DEVIATION_TYPES
        stddevs.append(np.log(10 ** C['sigma']) + np.zeros(num_sites))
    return stddevs