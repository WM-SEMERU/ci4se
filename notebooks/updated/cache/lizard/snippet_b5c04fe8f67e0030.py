def createRtiFromFileName(fileName):
    cls, rtiRegItem = detectRtiFromFileName(fileName)
    if cls is None:
        logger.warn('Unable to import plugin {}: {}'.format(rtiRegItem.
            fullName, rtiRegItem.exception))
        rti = UnknownFileRti.createFromFileName(fileName)
        rti.setException(rtiRegItem.exception)
    else:
        rti = cls.createFromFileName(fileName)
    assert rti, 'Sanity check failed (createRtiFromFileName). Please report this bug.'
    return rti