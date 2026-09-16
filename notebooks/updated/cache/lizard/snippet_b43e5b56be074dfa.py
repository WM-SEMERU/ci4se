def build_pair(self, losses, stats):
    P, R = len(self.return_periods), len(self.weights)
    assert len(losses) == R, len(losses)
    array = numpy.zeros((P, R), F32)
    for r, ls in enumerate(losses):
        ne = self.num_events.get(r, 0)
        if ne:
            array[:, (r)] = losses_by_period(ls, self.return_periods, ne,
                self.eff_time)
    return self.pair(array, stats)