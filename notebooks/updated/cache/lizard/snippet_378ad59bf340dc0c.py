def _reset_state_mode(self, state, mode):
    state.set_mode(mode)
    state.options |= self._state_add_options
    state.options = state.options.difference(self._state_remove_options)