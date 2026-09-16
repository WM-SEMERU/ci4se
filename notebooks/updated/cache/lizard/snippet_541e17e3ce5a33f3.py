def makeA(laplacian_matrix):
    n = laplacian_matrix.shape[0]
    row, col = sp.sparse.triu(laplacian_matrix, k=1).nonzero()
    pairs = np.asarray((row, col)).T
    N = row.shape[0]
    A = sp.sparse.csr_matrix((np.ones(N), (np.arange(N), row)), shape=(N, n)
        ) + sp.sparse.csr_matrix((-1 * np.ones(N), (np.arange(N), col)),
        shape=(N, n))
    return A, pairs