def get(self, name=''):
    addrs = []
    with self._address_lock:
        for metadata in self._addresses.values():
            if name == '' or name and name in metadata['service']:
                mda = copy.copy(metadata)
                mda['receive_time'] = mda['receive_time'].isoformat()
                addrs.append(mda)
    LOGGER.debug('return address %s', str(addrs))
    return addrs