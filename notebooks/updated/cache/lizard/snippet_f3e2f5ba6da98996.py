def _inspect(instance):
    is_piper = isinstance(instance, Piper)
    is_function = isinstance(instance, FunctionType) or isbuiltin(instance)
    is_worker = isinstance(instance, Worker)
    is_iterable = getattr(instance, '__iter__', False) and not (is_piper or
        is_function or is_worker)
    is_iterable_p = is_iterable and isinstance(instance, Piper)
    is_iterable_f = is_iterable and (isinstance(instance[0], FunctionType) or
        isbuiltin(instance[0]))
    is_iterable_w = is_iterable and isinstance(instance[0], Worker)
    return (is_piper, is_worker, is_function, is_iterable_p, is_iterable_w,
        is_iterable_f)