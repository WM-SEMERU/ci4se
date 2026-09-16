def update(**kwargs):
    stdout = {}
    for mode in ('fetch', 'install'):
        err_ = {}
        ret = _wrapper(mode, err_=err_, **kwargs)
        if 'retcode' in err_ and err_['retcode'] != 0:
            return ret
        if 'stdout' in err_:
            stdout[mode] = err_['stdout']
    return '\n'.join(['{0}: {1}'.format(k, v) for k, v in six.iteritems(
        stdout)])