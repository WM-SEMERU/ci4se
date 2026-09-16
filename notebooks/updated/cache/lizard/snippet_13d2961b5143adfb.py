def check_sparsity(x, fraction=0.6):
    if not sps.issparse(x):
        return x
    n = numel(x)
    if n == 0:
        return x
    if len(x.data) / float(x) > 0.6:
        return x.toarray()
    else:
        return x