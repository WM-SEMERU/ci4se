def reprioritize(self, stream_id, depends_on=None, weight=16, exclusive=False):
    self._priority.reprioritize(stream_id, depends_on, weight, exclusive)