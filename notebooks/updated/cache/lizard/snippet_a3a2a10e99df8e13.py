def _get_delay(self, userdelay, frameslist):
    delay = userdelay or getattr(frameslist, 'delay', None)
    delay = (delay or self.default_delay) - self.nice_delay
    if delay < 0:
        delay = 0
    return delay