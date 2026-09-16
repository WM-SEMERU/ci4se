def append_provenance_step(self, title, description, timestamp=None):
    step_time = self._provenance.append_step(title, description, timestamp)
    if step_time > self.last_update:
        self.last_update = step_time