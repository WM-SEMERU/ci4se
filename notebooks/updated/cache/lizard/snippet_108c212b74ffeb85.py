def _data(self, pipe=None):
    pipe = self.redis if pipe is None else pipe
    items = pipe.hgetall(self.key).items()
    return {self._unpickle_key(k): self._unpickle(v) for k, v in items}