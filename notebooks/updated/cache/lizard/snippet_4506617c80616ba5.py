def pointIsInTriangle(p, p1, p2, p3):
    p = np.array(p)
    u = np.array(p2) - p1
    v = np.array(p3) - p1
    n = np.cross(u, v)
    w = p - p1
    ln = np.dot(n, n)
    if not ln:
        return True
    gamma = np.dot(np.cross(u, w), n) / ln
    beta = np.dot(np.cross(w, v), n) / ln
    alpha = 1 - gamma - beta
    if 0 < alpha < 1 and 0 < beta < 1 and 0 < gamma < 1:
        return True
    return False