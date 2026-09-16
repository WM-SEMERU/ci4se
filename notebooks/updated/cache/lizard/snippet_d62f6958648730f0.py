def toggle_minmax(self, state):
    self.sig_option_changed.emit('minmax', state)
    self.model.minmax = state