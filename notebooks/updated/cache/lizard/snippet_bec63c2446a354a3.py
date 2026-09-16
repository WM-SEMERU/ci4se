def softplus(x, scale=1.0, name=None):
    if scale == 1:
        return tf.nn.softplus(x)
    else:
        with tf.name_scope(name, 'softplus', [x]):
            scale = tf.convert_to_tensor(scale, dtype=x.dtype.base_dtype)
            return tf.nn.softplus(x * scale) / scale