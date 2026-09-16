def set_data_value(datastore, path, data):
    if isinstance(path, six.string_types):
        path = '/'.split(path)
    return _proxy_cmd('set_data_value', datastore, path, data)