def undo(self):
    state = self.state_machine.root_state
    self.set_root_state_to_version(state, self.before_storage)