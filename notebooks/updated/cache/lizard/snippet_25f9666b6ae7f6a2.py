def start_state_id(self):
    for transition_id in self.transitions:
        if self.transitions[transition_id].from_state is None:
            to_state = self.transitions[transition_id].to_state
            if to_state is not None:
                return to_state
            else:
                return self.state_id
    return None