def do_expire(self):
    _timeouts = deepcopy(self.timeouts)
    for key, value in _timeouts.items():
        if value - self.clock.now() < timedelta(0):
            del self.timeouts[key]
            if key in self.redis:
                self.redis.pop(key, None)