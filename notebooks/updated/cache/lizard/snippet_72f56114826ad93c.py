def global_var(self, name):
    self.newline_label(name, False, True)
    self.newline_text('WORD\t1', True)