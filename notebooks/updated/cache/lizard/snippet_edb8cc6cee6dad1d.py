def get_backend(config):
    backend_string = get_conf(config, 'Dagobahd.backend', None)
    if backend_string is None:
        from ..backend.base import BaseBackend
        return BaseBackend()
    elif backend_string.lower() == 'mongo':
        backend_kwargs = {}
        for conf_kwarg in ['host', 'port', 'db', 'dagobah_collection',
            'job_collection', 'log_collection']:
            backend_kwargs[conf_kwarg] = get_conf(config, 'MongoBackend.%s' %
                conf_kwarg)
        backend_kwargs['port'] = int(backend_kwargs['port'])
        try:
            from ..backend.mongo import MongoBackend
        except:
            raise ImportError(
                'Could not initialize the MongoDB Backend. Are you sure' +
                ' the optional drivers are installed? If not, try running ' +
                '"pip install pymongo" to install them.')
        return MongoBackend(**backend_kwargs)
    raise ValueError('unknown backend type specified in conf')