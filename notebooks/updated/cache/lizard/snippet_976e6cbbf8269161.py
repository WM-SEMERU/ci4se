def linear_interpolate_rank(tensor1, tensor2, coeffs, rank=1):
    _, _, _, num_channels = common_layers.shape_list(tensor1)
    diff_sq_sum = tf.reduce_sum((tensor1 - tensor2) ** 2, axis=(0, 1, 2))
    _, feature_ranks = tf.math.top_k(diff_sq_sum, k=rank)
    feature_rank = feature_ranks[-1]
    channel_inds = tf.range(num_channels, dtype=tf.int32)
    channel_mask = tf.equal(channel_inds, feature_rank)
    ones_t = tf.ones(num_channels, dtype=tf.float32)
    zeros_t = tf.zeros(num_channels, dtype=tf.float32)
    interp_tensors = []
    for coeff in coeffs:
        curr_coeff = tf.where(channel_mask, coeff * ones_t, zeros_t)
        interp_tensor = tensor1 + curr_coeff * (tensor2 - tensor1)
        interp_tensors.append(interp_tensor)
    return tf.concat(interp_tensors, axis=0)