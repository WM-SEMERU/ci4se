def _expectation(p, mean1, none1, mean2, none2, nghp=None):
    with params_as_tensors_for(mean1):
        N = tf.shape(p.mu)[0]
        e_xxt = p.cov + p.mu[:, :, (None)] * p.mu[:, (None), :]
        e_A_xxt = tf.matmul(tf.tile(mean1.A[None, ...], (N, 1, 1)), e_xxt,
            transpose_a=True)
        e_b_xt = mean1.b[(None), :, (None)] * p.mu[:, (None), :]
        return e_A_xxt + e_b_xt