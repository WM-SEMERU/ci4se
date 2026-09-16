def correlation(ina, inb, kernel_size, max_displacement, stride_1, stride_2,
    pad, data_format):
    assert pad == max_displacement
    assert kernel_size == 1
    assert data_format == 'NCHW'
    assert max_displacement % stride_2 == 0
    assert stride_1 == 1
    D = int(max_displacement / stride_2 * 2) + 1
    b, c, h, w = ina.shape.as_list()
    inb = tf.pad(inb, [[0, 0], [0, 0], [pad, pad], [pad, pad]])
    res = []
    for k1 in range(0, D):
        start_h = k1 * stride_2
        for k2 in range(0, D):
            start_w = k2 * stride_2
            s = tf.slice(inb, [0, 0, start_h, start_w], [-1, -1, h, w])
            ans = tf.reduce_mean(ina * s, axis=1, keepdims=True)
            res.append(ans)
    res = tf.concat(res, axis=1)
    return res