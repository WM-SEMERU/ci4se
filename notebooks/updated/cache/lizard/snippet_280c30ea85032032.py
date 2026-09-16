def weave(target, advices, pointcut=None, ctx=None, depth=1, public=False,
    pointcut_application=None, ttl=None):
    result = []
    if isroutine(advices):
        advices = [advices]
    if advices:
        if pointcut is None or callable(pointcut):
            pass
        elif isinstance(pointcut, string_types):
            pointcut = _namematcher(pointcut)
        else:
            error_msg = 'Wrong pointcut to check weaving on {0}.'
            error_msg = error_msg.format(target)
            advice_msg = 'Must be None, or be a str or a function/method.'
            right_msg = 'Not {0}'.format(type(pointcut))
            raise AdviceError('{0} {1} {2}'.format(error_msg, advice_msg,
                right_msg))
        if ctx is None:
            ctx = find_ctx(elt=target)
        _weave(target=target, advices=advices, pointcut=pointcut, depth=
            depth, depth_predicate=_publiccallable if public else callable,
            ctx=ctx, intercepted=result, pointcut_application=
            pointcut_application)
        if ttl is not None:
            kwargs = {'target': target, 'advices': advices, 'pointcut':
                pointcut, 'depth': depth, 'public': public, 'ctx': ctx}
            timer = Timer(ttl, unweave, kwargs=kwargs)
            timer.start()
            result = result, timer
    return result