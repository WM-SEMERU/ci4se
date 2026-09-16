def state(self, state):
    state = state.lower()
    if state not in valid_states:
        raise ValueError('Build state must have a value from:\n{}'.format(
            ', '.join(valid_state)))
    self.obj['state'] = state
    self.changes.append('Updating build:{}.state={}'.format(self.obj['name'
        ], state))
    return self