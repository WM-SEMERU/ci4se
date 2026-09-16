def svd_entropy(X, Tau, DE, W=None):
    if W is None:
        Y = embed_seq(X, Tau, DE)
        W = numpy.linalg.svd(Y, compute_uv=0)
        W /= sum(W)
    return -1 * sum(W * numpy.log(W))