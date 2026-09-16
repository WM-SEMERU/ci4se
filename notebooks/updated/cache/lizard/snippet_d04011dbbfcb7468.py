def _pairs_to_np(self, pairlist, dim):
    mat = np.zeros((dim, dim + 1))
    for line in pairlist:
        i = int(line[0]) - 1
        j = int(line[1]) - 1
        prob = float(line[2])
        mat[i, j] = prob
    return mat