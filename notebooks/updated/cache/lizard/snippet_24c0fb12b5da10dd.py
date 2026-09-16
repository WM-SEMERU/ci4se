def project_sequence(s, permutation=None):
    xs, ys = unzip([project_point(p, permutation=permutation) for p in s])
    return xs, ys