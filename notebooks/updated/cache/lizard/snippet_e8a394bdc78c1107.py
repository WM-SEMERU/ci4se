def forward(self, data_batch, is_train=None, carry_state=True):
    if carry_state:
        if isinstance(self._next_states, (int, float)):
            self._module.set_states(value=self._next_states)
        else:
            self._module.set_states(states=self._next_states)
    self._module.forward(data_batch, is_train=is_train)
    outputs = self._module.get_outputs(merge_multi_context=False)
    self._next_states = outputs[:-1]