def step_size(self, t0, t1=None):
    tb0 = self.to_bucket(t0)
    if t1:
        tb1 = self.to_bucket(t1, steps=1)
    else:
        tb1 = self.to_bucket(t0, steps=1)
    days = (self.from_bucket(tb1, native=True) - self.from_bucket(tb0,
        native=True)).days
    return days * SIMPLE_TIMES['d']