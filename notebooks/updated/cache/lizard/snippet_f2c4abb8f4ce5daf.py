def _pseudoinverse(self, A, tol=1e-10):
    return np.linalg.pinv(A, rcond=tol)