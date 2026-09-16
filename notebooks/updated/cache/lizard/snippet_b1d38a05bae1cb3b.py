def sg_train(**kwargs):
    r
    opt = tf.sg_opt(kwargs)
    assert opt.loss is not None, 'loss is mandatory.'
    opt += tf.sg_opt(optim='MaxProp', lr=0.001, beta1=0.9, beta2=0.99,
        category='', ep_size=100000)
    train_op = sg_optim(opt.loss, optim=opt.optim, lr=0.001, beta1=opt.
        beta1, beta2=opt.beta2, category=opt.category)
    loss_ = opt.loss
    if isinstance(opt.loss, (tuple, list)):
        loss_ = opt.loss[0]

    @sg_train_func
    def train_func(sess, arg):
        return sess.run([loss_, train_op])[0]
    train_func(**opt)