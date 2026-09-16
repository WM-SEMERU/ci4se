def _build(self):
    if 'w' not in self._initializers:
        stddev = 1 / math.sqrt(np.prod(self._shape))
        self._initializers['w'] = tf.truncated_normal_initializer(stddev=stddev
            )
    self._w = tf.get_variable('w', shape=self._shape, dtype=self._dtype,
        initializer=self._initializers['w'], partitioner=self._partitioners
        .get('w', None), regularizer=self._regularizers.get('w', None))
    return self._w