def check_if_outcome_already_connected(self, from_state_id, from_outcome):
    for trans_key, transition in self.transitions.items():
        if transition.from_state == from_state_id:
            if transition.from_outcome == from_outcome:
                raise AttributeError(
                    'Outcome %s of state %s is already connected' % (str(
                    from_outcome), str(from_state_id)))