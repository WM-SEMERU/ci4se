def read(self, client):
    val = None
    if self.no_resource:
        return val
    LOG.debug('Reading from %s', self)
    try:
        val = client.read(self.path)
    except hvac.exceptions.InvalidRequest as vault_exception:
        if str(vault_exception).startswith('no handler for route'):
            val = None
    return val