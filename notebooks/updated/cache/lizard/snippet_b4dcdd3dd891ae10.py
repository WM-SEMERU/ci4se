def status(output=True, tgt='*', tgt_type='glob', timeout=None,
    gather_job_timeout=None):
    ret = {}
    if not timeout:
        timeout = __opts__['timeout']
    if not gather_job_timeout:
        gather_job_timeout = __opts__['gather_job_timeout']
    res = _ping(tgt, tgt_type, timeout, gather_job_timeout)
    ret['up'], ret['down'] = ([], []) if not res else res
    return ret