def exp_comp_(t, alpha=1, beta=1):
    return beta * (1 - np.exp(-alpha * np.maximum(0, t - 10 * beta)))