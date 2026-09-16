def wait_for(func, timeout=10, step=1, default=None, func_args=(),
    func_kwargs=None):
    if func_kwargs is None:
        func_kwargs = dict()
    max_time = time.time() + timeout
    step = min(step or 1, timeout) * BLUR_FACTOR
    ret = default
    while time.time() <= max_time:
        call_ret = func(*func_args, **func_kwargs)
        if call_ret:
            ret = call_ret
            break
        else:
            time.sleep(step)
            step = min(step, max_time - time.time()) * BLUR_FACTOR
    if time.time() > max_time:
        log.warning('Exceeded waiting time (%s seconds) to exectute %s',
            timeout, func)
    return ret