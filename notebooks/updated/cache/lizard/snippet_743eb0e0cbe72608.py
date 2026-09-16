def _expectation(p, mean1, none1, mean2, none2, nghp=None):
    with params_as_tensors_for(mean1, mean2):
        e_xxt = p.cov + p.mu[:, :, (None)] * p.mu[:, (None), :]
        e_A1t_xxt_A2 = tf.einsum('iq,nij,jz->nqz', mean1.A, e_xxt, mean2.A)
        e_A1t_x_b2t = tf.einsum('iq,ni,z->nqz', mean1.A, p.mu, mean2.b)
        e_b1_xt_A2 = tf.einsum('q,ni,iz->nqz', mean1.b, p.mu, mean2.A)
        e_b1_b2t = mean1.b[:, (None)] * mean2.b[(None), :]
        return e_A1t_xxt_A2 + e_A1t_x_b2t + e_b1_xt_A2 + e_b1_b2t