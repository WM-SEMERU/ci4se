def _keygen(self, event, ts=None):
    return '%s:%s' % (self.namespace(ts or time.time()), event)