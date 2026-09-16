def check_call(*popenargs, **kwargs):
    retcode = call(*popenargs, **kwargs)
    cmd = kwargs.get('args')
    if cmd is None:
        cmd = popenargs[0]
    if retcode:
        raise CalledProcessError(retcode, cmd)
    return retcode