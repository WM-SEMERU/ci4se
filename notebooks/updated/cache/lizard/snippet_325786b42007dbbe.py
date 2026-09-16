def subparsers(**kwargs):

    def decorator(func):
        adaptor = ScriptAdaptor._get_adaptor(func)
        adaptor.subkwargs = kwargs
        adaptor.do_subs = True
        return func
    return decorator