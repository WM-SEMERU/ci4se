def canAdd(self, filename):
    try:
        result = self.run(['add', '-n', '-t', 'text', filename])[0]
    except errors.CommandError as err:
        LOGGER.debug(err)
        return False
    if result.get('code') not in ('error', 'info'):
        return True
    LOGGER.warn('Unable to add {}: {}'.format(filename, result['data']))
    return False