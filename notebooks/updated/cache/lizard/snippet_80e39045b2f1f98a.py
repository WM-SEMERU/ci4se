def state_size(self):
    if self._max_unique_stats == 1:
        return tf.TensorShape([self._hidden_size]), tf.TensorShape([self.
            _hidden_size])
    else:
        return tf.TensorShape([self._hidden_size]), tf.TensorShape([self.
            _hidden_size]), tf.TensorShape(1)