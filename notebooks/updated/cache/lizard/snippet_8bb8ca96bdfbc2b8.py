def item_properties(self, handle):
    logger.debug('Getting properties for handle: {}'.format(handle))
    properties = {'size_in_bytes': self.get_size_in_bytes(handle),
        'utc_timestamp': self.get_utc_timestamp(handle), 'hash': self.
        get_hash(handle), 'relpath': self.get_relpath(handle)}
    logger.debug('{} properties: {}'.format(handle, properties))
    return properties