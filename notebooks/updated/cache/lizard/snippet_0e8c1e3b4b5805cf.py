def sg_densenet_layer(x, opt):
    r
    assert opt.dim is not None, 'dim is mandatory.'
    assert opt.num is not None, 'num is mandatory.'
    opt += tf.sg_opt(stride=1, act='relu', trans=True)

    def cname(index):
        return opt.name if opt.name is None else opt.name + '_%d' % index
    with tf.sg_context(bias=False, reuse=opt.reuse):
        out = x
        for i in range(opt.num):
            out_new = out.sg_bypass(act=opt.act, bn=True, name=cname(3 * i + 1)
                ).sg_conv(dim=opt.dim // 4, size=1, act=opt.act, bn=True,
                name=cname(3 * i + 2)).sg_conv(dim=opt.dim, size=3, name=
                cname(3 * i + 3))
            out = tf.concat([out_new, out], 3)
        if opt.trans:
            out = out.sg_bypass(act=opt.act, bn=True, name=cname(3 * i + 4)
                ).sg_conv(size=1, name=cname(3 * i + 5)).sg_pool(avg=True)
    return out