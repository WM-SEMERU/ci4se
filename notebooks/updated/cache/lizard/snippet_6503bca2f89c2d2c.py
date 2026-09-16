def initial_state(self, batch_size, dtype=tf.float32, trainable=False,
    trainable_initializers=None, trainable_regularizers=None, name=None):
    core_initial_state = self._core.initial_state(batch_size, dtype=dtype,
        trainable=trainable, trainable_initializers=trainable_initializers,
        trainable_regularizers=trainable_regularizers, name=name)
    dropout_masks = [None] * len(self._dropout_state_size)

    def set_dropout_mask(index, state, keep_prob):
        if index is not None:
            ones = tf.ones_like(state, dtype=dtype)
            dropout_masks[index] = tf.nn.dropout(ones, keep_prob=keep_prob)
    tf.contrib.framework.nest.map_structure(set_dropout_mask, self.
        _dropout_indexes, core_initial_state, self._keep_probs)
    return core_initial_state, dropout_masks