def _data(self, pipe=None):
    pipe = self.redis if pipe is None else pipe
    return [self._unpickle(v) for v in pipe.lrange(self.key, 0, -1)]