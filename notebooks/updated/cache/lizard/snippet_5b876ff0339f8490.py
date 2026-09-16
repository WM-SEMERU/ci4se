def get_floating_spinning_factors(self):
    data = []
    for src in self.get_sources():
        if hasattr(src, 'hypocenter_distribution'):
            data.append((len(src.hypocenter_distribution.data), len(src.
                nodal_plane_distribution.data)))
    if not data:
        return numpy.array([1, 1])
    return numpy.array(data).mean(axis=0)