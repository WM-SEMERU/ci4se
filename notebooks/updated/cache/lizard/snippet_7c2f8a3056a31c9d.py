def _get_stddevs(self, C, stddev_types, mag, num_sites):
    stddevs = []
    for _ in stddev_types:
        if mag < 7.16:
            sigma = C['c11'] + C['c12'] * mag
        elif mag >= 7.16:
            sigma = C['c13']
        stddevs.append(np.zeros(num_sites) + sigma)
    return stddevs