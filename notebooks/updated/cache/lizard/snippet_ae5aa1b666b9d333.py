def one_over_x_like(x):
    if np.any(x < 0):
        return -np.Inf
    else:
        return -np.sum(np.log(x))