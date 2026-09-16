def splay(vec):
    N2 = 2 ** int(numpy.log2(len(vec)) / 2)
    N1 = len(vec) / N2
    return N1, N2