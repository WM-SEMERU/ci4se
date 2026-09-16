def get_reduced_bases(lattice, method='delaunay', tolerance=1e-05):
    if method == 'niggli':
        return spg.niggli_reduce(lattice, eps=tolerance)
    else:
        return spg.delaunay_reduce(lattice, eps=tolerance)