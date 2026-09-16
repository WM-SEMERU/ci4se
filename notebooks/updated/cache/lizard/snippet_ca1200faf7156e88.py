def sp_rand(m, n, a):
    if m == 0 or n == 0:
        return spmatrix([], [], [], (m, n))
    nnz = min(max(0, int(round(a * m * n))), m * n)
    nz = matrix(random.sample(range(m * n), nnz), tc='i')
    return spmatrix(normal(nnz, 1), nz % m, matrix([int(ii) for ii in nz /
        m]), (m, n))