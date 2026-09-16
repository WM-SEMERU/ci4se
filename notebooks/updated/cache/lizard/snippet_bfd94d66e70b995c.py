def sg_squeeze(tensor, opt):
    r
    opt += tf.sg_opt(axis=[-1])
    opt.axis = opt.axis if isinstance(opt.axis, (tuple, list)) else [opt.axis]
    return tf.squeeze(tensor, opt.axis, name=opt.name)