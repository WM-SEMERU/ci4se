def timed_call(self, ms, callback, *args, **kwargs):
    return self.loop.timed_call(ms, callback, *args, **kwargs)