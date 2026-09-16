def _eigsorted(cov, asc=True):
    eigval, eigvec = np.linalg.eigh(cov)
    order = eigval.argsort()
    if not asc:
        order = order[::-1]
    return eigval[order], eigvec[:, (order)]