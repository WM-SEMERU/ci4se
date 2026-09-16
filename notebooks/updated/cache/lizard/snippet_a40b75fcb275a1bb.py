def uniform_spacings(N):
    z = np.cumsum(-np.log(random.rand(N + 1)))
    return z[:-1] / z[-1]