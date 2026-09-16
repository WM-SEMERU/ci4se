def describe_version(self):
    self._seqid += 1
    d = self._reqs[self._seqid] = defer.Deferred()
    self.send_describe_version()
    return d