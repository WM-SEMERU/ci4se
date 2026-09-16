def sequence_edit_distance(predictions, labels, weights_fn=common_layers.
    weights_nonzero):
    if weights_fn is not common_layers.weights_nonzero:
        raise ValueError('Only weights_nonzero can be used for this metric.')
    with tf.variable_scope('edit_distance', values=[predictions, labels]):
        predictions = tf.to_int32(tf.squeeze(tf.argmax(predictions, axis=-1
            ), axis=(2, 3)))
        nonzero_idx = tf.where(tf.not_equal(predictions, 0))
        sparse_outputs = tf.SparseTensor(nonzero_idx, tf.gather_nd(
            predictions, nonzero_idx), tf.shape(predictions, out_type=tf.int64)
            )
        labels = tf.squeeze(labels, axis=(2, 3))
        nonzero_idx = tf.where(tf.not_equal(labels, 0))
        label_sparse_outputs = tf.SparseTensor(nonzero_idx, tf.gather_nd(
            labels, nonzero_idx), tf.shape(labels, out_type=tf.int64))
        distance = tf.reduce_sum(tf.edit_distance(sparse_outputs,
            label_sparse_outputs, normalize=False))
        reference_length = tf.to_float(common_layers.shape_list(nonzero_idx)[0]
            )
        return distance / reference_length, reference_length