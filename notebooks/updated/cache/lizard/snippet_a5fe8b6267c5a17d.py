def layer_norm_compute(x, epsilon, scale, bias, layer_collection=None):
    params = scale, bias
    epsilon, scale, bias = [cast_like(t, x) for t in [epsilon, scale, bias]]
    mean = tf.reduce_mean(x, axis=[-1], keepdims=True)
    variance = tf.reduce_mean(tf.squared_difference(x, mean), axis=[-1],
        keepdims=True)
    norm_x = (x - mean) * tf.rsqrt(variance + epsilon)
    output = norm_x * scale + bias
    return output