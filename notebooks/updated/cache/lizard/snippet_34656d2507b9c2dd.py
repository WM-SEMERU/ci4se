def combine_first_two_dimensions(x):
    ret = tf.reshape(x, tf.concat([[-1], common_layers.shape_list(x)[2:]], 0))
    old_shape = x.get_shape().dims
    a, b = old_shape[:2]
    new_shape = [a * b if a and b else None] + old_shape[2:]
    ret.set_shape(new_shape)
    return ret