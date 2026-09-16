def linsys(x0, rho, P, q):
    return np.linalg.solve(rho * np.eye(q.shape[0]) + P, rho * x0.copy() + q)