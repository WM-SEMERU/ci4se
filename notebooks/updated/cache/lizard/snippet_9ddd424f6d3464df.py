def save(self, file):
    d = {'framerate': self.framerate, 'positions': self._timed_positions}
    json.dump(d, file, indent=2)