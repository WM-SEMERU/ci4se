def gru_feedfwd(a_t, h_prev, filters, name=None):
    with tf.variable_scope(name, default_name='GRU', values=[a_t, h_prev]):
        z_t = tf.sigmoid(tpu_conv1d(a_t, filters, 1, padding='SAME', name=
            'W_z') + tpu_conv1d(h_prev, filters, 1, padding='SAME', name='U_z')
            )
        r_t = tf.sigmoid(tpu_conv1d(a_t, filters, 1, padding='SAME', name=
            'W_r') + tpu_conv1d(h_prev, filters, 1, padding='SAME', name='U_r')
            )
        h_tilde = tf.tanh(tpu_conv1d(a_t, filters, 1, padding='SAME', name=
            'W') + tpu_conv1d(r_t * h_prev, filters, 1, padding='SAME',
            name='U'))
        h_t = (1.0 - z_t) * h_prev + z_t * h_tilde
    return h_t