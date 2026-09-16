def ping(self, remote):
    try:
        self.proxies['%s-%s' % (self._interface_id, remote)].ping('%s-%s' %
            (self._interface_id, remote))
    except Exception as err:
        LOG.warning('ServerThread.ping: Exception: %s' % str(err))