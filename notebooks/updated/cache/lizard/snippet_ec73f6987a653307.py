def ClientFromConfig(engine, config, database, logger=None, verbose=True):
    if type(config) == list:
        config = dict(config)
    if engine == 'couchbase':
        return Client(engine=engine, host=config.get('host'), auth=config.
            get('bucket_%s' % database), logger=logger, verbose=verbose)
    elif engine == 'couchdb':
        if config.get('admin_user') and config.get('admin_password'):
            auth = '%s:%s' % (config.get('admin_user'), config.get(
                'admin_password'))
        elif config.get('user') and config.get('password'):
            auth = '%s:%s' % (config.get('user'), config.get('password'))
        else:
            auth = None
        return Client(engine=engine, host=config.get('host'), auth=auth,
            database=config.get('db_%s' % database), logger=logger, verbose
            =verbose)
    elif engine == 'dummydb':
        return Client(engine=engine)
    else:
        raise InvalidEngineException(engine)