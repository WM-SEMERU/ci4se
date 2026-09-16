def set_velocities(self, velocities):
    assert len(velocities) == len(self.mol)
    self.params['velocity'] = velocities