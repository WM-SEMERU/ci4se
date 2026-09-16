def block_diagonal_matrix(matrices, type=None):
    ur
    if type is None:
        type = np.float64
    sizes = [Ai.shape[0] for Ai in matrices]
    size = sum(sizes)
    symbolic = hasattr(matrices[0][0], 'subs')
    if symbolic:
        A = symzeros(size, size)
    else:
        A = np.zeros((size, size), type)
    ini = 0
    fin = 0
    for i, sizei in enumerate(sizes):
        fin += sizei
        A[ini:fin, ini:fin] = matrices[i]
        ini += sizei
    return A