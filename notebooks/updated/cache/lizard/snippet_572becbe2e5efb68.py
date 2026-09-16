def poisson_dist(p1, p2):
    p1_ = p1 + eps
    p2_ = p2 + eps
    return np.dot(p1_ - p2_, np.log(p1_ / p2_))