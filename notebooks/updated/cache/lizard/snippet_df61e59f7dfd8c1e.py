def random_shift(x, pad=(4, 4), mode='REFLECT'):
    assert mode in 'REFLECT SYMMETRIC CONSTANT'.split()
    assert x.get_shape().ndims == 3
    xp = tf.pad(x, [[pad[0], pad[0]], [pad[1], pad[1]], [0, 0]], mode)
    return tf.random_crop(xp, tf.shape(x))