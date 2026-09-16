def server(value=None):
    if value is None:
        return PyGraphistry._config['hostname']
    shortcuts = {'dev': 'localhost:3000', 'staging':
        'staging.graphistry.com', 'labs': 'labs.graphistry.com'}
    if value in shortcuts:
        resolved = shortcuts[value]
        PyGraphistry._config['hostname'] = resolved
        util.warn('Resolving alias %s to %s' % (value, resolved))
    else:
        PyGraphistry._config['hostname'] = value