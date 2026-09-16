def KLDivergenceLoss():
    data = mx.sym.Variable('data')
    mu1, lv1 = mx.sym.split(data, num_outputs=2, axis=0)
    mu2 = mx.sym.zeros_like(mu1)
    lv2 = mx.sym.zeros_like(lv1)
    v1 = mx.sym.exp(lv1)
    v2 = mx.sym.exp(lv2)
    mu_diff_sq = mx.sym.square(mu1 - mu2)
    dimwise_kld = 0.5 * (lv2 - lv1 + mx.symbol.broadcast_div(v1, v2) + mx.
        symbol.broadcast_div(mu_diff_sq, v2) - 1.0)
    KL = mx.symbol.sum(dimwise_kld, axis=1)
    KLloss = mx.symbol.MakeLoss(mx.symbol.mean(KL), name='KLloss')
    return KLloss