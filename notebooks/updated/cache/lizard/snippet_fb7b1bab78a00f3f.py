def _bisect(self, begin, end, listener):
    step = (end.date - begin.date) / 2
    while abs(step) >= self._eps_bisect:
        date = begin.date + step
        if self.SPEAKER_MODE == 'global':
            orb = self.propagate(date)
        else:
            orb = begin.propagate(date)
        if listener(begin) * listener(orb) > 0:
            begin = orb
        else:
            end = orb
        step = (end.date - begin.date) / 2
    else:
        end.event = listener.info(end)
        return end