def collect_variables(self, g_scope='gen', d_scope='discrim'):
    self.g_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, g_scope)
    assert self.g_vars
    self.d_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, d_scope)
    assert self.d_vars