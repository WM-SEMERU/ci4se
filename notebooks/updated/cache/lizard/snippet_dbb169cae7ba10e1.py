def h_hat(ac):
    ac = asarray_ndim(ac, 2)
    assert ac.shape[1] == 2, 'only biallelic variants supported'
    an = ac.sum(axis=1)
    x = ac[:, (0)] * ac[:, (1)] / (an * (an - 1))
    return x