def sg_concat(tensor, opt):
    r
    assert opt.target is not None, 'target is mandatory.'
    opt += tf.sg_opt(axis=tensor.get_shape().ndims - 1)
    target = opt.target if isinstance(opt.target, (tuple, list)) else [opt.
        target]
    return tf.concat([tensor] + target, opt.axis, name=opt.name)