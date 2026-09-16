def spawn_later(self, ms, f, *a):
    self.scheduled.add(ms, f, *a)