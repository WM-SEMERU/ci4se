def setMetadata(self, remote, address, key, value):
    try:
        return self.proxies['%s-%s' % (self._interface_id, remote)
            ].setMetadata(address, key, value)
    except Exception as err:
        LOG.debug('ServerThread.setMetadata: Exception: %s' % str(err))