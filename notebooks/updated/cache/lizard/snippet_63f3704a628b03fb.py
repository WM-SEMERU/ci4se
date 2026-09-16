def set_duration(self, duration):
    if duration > 0:
        self.duration = duration
        self.server.request('screen_set %s duration %i' % (self.ref, self.
            duration * 8))