def _cholesky(self, A, **kwargs):
    if sp.sparse.issparse(A):
        diag = sp.sparse.eye(A.shape[0])
    else:
        diag = np.eye(A.shape[0])
    constraint_l2 = self._constraint_l2
    while constraint_l2 <= self._constraint_l2_max:
        try:
            L = cholesky(A, **kwargs)
            self._constraint_l2 = constraint_l2
            return L
        except NotPositiveDefiniteError:
            if self.verbose:
                warnings.warn(
                    """Matrix is not positive definite. 
Increasing l2 reg by factor of 10."""
                    , stacklevel=2)
            A -= constraint_l2 * diag
            constraint_l2 *= 10
            A += constraint_l2 * diag
    raise NotPositiveDefiniteError('Matrix is not positive \ndefinite.')