def set_style(self, input_feeds):
    sess = tf.get_default_session()
    computed = sess.run(self.input_grams, input_feeds)
    for v, g in zip(self.target_vars, computed):
        v.load(g)