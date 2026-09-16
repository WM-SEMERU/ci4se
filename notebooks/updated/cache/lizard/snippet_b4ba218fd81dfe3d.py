def overlap(self, other, method='fraction'):
    checkopts(method, ['fraction', 'rates'])
    coords_self = self.coordinates.tolist()
    coords_other = other.coordinates.tolist()
    intersection = [a for a in coords_self if a in coords_other]
    nhit = float(len(intersection))
    ntotal = float(len(set([tuple(x) for x in coords_self] + [tuple(x) for
        x in coords_other])))
    if method == 'rates':
        recall = nhit / len(coords_self)
        precision = nhit / len(coords_other)
        return recall, precision
    if method == 'fraction':
        return nhit / float(ntotal)