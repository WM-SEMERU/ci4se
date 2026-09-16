def describe_keyspaces(self):
    self._seqid += 1
    d = self._reqs[self._seqid] = defer.Deferred()
    self.send_describe_keyspaces()
    return d