def forget_xy(t):
    shape = t.shape[0], None, None, t.shape[3]
    return tf.placeholder_with_default(t, shape)