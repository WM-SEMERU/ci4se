def gpg_error(exception, message):
    LOGGER.debug('GPG Command %s', ' '.join([str(x) for x in exception.cmd]))
    LOGGER.debug('GPG Output %s', exception.output)
    raise CryptoritoError(message)