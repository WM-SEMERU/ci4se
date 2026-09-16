def memory_map(attrs=None, where=None):
    if __grains__['os_family'] in ['RedHat', 'Debian']:
        return _osquery_cmd(table='memory_map', attrs=attrs, where=where)
    return {'result': False, 'comment':
        'Only available on Red Hat or Debian based systems.'}