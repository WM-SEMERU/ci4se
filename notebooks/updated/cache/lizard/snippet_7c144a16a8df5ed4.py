def expert_dot_product(q, k, v, info_q, info_k):
    length_q = common_layers.shape_list(q)[0]
    length_k = common_layers.shape_list(k)[0]
    depth_v = v.get_shape().as_list()[-1]
    bias = attention_bias_coordinates(info_q.coordinates, info_k.coordinates)
    if info_k.order is not None:
        bias += attention_bias_future(info_q.order, info_k.order)
    q, k, v = [tf.expand_dims(tf.expand_dims(t, 0), 0) for t in (q, k, v)]

    def is_zero():
        zeros = tf.zeros(shape=[1, 1, length_q, depth_v], dtype=tf.float32)
        zeros = tf.Print(zeros, [length_k, length_q], 'length_k/length_q: ')
        return zeros

    def is_not_zero():
        return dot_product_attention(q, k, v, bias=bias, make_image_summary
            =False)
    v_out = tf.cond(tf.logical_or(tf.equal(length_q, 0), tf.equal(length_k,
        0)), is_zero, is_not_zero)
    v_out = tf.squeeze(v_out, axis=0)
    v_out = tf.squeeze(v_out, axis=0)
    return v_out