def get_signs(M, cutoff=1e-10, validate=True, ambiguous=True):
    assert is_symmetric(M), 'the matrix is not symmetric:\n{0}'.format(str(M))
    N, x = M.shape
    w, v = np.linalg.eigh(M)
    m = np.argmax(w)
    mv = v[:, (m)]
    f = lambda x: x if abs(x) > cutoff else 0
    mv = [f(x) for x in mv]
    sign_array = np.array(np.sign(mv), dtype=int)
    if np.sum(sign_array) < 0:
        sign_array = -sign_array
    if validate:
        diag = np.matrix(np.eye(N, dtype=int) * sign_array)
        final = diag * M * diag
        assert (final >= 0).all(), 'result check fails:\n{0}'.format(final)
    if not ambiguous:
        sign_array[sign_array == 0] = 1
    return sign_array