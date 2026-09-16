def _rand_sparse(m, n, density, format='csr'):
    nnz = max(min(int(m * n * density), m * n), 0)
    row = np.random.randint(low=0, high=m - 1, size=nnz)
    col = np.random.randint(low=0, high=n - 1, size=nnz)
    data = np.ones(nnz, dtype=float)
    return sp.sparse.csr_matrix((data, (row, col)), shape=(m, n))