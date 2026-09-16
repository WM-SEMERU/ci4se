def context(self, id):
    if id not in self.circuits:
        self.circuits[id] = self.factory(self.clock, self.log.getChild(id),
            self.error_types, self.maxfail, self.reset_timeout, self.
            time_unit, backoff_cap=self.backoff_cap, with_jitter=self.
            with_jitter)
    return self.circuits[id]