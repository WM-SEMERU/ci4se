def set_interval(self, start, end, value, compact=False):
    for i, (s, e, v) in enumerate(self.iterperiods(start, end)):
        if i == 0:
            self.set(s, value, compact)
        else:
            del self[s]
    self.set(end, v, compact)