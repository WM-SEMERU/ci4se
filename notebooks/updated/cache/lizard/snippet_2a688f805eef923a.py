def to_backward_slashes(data):
    data = data.replace('/', '\\')
    LOGGER.debug("> Data: '{0}' to backward slashes.".format(data))
    return data