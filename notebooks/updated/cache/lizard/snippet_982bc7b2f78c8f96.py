def record_timing(self, duration, *path):
    self.application.statsd.send(path, duration * 1000.0, 'ms')