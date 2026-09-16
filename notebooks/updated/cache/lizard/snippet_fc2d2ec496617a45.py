def show(uuid):
    ret = {}
    fmdump = _check_fmdump()
    cmd = '{cmd} -u {uuid} -V'.format(cmd=fmdump, uuid=uuid)
    res = __salt__['cmd.run_all'](cmd)
    retcode = res['retcode']
    result = {}
    if retcode != 0:
        result['Error'] = 'error executing fmdump'
    else:
        result = _parse_fmdump_verbose(res['stdout'])
    return result