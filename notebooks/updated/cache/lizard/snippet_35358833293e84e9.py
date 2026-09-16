def wait(cond, msg=None, _timeout=10, _raiseException=True):
    status = False
    delay = 0.25
    elapsed = 0
    if msg is None and type(cond) is str:
        msg = cond
    if type(cond) is bool:
        if cond:
            log.warn(
                'Boolean passed as argument to wait. Make sure argument to wait is surrounded by a lambda or " "'
                )
        else:
            raise FalseWaitError(msg)
    if type(cond) in (int, float):
        gevent.sleep(cond)
        status = True
    else:
        while True:
            if _timeout is not None and elapsed >= _timeout:
                if _raiseException:
                    raise APITimeoutError(_timeout, msg)
                else:
                    status = False
                    break
            if type(cond) is str:
                caller = inspect.stack()[1][0]
                status = eval(cond, caller.f_globals, caller.f_locals)
            elif callable(cond):
                status = cond()
            else:
                status = cond
            if status:
                break
            gevent.sleep(delay)
            elapsed += delay
    return status