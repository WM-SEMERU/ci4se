def decompile(f):
    co = f.__code__
    args, kwonly, varargs, varkwargs = paramnames(co)
    annotations = f.__annotations__ or {}
    defaults = list(f.__defaults__ or ())
    kw_defaults = f.__kwdefaults__ or {}
    if f.__name__ == '<lambda>':
        node = ast.Lambda
        body = pycode_to_body(co, DecompilationContext(in_lambda=True))[0]
        extra_kwargs = {}
    else:
        node = ast.FunctionDef
        body = pycode_to_body(co, DecompilationContext(in_function_block=True))
        extra_kwargs = {'decorator_list': [], 'returns': annotations.get(
            'return')}
    return node(name=f.__name__, args=make_function_arguments(args=args,
        kwonly=kwonly, varargs=varargs, varkwargs=varkwargs, defaults=
        defaults, kw_defaults=kw_defaults, annotations=annotations), body=
        body, **extra_kwargs)