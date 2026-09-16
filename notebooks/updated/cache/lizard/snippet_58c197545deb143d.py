def states(self):
    state_list = []
    for state in States:
        if state.value & self._states != 0:
            state_list.append(state)
    if self._flashing_states & States.FILTER != 0:
        state_list.append(States.FILTER_LOW_SPEED)
    return state_list