def reset(self, period=None):
    if period is not None:
        self.period = period
    self.reset_event.set()