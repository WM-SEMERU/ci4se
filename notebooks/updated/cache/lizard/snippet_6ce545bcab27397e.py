def tan_rand(q, seed=9):
    rs = np.random.RandomState(seed)
    rvec = rs.rand(q.shape[0])
    qd = np.cross(rvec, q)
    qd = qd / np.linalg.norm(qd)
    while np.dot(q, qd) > 1e-06:
        rvec = rs.rand(q.shape[0])
        qd = np.cross(rvec, q)
        qd = qd / np.linalg.norm(qd)
    return qd