def _save_function_initial_state(self, function_key, function_address, state):
    l.debug('Saving the initial state for function %#08x with function key %s',
        function_address, function_key)
    if function_key in self._function_initial_states[function_address]:
        existing_state = self._function_initial_states[function_address][
            function_key]
        merged_state, _, _ = existing_state.merge(state)
        self._function_initial_states[function_address][function_key
            ] = merged_state
    else:
        self._function_initial_states[function_address][function_key] = state