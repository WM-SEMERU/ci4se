def unfolding(tens, i):
    return reshape(tens.full(), (np.prod(tens.n[0:i + 1]), -1))