def __init_defaults(self, config):
    provider = self.__provider
    if provider == 'sqlite':
        config.setdefault('dbname', ':memory:')
        config.setdefault('create_db', True)
    elif provider == 'mysql':
        config.setdefault('port', 3306)
        config.setdefault('charset', 'utf8')
    elif provider == 'postgres':
        config.setdefault('port', 5432)
    elif provider == 'oracle':
        config.setdefault('port', 1521)
    else:
        raise ValueError('Unsupported provider "{}"'.format(provider))
    if provider != 'sqlite':
        config.setdefault('host', 'localhost')
        config.setdefault('user', None)
        config.setdefault('password', None)
        config.setdefault('dbname', None)