def setPgConfigOptions(**kwargs):
    for key, value in kwargs.items():
        logger.debug('Setting PyQtGraph config option: {} = {}'.format(key,
            value))
    pg.setConfigOptions(**kwargs)