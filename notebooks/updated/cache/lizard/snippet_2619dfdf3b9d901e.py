def register_magnitude_model(self, pid):
    if self.assignments['forward_model'] is None:
        self.assignments['forward_model'] = [None, None]
    self.assignments['forward_model'][0] = pid