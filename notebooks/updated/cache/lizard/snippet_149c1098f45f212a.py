def counter(self, name):
    with self._lock:
        if name not in self._counters:
            if self._registry._ignore_patterns and any(pattern.match(name) for
                pattern in self._registry._ignore_patterns):
                counter = noop_metric
            else:
                counter = Counter(name)
            self._counters[name] = counter
        return self._counters[name]