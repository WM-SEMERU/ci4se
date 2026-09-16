def replace(self, episodes, length, rows=None):
    rows = tf.range(self._capacity) if rows is None else rows
    assert rows.shape.ndims == 1
    assert_capacity = tf.assert_less(rows, self._capacity, message=
        'capacity exceeded')
    with tf.control_dependencies([assert_capacity]):
        assert_max_length = tf.assert_less_equal(length, self._max_length,
            message='max length exceeded')
    with tf.control_dependencies([assert_max_length]):
        replace_ops = tools.nested.map(lambda var, val: tf.scatter_update(
            var, rows, val), self._buffers, episodes, flatten=True)
    with tf.control_dependencies(replace_ops):
        return tf.scatter_update(self._length, rows, length)