def obj(x):
    j = np.arange(1, 6)
    tmp1 = np.dot(j, np.cos((j + 1) * x[0] + j))
    tmp2 = np.dot(j, np.cos((j + 1) * x[1] + j))
    return tmp1 * tmp2