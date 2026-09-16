def set_max_clients(limit):
    global _dirty, _max_clients
    LOGGER.debug('Setting maximum client limit to %i', limit)
    _dirty = True
    _max_clients = limit