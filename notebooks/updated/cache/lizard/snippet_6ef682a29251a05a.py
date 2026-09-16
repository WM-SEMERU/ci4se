def stats(self, name, value):
    for counter in self._counters:
        counter.stats(name, value)