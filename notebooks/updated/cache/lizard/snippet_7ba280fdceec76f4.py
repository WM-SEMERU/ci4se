def _multicall(hook_impls, caller_kwargs, firstresult=False):
    __tracebackhide__ = True
    results = []
    excinfo = None
    try:
        teardowns = []
        try:
            for hook_impl in reversed(hook_impls):
                try:
                    args = [caller_kwargs[argname] for argname in hook_impl
                        .argnames]
                except KeyError:
                    for argname in hook_impl.argnames:
                        if argname not in caller_kwargs:
                            raise HookCallError(
                                'hook call must provide argument %r' % (
                                argname,))
                if hook_impl.hookwrapper:
                    try:
                        gen = hook_impl.function(*args)
                        next(gen)
                        teardowns.append(gen)
                    except StopIteration:
                        _raise_wrapfail(gen, 'did not yield')
                else:
                    res = hook_impl.function(*args)
                    if res is not None:
                        results.append(res)
                        if firstresult:
                            break
        except BaseException:
            excinfo = sys.exc_info()
    finally:
        if firstresult:
            outcome = _Result(results[0] if results else None, excinfo)
        else:
            outcome = _Result(results, excinfo)
        for gen in reversed(teardowns):
            try:
                gen.send(outcome)
                _raise_wrapfail(gen, 'has second yield')
            except StopIteration:
                pass
        return outcome.get_result()