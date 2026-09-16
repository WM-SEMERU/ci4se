def ap_entropy(X, M, R):
    N = len(X)
    Em = embed_seq(X, 1, M)
    A = numpy.tile(Em, (len(Em), 1, 1))
    B = numpy.transpose(A, [1, 0, 2])
    D = numpy.abs(A - B)
    InRange = numpy.max(D, axis=2) <= R
    Cm = InRange.mean(axis=0)
    Dp = numpy.abs(numpy.tile(X[M:], (N - M, 1)) - numpy.tile(X[M:], (N - M,
        1)).T)
    Cmp = numpy.logical_and(Dp <= R, InRange[:-1, :-1]).mean(axis=0)
    Phi_m, Phi_mp = numpy.sum(numpy.log(Cm)), numpy.sum(numpy.log(Cmp))
    Ap_En = (Phi_m - Phi_mp) / (N - M)
    return Ap_En