def unit(w, sparsity):
    w_shape = common_layers.shape_list(w)
    count = tf.to_int32(w_shape[-1] * sparsity)
    mask = common_layers.unit_targeting(w, count)
    return (1 - mask) * w