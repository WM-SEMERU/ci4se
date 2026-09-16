def apply_to(self, A):
    if A.ndim == 1:
        A = np.expand_dims(A, axis=0)
    rows, cols = A.shape
    A_new = np.hstack([A, np.ones((rows, 1))])
    A_new = np.transpose(self.T.dot(np.transpose(A_new)))
    return A_new[:, 0:cols]