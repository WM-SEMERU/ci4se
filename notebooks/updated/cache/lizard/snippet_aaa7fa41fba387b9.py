def func_attr(f, attr):
    if hasattr(f, 'func_%s' % attr):
        return getattr(f, 'func_%s' % attr)
    elif hasattr(f, '__%s__' % attr):
        return getattr(f, '__%s__' % attr)
    else:
        raise ValueError('Object %s has no attr' % (str(f), attr))