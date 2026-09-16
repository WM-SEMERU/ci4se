def log(self):
    if self.tot < 3:
        return
    msgs = []
    for name, t in self.times:
        if t / self.tot > 0.3 and t > 1:
            msgs.append(name + ': ' + humanize_time_delta(t))
    logger.info('Callbacks took {:.3f} sec in total. {}'.format(self.tot,
        '; '.join(msgs)))