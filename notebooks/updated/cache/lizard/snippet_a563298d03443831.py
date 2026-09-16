def _add_help_noop_and_quit_transitions(self):
    states = set()
    for state_name in self.state.known_states():
        if state_name not in ['new', 'finished']:
            states.add(state_name)
    for state in states:
        self._add_state(state, 'NOOP', state)
        self._add_state(state, 'HELP', state)
        self._add_state(state, 'QUIT', 'finished')