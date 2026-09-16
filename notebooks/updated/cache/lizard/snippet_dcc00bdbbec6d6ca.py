def _build(self, inputs, prev_state):
    prev_hidden, prev_cell = prev_state
    if self._hidden_clip_value is not None:
        prev_hidden = tf.clip_by_value(prev_hidden, -self.
            _hidden_clip_value, self._hidden_clip_value)
    if self._cell_clip_value is not None:
        prev_cell = tf.clip_by_value(prev_cell, -self._cell_clip_value,
            self._cell_clip_value)
    self._create_gate_variables(inputs.get_shape(), inputs.dtype)
    inputs_and_hidden = tf.concat([inputs, prev_hidden], 1)
    gates = tf.matmul(inputs_and_hidden, self._w_xh)
    if self._use_layer_norm:
        gates = layer_norm.LayerNorm()(gates)
    gates += self._b
    i, j, f, o = tf.split(value=gates, num_or_size_splits=4, axis=1)
    if self._use_peepholes:
        self._create_peephole_variables(inputs.dtype)
        f += self._w_f_diag * prev_cell
        i += self._w_i_diag * prev_cell
    forget_mask = tf.sigmoid(f + self._forget_bias)
    next_cell = forget_mask * prev_cell + tf.sigmoid(i) * tf.tanh(j)
    cell_output = next_cell
    if self._use_peepholes:
        cell_output += self._w_o_diag * cell_output
    next_hidden = tf.tanh(cell_output) * tf.sigmoid(o)
    if self._use_projection:
        next_hidden = tf.matmul(next_hidden, self._w_h_projection)
    return next_hidden, LSTMState(hidden=next_hidden, cell=next_cell)