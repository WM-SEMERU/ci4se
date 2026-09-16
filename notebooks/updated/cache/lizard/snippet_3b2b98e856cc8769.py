def remove_transition(self, transition_id, destroy=True):
    if transition_id == -1 or transition_id == -2:
        raise AttributeError(
            'The transition_id must not be -1 (Aborted) or -2 (Preempted)')
    if transition_id not in self._transitions:
        raise AttributeError('The transition_id %s does not exist' % str(
            transition_id))
    self.transitions[transition_id].parent = None
    return self.transitions.pop(transition_id)