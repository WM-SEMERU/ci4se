def call_remote_api(self, func_name, *args, **kwargs):
    f = getattr(remote_api, func_name)
    mode = self._extract_mode(kwargs)
    kwargs['operationMode'] = vrep_mode[mode]
    if '_force' in kwargs:
        del kwargs['_force']
        _force = True
    else:
        _force = False
    for _ in range(VrepIO.MAX_ITER):
        with self._lock:
            ret = f(self.client_id, *args, **kwargs)
        if _force:
            return
        if mode == 'sending' or isinstance(ret, int):
            err, res = ret, None
        else:
            err, res = ret[0], ret[1:]
            res = res[0] if len(res) == 1 else res
        err = [bool(err >> i & 1) for i in range(len(vrep_error))]
        if remote_api.simx_return_novalue_flag not in err:
            break
        time.sleep(VrepIO.TIMEOUT)
    if any(err):
        msg = ' '.join([vrep_error[2 ** i] for i, e in enumerate(err) if e])
        raise VrepIOErrors(msg)
    return res