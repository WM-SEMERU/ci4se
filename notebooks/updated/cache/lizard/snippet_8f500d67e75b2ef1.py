def sort_matrix(a, n=0):
    a = _n.array(a)
    return a[:, (a[(n), :].argsort())]