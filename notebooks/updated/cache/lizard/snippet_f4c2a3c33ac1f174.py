def get_kabsch_rotation(Q, P):
    A = np.dot(np.transpose(P), Q)
    V, S, W = np.linalg.svd(A)
    W = W.T
    d = np.linalg.det(np.dot(W, V.T))
    return np.linalg.multi_dot((W, np.diag([1.0, 1.0, d]), V.T))