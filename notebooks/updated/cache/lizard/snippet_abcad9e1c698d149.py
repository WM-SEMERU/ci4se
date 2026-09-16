def start(self, segment):
    if self.closed:
        raise UserCritical(msg='attempt to transfer wal after closing',
            hint='report a bug')
    g = gevent.Greenlet(self.transferer, segment)
    g.link(self._complete_execution)
    self.greenlets.add(g)
    self.expect += 1
    g.start()