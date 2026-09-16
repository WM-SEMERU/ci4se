def discriminator2(ndf, no_bias=True, fix_gamma=True, eps=1e-05 + 1e-12):
    BatchNorm = mx.sym.BatchNorm
    data = mx.sym.Variable('data')
    label = mx.sym.Variable('label')
    d4 = mx.sym.Convolution(data, name='d4', kernel=(5, 5), stride=(2, 2),
        pad=(2, 2), num_filter=ndf * 8, no_bias=no_bias)
    dbn4 = BatchNorm(d4, name='dbn4', fix_gamma=fix_gamma, eps=eps)
    dact4 = mx.sym.LeakyReLU(dbn4, name='dact4', act_type='leaky', slope=0.2)
    h = mx.sym.Flatten(dact4)
    d5 = mx.sym.FullyConnected(h, num_hidden=1, name='d5')
    dloss = mx.sym.LogisticRegressionOutput(data=d5, label=label, name='dloss')
    return dloss