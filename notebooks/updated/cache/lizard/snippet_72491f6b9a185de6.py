def ndiag_mc(funcs, S: int, Fmu, Fvar, logspace: bool=False, epsilon=None, **Ys
    ):
    N, D = tf.shape(Fmu)[0], tf.shape(Fvar)[1]
    if epsilon is None:
        epsilon = tf.random_normal((S, N, D), dtype=settings.float_type)
    mc_x = Fmu[(None), :, :] + tf.sqrt(Fvar[(None), :, :]) * epsilon
    mc_Xr = tf.reshape(mc_x, (S * N, D))
    for name, Y in Ys.items():
        D_out = tf.shape(Y)[1]
        mc_Yr = tf.tile(Y[None, ...], [S, 1, 1])
        Ys[name] = tf.reshape(mc_Yr, (S * N, D_out))

    def eval_func(func):
        feval = func(mc_Xr, **Ys)
        feval = tf.reshape(feval, (S, N, -1))
        if logspace:
            log_S = tf.log(tf.cast(S, settings.float_type))
            return tf.reduce_logsumexp(feval, axis=0) - log_S
        else:
            return tf.reduce_mean(feval, axis=0)
    if isinstance(funcs, Iterable):
        return [eval_func(f) for f in funcs]
    else:
        return eval_func(funcs)