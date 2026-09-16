def unroll(self, length, inputs, begin_state=None, layout='NTC',
    merge_outputs=None, valid_length=None):
    if self.drop_states:
        return super(VariationalDropoutCell, self).unroll(length, inputs,
            begin_state, layout, merge_outputs, valid_length=valid_length)
    self.reset()
    inputs, axis, F, batch_size = _format_sequence(length, inputs, layout, True
        )
    states = _get_begin_state(self, F, begin_state, inputs, batch_size)
    if self.drop_inputs:
        inputs = F.Dropout(inputs, p=self.drop_inputs, axes=(axis,))
    outputs, states = self.base_cell.unroll(length, inputs, states, layout,
        merge_outputs=True, valid_length=valid_length)
    if self.drop_outputs:
        outputs = F.Dropout(outputs, p=self.drop_outputs, axes=(axis,))
    merge_outputs = isinstance(outputs, tensor_types
        ) if merge_outputs is None else merge_outputs
    outputs, _, _, _ = _format_sequence(length, outputs, layout, merge_outputs)
    if valid_length is not None:
        outputs = _mask_sequence_variable_length(F, outputs, length,
            valid_length, axis, merge_outputs)
    return outputs, states