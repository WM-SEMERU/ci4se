def get_source(label, source_type, **kwargs):
    if source_type not in yapconf.ALL_SUPPORTED_SOURCES:
        raise YapconfSourceError(
            'Invalid source type %s. Supported types are %s.' % (
            source_type, yapconf.ALL_SUPPORTED_SOURCES))
    if source_type not in yapconf.SUPPORTED_SOURCES:
        raise YapconfSourceError(
            'Unsupported source type "%s". If you want to use this type, you will need to install the correct client for it (try `pip install yapconf[%s]. Currently supported types are %s. All supported types are %s'
             % (source_type, source_type, yapconf.SUPPORTED_SOURCES,
            yapconf.ALL_SUPPORTED_SOURCES))
    if source_type == 'dict':
        return DictConfigSource(label, data=kwargs.get('data'))
    elif source_type == 'json':
        return JsonConfigSource(label, **kwargs)
    elif source_type == 'yaml':
        filename = kwargs.get('filename')
        if 'filename' in kwargs:
            kwargs.pop('filename')
        return YamlConfigSource(label, filename, **kwargs)
    elif source_type == 'environment':
        return EnvironmentConfigSource(label)
    elif source_type == 'etcd':
        return EtcdConfigSource(label, kwargs.get('client'), kwargs.get(
            'key', '/'))
    elif source_type == 'kubernetes':
        name = kwargs.get('name')
        if 'name' in kwargs:
            kwargs.pop('name')
        client = kwargs.get('client')
        if 'client' in kwargs:
            kwargs.pop('client')
        return KubernetesConfigSource(label, client, name, **kwargs)
    else:
        raise NotImplementedError('No implementation for source type %s' %
            source_type)