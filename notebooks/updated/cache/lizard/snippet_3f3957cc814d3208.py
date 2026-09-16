def ttl(self, steps, relative_time=None):
    if steps:
        if relative_time:
            rtime = self.to_bucket(relative_time)
            ntime = self.to_bucket(time.time())
            if ntime - rtime > steps:
                return 0
            else:
                return (steps + rtime - ntime) * self._step
        return steps * self._step
    return None