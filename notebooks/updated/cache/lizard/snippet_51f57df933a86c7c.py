def formatter_class(klass):

    def decorator(func):
        adaptor = ScriptAdaptor._get_adaptor(func)
        adaptor.formatter_class = klass
        return func
    return decorator