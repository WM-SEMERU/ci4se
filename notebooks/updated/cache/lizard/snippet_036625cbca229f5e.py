def done(self, result, noraise=False):
    if self.ev_done.is_set():
        if isinstance(self.result, Exception) and not noraise:
            raise self.result
        return self.result
    self.endtime = time.time()
    try:
        self.totaltime = self.endtime - self.starttime
    except AttributeError:
        self.totaltime = 0.0
    self.result = result
    self.ev_done.set()
    self.make_callback('resolved', self.result)
    if isinstance(result, Exception) and not noraise:
        raise result
    return result