def X_less(self):
    self.parent.value('window_length', self.parent.value('window_length') / 2)
    self.parent.overview.update_position()