def change_state_id(self, state_id=None):
    if state_id is None:
        state_id = state_id_generator(used_state_ids=[self.state_id])
    if not self.is_root_state and not self.is_root_state_of_library:
        used_ids = list(self.parent.states.keys()) + [self.parent.state_id,
            self.state_id]
        if state_id in used_ids:
            state_id = state_id_generator(used_state_ids=used_ids)
    self._state_id = state_id