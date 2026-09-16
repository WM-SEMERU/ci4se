def effective_FPS(self):
    if self.start_time is None:
        self.start_time = 0
    elapsed = monotonic() - self.start_time
    return self.called / elapsed