def delay(self, secondsLater):
    if self.cancelled:
        raise error.AlreadyCancelled
    elif self.called:
        raise error.AlreadyCalled
    else:
        self.delayed_time += secondsLater
        if self.delayed_time < 0:
            self.activate_delay()
            self.resetter(self)