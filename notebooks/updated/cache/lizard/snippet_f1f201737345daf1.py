def _relative_position_to_absolute_position_masked(x):
    batch, heads, length, _ = common_layers.shape_list(x)
    x = tf.pad(x, [[0, 0], [0, 0], [0, 0], [1, 0]])
    x = tf.reshape(x, [batch, heads, 1 + length, length])
    x = tf.slice(x, [0, 0, 1, 0], [-1, -1, -1, -1])
    return x