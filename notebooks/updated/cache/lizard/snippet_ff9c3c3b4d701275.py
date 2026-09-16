def create_hash(self, initial, capacity, error):
    self.hash = 0
    self.hashbits, self.num_hashes = self._optimal_size(capacity, error)
    if len(initial):
        if type(initial) == str:
            self.add(initial)
        else:
            for t in initial:
                self.add(t)