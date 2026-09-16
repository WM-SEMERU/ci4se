def argument_group(group, **kwargs):

    def decorator(func):
        adaptor = ScriptAdaptor._get_adaptor(func)
        adaptor._add_group(group, 'group', kwargs)
        return func
    return decorator