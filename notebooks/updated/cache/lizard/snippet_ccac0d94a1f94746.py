def dot_product(t1, t2, keep_dims=False, name=None, reduction_dim=None):
    with tf.name_scope(name, 'dot', [t1, t2]) as scope:
        t1 = tf.convert_to_tensor(t1, name='t1')
        t2 = tf.convert_to_tensor(t2, name='t2')
        mul = tf.multiply(t1, t2)
        if not reduction_dim:
            reduction_dim = _last_index(mul, 1)
        return tf.reduce_sum(mul, reduction_dim, name=scope, keep_dims=
            keep_dims)