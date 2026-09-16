def timestamp(self, message='', checkpoint=None, finished=False,
    raise_error=True):
    if self.halt_on_next:
        self.halt(checkpoint, finished, raise_error=raise_error)
    if checkpoint:
        if finished:
            self._checkpoint(checkpoint)
            self.prev_checkpoint = checkpoint
            self.curr_checkpoint = None
        else:
            self.prev_checkpoint = self.curr_checkpoint
            self.curr_checkpoint = checkpoint
            self._checkpoint(self.prev_checkpoint)
        if (finished and checkpoint == self.stop_after or not finished and 
            checkpoint == self.stop_before):
            self.halt(checkpoint, finished, raise_error=raise_error)
        elif checkpoint == self.start_point:
            self._active = True
        if not finished and checkpoint == self.stop_after:
            self.halt_on_next = True
    elapsed = self.time_elapsed(self.last_timestamp)
    t = time.strftime('%m-%d %H:%M:%S')
    if checkpoint is None:
        msg = '{m} ({t}) elapsed: {delta_t} _TIME_'.format(m=message, t=t,
            delta_t=elapsed)
    else:
        msg = '{m} ({t}) ({status} {stage}) elapsed: {delta_t} _TIME_'.format(m
            =message, t=t, status='finished' if finished else 'starting',
            stage=checkpoint, delta_t=elapsed)
    if re.match('^###', message):
        msg = '\n{}\n'.format(msg)
    print(msg)
    self.last_timestamp = time.time()