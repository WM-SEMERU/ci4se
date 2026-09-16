def cvm_unif_fix1(statistic):
    args = fix1_args / statistic
    kvs = kv((0.25, 0.75, 1.25), args[:, :, (newaxis)])
    gs, hs = exp(-args) * tensordot(((1, 1, 0), (2, 3, -1)), kvs, axes=(1, 2))
    a = dot((7, 16, 7), fix1_csa * gs).sum() / statistic ** 1.5
    b = dot((1, 0, 24), fix1_csb * hs).sum() / statistic ** 2.5
    return cvm_unif_inf(statistic) / 12 - a - b