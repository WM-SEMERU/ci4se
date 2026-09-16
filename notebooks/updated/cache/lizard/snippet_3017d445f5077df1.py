def rank(matrix, atol=1e-13, rtol=0):
    matrix = np.atleast_2d(matrix)
    sigma = svd(matrix, compute_uv=False)
    tol = max(atol, rtol * sigma[0])
    return int((sigma >= tol).sum())