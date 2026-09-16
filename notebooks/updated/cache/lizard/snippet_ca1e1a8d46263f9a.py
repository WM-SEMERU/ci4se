def alf(attrs=None, where=None):
    if salt.utils.platform.is_darwin():
        return _osquery_cmd(table='alf', attrs=attrs, where=where)
    return {'result': False, 'comment': 'Only available on macOS systems.'}