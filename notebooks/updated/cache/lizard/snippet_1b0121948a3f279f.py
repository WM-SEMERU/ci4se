def load(path):
    ret = {}
    fmadm = _check_fmadm()
    cmd = '{cmd} load {path}'.format(cmd=fmadm, path=path)
    res = __salt__['cmd.run_all'](cmd)
    retcode = res['retcode']
    result = {}
    if retcode != 0:
        result['Error'] = res['stderr']
    else:
        result = True
    return result