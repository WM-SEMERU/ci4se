def _py_func_with_gradient(func, inp, Tout, stateful=True, name=None,
    grad_func=None):
    rnd_name = 'PyFuncGrad-' + '%0x' % getrandbits(30 * 4)
    tf.RegisterGradient(rnd_name)(grad_func)
    g = tf.get_default_graph()
    with g.gradient_override_map({'PyFunc': rnd_name, 'PyFuncStateless':
        rnd_name}):
        return tf.py_func(func, inp, Tout, stateful=stateful, name=name)